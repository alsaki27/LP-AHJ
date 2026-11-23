from __future__ import annotations
import csv, math, re, json, urllib.parse, urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[2]  # LP workspace root
AUDIT = Path(__file__).resolve().parent
SERVICE = "https://imagery.nationalmap.gov/arcgis/rest/services/USGSNAIPImagery/ImageServer/exportImage"
CAPTURED = datetime.now().astimezone().isoformat(timespec="minutes")
WIDTH_M, HEIGHT_M = 900.0, 650.0
PIX_W, PIX_H = 1200, 900
ATTRIBUTION = "Imagery: USGS, USDA FSA NAIP; The National Map Orthoimagery. Service metadata: 2025-01-09; acquisition date not resolved."

try:
    FONT = ImageFont.truetype("arial.ttf", 23)
    SMALL = ImageFont.truetype("arial.ttf", 16)
except OSError:
    FONT = ImageFont.load_default()
    SMALL = ImageFont.load_default()

sources = [
    ("segment0", AUDIT / "segment0" / "segment0_corridor_sample_targets.csv", "sample_lat", "sample_lon", "snapshot_id", "route_feature_id"),
    ("segment1", AUDIT / "segment1" / "segment1_imagery_targets.csv", "lat", "lon", "route_feature_id", "ODOT_SFN"),
    ("chicago_spurs", AUDIT / "chicago_spurs" / "chicago_spurs_google_imagery_targets.csv", "latitude", "longitude", "target_id", "feature_id"),
]

def sanitize(value: str) -> str:
    return re.sub(r"[^A-Za-z0-9_.-]+", "_", value).strip("_")[:96]

def fetch_one(item):
    route, row, lat_col, lon_col, id_col, aux_col = item
    lat, lon = float(row[lat_col]), float(row[lon_col])
    deg_lat = HEIGHT_M / 111320.0
    deg_lon = WIDTH_M / (111320.0 * math.cos(math.radians(lat)))
    bbox = f"{lon-deg_lon/2:.8f},{lat-deg_lat/2:.8f},{lon+deg_lon/2:.8f},{lat+deg_lat/2:.8f}"
    params = urllib.parse.urlencode({"bbox":bbox,"bboxSR":"4326","imageSR":"4326","size":f"{PIX_W},{PIX_H}","format":"jpg","f":"image","interpolation":"RSP_Bilinear"})
    url = SERVICE + "?" + params
    req = urllib.request.Request(url, headers={"User-Agent":"LP-AHJ imagery audit/1.0"})
    with urllib.request.urlopen(req, timeout=90) as response:
        data = response.read()
        ctype = response.headers.get("Content-Type", "")
    if "image" not in ctype.lower() or not data.startswith(b"\xff\xd8"):
        raise RuntimeError(f"Non-image response ({ctype}) for {route} {row.get(id_col)}")
    raw = Image.open(__import__("io").BytesIO(data)).convert("RGB")
    canvas = Image.new("RGB", (PIX_W, PIX_H+118), "white")
    canvas.paste(raw, (0, 64))
    draw = ImageDraw.Draw(canvas)
    target = row.get(id_col, "target")
    feature = row.get(aux_col, "")
    name = f"{route.upper()}  |  {target}" + (f"  |  {feature}" if feature else "")
    draw.text((16, 15), name[:100], fill=(20, 37, 58), font=FONT)
    # Target coordinate is the supplied screening/sample point, not a surveyed location.
    cx, cy = PIX_W//2, 64+PIX_H//2
    draw.ellipse((cx-13,cy-13,cx+13,cy+13),fill=(220,20,45),outline="white",width=4)
    draw.line((cx-24,cy,cx+24,cy),fill="white",width=2)
    draw.line((cx,cy-24,cx,cy+24),fill="white",width=2)
    draw.rectangle((0, PIX_H+64, PIX_W, PIX_H+118), fill=(250,250,250))
    draw.text((12, PIX_H+75), ATTRIBUTION, fill=(34,34,34), font=SMALL)
    draw.text((12, PIX_H+98), f"Snapshot retrieved {CAPTURED}; target {lat:.6f}, {lon:.6f}; 900 x 650 m crop. Visual screen only.", fill=(65,65,65), font=SMALL)
    out_dir = AUDIT / route / "naip_snapshots"
    out_dir.mkdir(parents=True, exist_ok=True)
    file_id = sanitize(f"{target}_{row.get(aux_col, '')}_{lat:.5f}_{lon:.5f}")
    out_path = out_dir / f"{route}_{file_id}.jpg"
    canvas.save(out_path, quality=90, optimize=True)
    return {"route":route,"target_id":file_id,"route_feature_id":row.get(id_col,""),"feature_id":row.get(aux_col,""),"lat":lat,"lon":lon,"image":str(out_path.relative_to(ROOT)).replace("\\","/"),"source":SERVICE,"imagery_metadata_date":"2025-01-09 (service copyright metadata; not the per-pixel acquisition date)","snapshot_retrieved":CAPTURED,"google_link":row.get("google_maps_satellite_url", row.get("imagery_link", row.get("google_satellite_url",""))),"screening_note":"Target coordinate supplied by route screening register; not a surveyed crossing point. Acquisition date and actual crossing/jurisdiction require confirmation."}

