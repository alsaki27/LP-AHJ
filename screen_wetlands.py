"""Intersect every RFP route feature with FWS National Wetlands Inventory polygons.

NWI is a screening layer and does not establish regulatory jurisdiction.
Usage: python screen_wetlands.py PATH_TO_RFP_ZIP
"""

from __future__ import annotations

import csv
import json
import sys
import time
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import requests

from analyze_public_gis import OUT, read_route


URL = "https://fwspublicservices.wim.usgs.gov/wetlandsmapservice/rest/services/Wetlands/MapServer/0"


def query(feature: dict) -> list[dict]:
    data = {
        "f": "json",
        "where": "1=1",
        "geometry": json.dumps({"paths": [feature["points"]], "spatialReference": {"wkid": 4326}}),
        "geometryType": "esriGeometryPolyline",
        "inSR": 4326,
        "spatialRel": "esriSpatialRelIntersects",
        "outFields": "OBJECTID,WETLAND_TYPE,ATTRIBUTE",
        "returnGeometry": "false",
    }
    for attempt in range(3):
        try:
            response = requests.post(URL + "/query", data=data, timeout=25)
            response.raise_for_status()
            body = response.json()
            if body.get("error"):
                raise RuntimeError(str(body["error"]))
            if body.get("exceededTransferLimit"):
                raise RuntimeError("Transfer limit exceeded")
            return body.get("features", [])
        except (requests.RequestException, RuntimeError, ValueError):
            if attempt == 2:
                raise
            time.sleep(attempt + 1)
    raise AssertionError("Unreachable")


def main(source: Path) -> None:
    features = read_route(source)
    rows = []
    with ThreadPoolExecutor(max_workers=5) as pool:
        futures = {pool.submit(query, f): f for f in features}
        for fut in as_completed(futures):
            f = futures[fut]
            try:
                matches = fut.result()
                counts = Counter(str(x["attributes"].get("WETLAND_TYPE") or "Unspecified") for x in matches)
                rows.append({
                    "feature_id": f["id"],
                    "state": f["state"].upper(),
                    "nwi_intersecting_polygon_count": len(matches),
                    "nwi_types": "; ".join(f"{k} ({v})" for k, v in sorted(counts.items())),
                    "source_url": URL,
                    "status": "NWI screening only; no regulatory determination",
                })
            except Exception as exc:
                rows.append({
                    "feature_id": f["id"], "state": f["state"].upper(),
                    "nwi_intersecting_polygon_count": "", "nwi_types": "",
                    "source_url": URL, "status": f"Query failed: {exc}",
                })
    rows.sort(key=lambda x: x["feature_id"])
    target = OUT / "nwi_wetland_screen.csv"
    with target.open("w", newline="", encoding="utf-8-sig") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print(f"{target}: {len(rows)} rows; {sum(int(x['nwi_intersecting_polygon_count'] or 0)>0 for x in rows)} features intersect NWI polygons")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python screen_wetlands.py PATH_TO_RFP_ZIP")
    main(Path(sys.argv[1]))
