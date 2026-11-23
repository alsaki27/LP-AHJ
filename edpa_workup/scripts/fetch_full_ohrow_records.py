from pathlib import Path
import json
import requests
import pandas as pd

ROOT = Path(__file__).resolve().parent / "edpa_workup"
SERVICE = "https://odotgis.dot.state.oh.us/arcgis/rest/services/OhROW/ROW_Monuments_Viewer/MapServer/1/query"
idx = pd.read_csv(ROOT / "ohrow_plan_index_candidates.csv")
ids = ",".join(str(int(x)) for x in idx.plan_index_object_id)
resp = requests.get(SERVICE, params={
    "f": "json", "objectIds": ids, "outFields": "*", "returnGeometry": "true", "outSR": "4326"
}, timeout=90)
resp.raise_for_status()
data = resp.json()
(ROOT / "ohrow_plan_index_full_raw.json").write_text(json.dumps(data, indent=2), encoding="utf-8")
features = []
for f in data.get("features", []):
    a = f.get("attributes", {})
    a["OBJECTID"] = a.get("OBJECTID")
    a["geometry_json"] = json.dumps(f.get("geometry", {}), separators=(",", ":"))
    features.append(a)
full = pd.DataFrame(features).merge(idx[["plan_index_object_id", "candidate_route_features"]], left_on="OBJECTID", right_on="plan_index_object_id", how="left")
full.to_csv(ROOT / "ohrow_plan_index_full.csv", index=False)
print(f"Fetched {len(features)} complete OhROW index rows for {len(idx)} route-linked candidates.")
for key in ["PLAN_SHEETS", "ROW_REC_DOC_INFO", "ROW_MNMT_REPORT", "ADDTL_DOCS1", "PlanGUID"]:
    if key in full:
        print(key, "nonblank rows:", int(full[key].fillna("").astype(str).str.strip().ne("").sum()))