jobs=[]
for route, csv_path, lat_col, lon_col, id_col, aux_col in sources:
    with csv_path.open(encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            if row.get(lat_col) and row.get(lon_col):
                jobs.append((route,row,lat_col,lon_col,id_col,aux_col))

results=[]
errors=[]
with ThreadPoolExecutor(max_workers=5) as pool:
    futs={pool.submit(fetch_one,job):job for job in jobs}
    for done_n, fut in enumerate(as_completed(futs), 1):
        job=futs[fut]
        try:
            results.append(fut.result())
            print(f"[{done_n}/{len(futs)}] saved {results[-1]['route']}: {results[-1]['target_id']}", flush=True)
        except Exception as e:
            errors.append({"route":job[0],"target":job[1].get(job[4]),"error":str(e)})
            print(f"[{done_n}/{len(futs)}] ERROR {job[0]} {job[1].get(job[4])}: {e}", flush=True)

index = AUDIT / "naip_snapshot_index.csv"
with index.open("w",encoding="utf-8-sig",newline="") as f:
    cols=list(results[0].keys()) if results else ["route","target_id","error"]
    w=csv.DictWriter(f,fieldnames=cols); w.writeheader(); w.writerows(sorted(results,key=lambda r:(r["route"],r["target_id"])))

# Eight-site contact sheets per corridor; full-size snapshots remain alongside each sheet.
for route, *_ in sources:
    entries=[r for r in sorted(results,key=lambda r:r["target_id"]) if r["route"]==route]
    thumb_w,thumb_h=600,509
    per_sheet=8
    for page,start in enumerate(range(0,len(entries),per_sheet),1):
        chunk=entries[start:start+per_sheet]
        sheet=Image.new("RGB",(thumb_w*2,thumb_h*4),(238,241,245))
        for i,entry in enumerate(chunk):
            im=Image.open(ROOT/entry["image"]).convert("RGB").resize((thumb_w,thumb_h-30))
            x=(i%2)*thumb_w; y=(i//2)*thumb_h
            sheet.paste(im,(x,y))
            d=ImageDraw.Draw(sheet); d.text((x+8,y+thumb_h-27),entry["target_id"],fill=(16,31,48),font=SMALL)
        dst=AUDIT/route/f"naip_contact_{page:02d}.jpg"
        sheet.save(dst,quality=88,optimize=True)

summary={"snapshots_written":len(results),"expected_targets":len(jobs),"errors":errors,"index":str(index.relative_to(ROOT)).replace("\\","/")}
(AUDIT/"naip_snapshot_run_summary.json").write_text(json.dumps(summary,indent=2),encoding="utf-8")
print(json.dumps(summary,indent=2))
