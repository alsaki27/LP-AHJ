"""Extract the RFP KMZ placemarks into a traceable, one-row-per-feature inventory.

Usage: python build_route_inventory.py PATH_TO_RFP_ZIP
The output is a screening inventory; feature labels are not verified crossings.
"""

from __future__ import annotations

import csv
import hashlib
import io
import sys
import xml.etree.ElementTree as ET
import zipfile
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

from pyproj import Geod


NS = {"k": "http://www.opengis.net/kml/2.2"}
GEOD = Geod(ellps="WGS84")
OUT_DIR = Path(__file__).resolve().parent / "edpa_workup"


def coords_of(placemark: ET.Element) -> list[tuple[float, float]]:
    points = []
    for node in placemark.findall(".//k:coordinates", NS):
        for raw in (node.text or "").split():
            lon, lat, *_ = raw.split(",")
            points.append((float(lon), float(lat)))
    return points


def feet(points: list[tuple[float, float]]) -> float:
    return sum(
        GEOD.inv(*a, *b)[2] / 0.3048 for a, b in zip(points, points[1:])
    )


def main(source: Path) -> None:
    OUT_DIR.mkdir(exist_ok=True)
    rows = []
    totals: dict[str, float] = defaultdict(float)
    counts: Counter[str] = Counter()
    with zipfile.ZipFile(source) as package:
        for member in package.namelist():
            if not member.lower().endswith(".kmz"):
                continue
            group = "Chicago spurs" if "Spurs" in member else "Ohio mainline"
            with zipfile.ZipFile(io.BytesIO(package.read(member))) as kmz:
                for kml_name in kmz.namelist():
                    if not kml_name.lower().endswith(".kml"):
                        continue
                    root = ET.fromstring(kmz.read(kml_name))
                    for placemark in root.findall(".//k:Placemark", NS):
                        name = placemark.findtext("k:name", default="", namespaces=NS)
                        points = coords_of(placemark)
                        if len(points) < 2:
                            raise ValueError(f"Feature {name} has fewer than 2 vertices")
                        route_part = name.split("-")[0]
                        label = name.split("-")[-1]
                        length = feet(points)
                        counts[label] += 1
                        totals[group] += length
                        rows.append({
                            "project_part": group,
                            "source_kmz": member,
                            "source_kml": kml_name,
                            "feature_id": name,
                            "route_part": route_part,
                            "source_label": label,
                            "label_status": "Unverified source label",
                            "length_ft_geodesic": f"{length:.1f}",
                            "vertex_count": len(points),
                            "start_lon": f"{points[0][0]:.8f}",
                            "start_lat": f"{points[0][1]:.8f}",
                            "end_lon": f"{points[-1][0]:.8f}",
                            "end_lat": f"{points[-1][1]:.8f}",
                            "verified_feature_name": "",
                            "verified_owner_or_ahj": "",
                            "permit_candidate": "",
                            "evidence_reference": "",
                            "review_status": "Not reviewed",
                        })
    out = OUT_DIR / "route_feature_inventory.csv"
    with out.open("w", newline="", encoding="utf-8-sig") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    sha = hashlib.sha256(source.read_bytes()).hexdigest()
    print(f"Source SHA256: {sha}")
    print(f"Inventory: {out} ({len(rows)} features)")
    for group, length in totals.items():
        print(f"{group}: {length:.0f} ft / {length / 5280:.2f} mi")
    print(f"Labels: {dict(counts)}")
    print(f"Prepared: {date.today().isoformat()}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python build_route_inventory.py PATH_TO_RFP_ZIP")
    main(Path(sys.argv[1]))
