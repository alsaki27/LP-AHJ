"""Package public-GIS screening annotations on the unchanged RFP route geometry.

Usage: python build_screening_kmz.py PATH_TO_RFP_ZIP
"""

from __future__ import annotations

import csv
import html
import sys
import xml.etree.ElementTree as ET
import zipfile
from collections import defaultdict
from pathlib import Path

from analyze_public_gis import OUT, read_route


KML = "http://www.opengis.net/kml/2.2"
ET.register_namespace("", KML)


def row_by_id(path: Path) -> dict[str, dict]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return {row["feature_id"]: row for row in csv.DictReader(handle)}


def grouped_by_id(path: Path, field: str) -> dict[str, list[dict]]:
    grouped = defaultdict(list)
    with path.open(encoding="utf-8-sig", newline="") as handle:
        for row in csv.DictReader(handle):
            grouped[row[field]].append(row)
    return grouped


def main(source: Path) -> None:
    features = read_route(source)
    gis = row_by_id(OUT / "route_gis_screen.csv")
    nwi = row_by_id(OUT / "nwi_wetland_screen.csv")
    special = grouped_by_id(OUT / "water_rail_candidates.csv", "route_feature_id")
    roads = grouped_by_id(OUT / "road_corridor_candidates.csv", "feature_id")
    root = ET.Element(f"{{{KML}}}kml")
    doc = ET.SubElement(root, f"{{{KML}}}Document")
    ET.SubElement(doc, f"{{{KML}}}name").text = "EDPA public GIS screening - NOT a permit determination"
    colors = {"Bore": "ff00ffff", "Water": "ffff0000", "HW": "ff00a5ff", "RR": "ff0000ff"}
    for label, color in colors.items():
        style = ET.SubElement(doc, f"{{{KML}}}Style", id=label)
        ls = ET.SubElement(style, f"{{{KML}}}LineStyle")
        ET.SubElement(ls, f"{{{KML}}}color").text = color
        ET.SubElement(ls, f"{{{KML}}}width").text = "5" if label != "Bore" else "3"
    folders = {}
    for f in features:
        fid = f["id"]
        label = fid.split("-")[-1]
        group_name = "Chicago spurs" if f["state"] == "il" else "Ohio mainline"
        if group_name not in folders:
            folders[group_name] = ET.SubElement(doc, f"{{{KML}}}Folder")
            ET.SubElement(folders[group_name], f"{{{KML}}}name").text = group_name
        pm = ET.SubElement(folders[group_name], f"{{{KML}}}Placemark")
        ET.SubElement(pm, f"{{{KML}}}name").text = fid
        ET.SubElement(pm, f"{{{KML}}}styleUrl").text = f"#{label}"
        screen = gis[fid]
        nwi_row = nwi[fid]
        leading_roads = sorted(roads.get(fid, []), key=lambda x: -float(x["total_road_length_within_30m_buffer_m"]))[:5]
        nearby = [x for x in special.get(fid, []) if x["gis_object_id"]]
        lines = [
            "PUBLIC GIS SCREENING ONLY - legal ROW, identity and permit authority require records/agency review",
            f"County candidates: {screen['county_candidates'] or 'None in layer'}",
            f"Place candidates: {screen['place_candidates'] or 'None in layer'}",
            f"Township candidates: {screen['township_candidates'] or 'None in layer'}",
            f"NWI aquatic polygon intersections: {nwi_row['nwi_intersecting_polygon_count']} ({nwi_row['nwi_types']})",
        ]
        if leading_roads:
            lines.append("Road candidates: " + "; ".join(
                f"{r['road_name']} {r['route_type']} {r['route_number']} [{r['jurisdiction_code']}]"
                for r in leading_roads
            ))
        if nearby:
            lines.append("Water/rail candidates: " + "; ".join(
                f"{r['candidate_name'] or r['rail_owner_code_1'] or 'Unnamed'} ({r['minimum_centerline_distance_m']} m)"
                for r in nearby
            ))
        ET.SubElement(pm, f"{{{KML}}}description").text = "\n".join(lines)
        line = ET.SubElement(pm, f"{{{KML}}}LineString")
        ET.SubElement(line, f"{{{KML}}}tessellate").text = "1"
        ET.SubElement(line, f"{{{KML}}}coordinates").text = " ".join(f"{lon},{lat},0" for lon, lat in f["points"])
    target = OUT / "EDPA_Public_GIS_Screening.kmz"
    with zipfile.ZipFile(target, "w", compression=zipfile.ZIP_DEFLATED) as kmz:
        kmz.writestr("doc.kml", ET.tostring(root, encoding="utf-8", xml_declaration=True))
    print(target, len(features), "route features")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python build_screening_kmz.py PATH_TO_RFP_ZIP")
    main(Path(sys.argv[1]))
