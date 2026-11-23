"""Build an annotated KMZ for Segment 1 from the original route and screening ledgers.

Geometry is not altered. Authority and assessor parcel layers are indicative GIS
screens only; they are not title, legal ROW, access rights, or permit determinations.
"""
from __future__ import annotations

import csv
import json
import zipfile
import xml.etree.ElementTree as ET
from collections import defaultdict
from pathlib import Path

from pyproj import Transformer
from shapely.geometry import LineString, Point, shape
from shapely.ops import substring, transform

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source_files" / "MT - CMH - v4.0 - Segment1.kmz"
OUT = ROOT / "segment1_vendor_screening_exhibit.kmz"
KML = "http://www.opengis.net/kml/2.2"
ET.register_namespace("", KML)
NS = {"k": KML}
TO_LOCAL = Transformer.from_crs(4326, 3734, always_xy=True).transform
TO_WGS = Transformer.from_crs(3734, 4326, always_xy=True).transform


def rows(path: Path):
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def elem(parent, name, text=None, **attrs):
    e = ET.SubElement(parent, f"{{{KML}}}{name}", attrs)
    if text is not None:
        e.text = str(text)
    return e


def add_style(doc, sid, color, width="3", fill=None):
    style = elem(doc, "Style", id=sid)
    ls = elem(style, "LineStyle")
    elem(ls, "color", color)
    elem(ls, "width", width)
    if fill:
        ps = elem(style, "PolyStyle")
        elem(ps, "color", fill)
        elem(ps, "fill", "0")
        elem(ps, "outline", "1")


def add_line(pm, line, style_url, *, local=False):
    elem(pm, "styleUrl", style_url)
    ls = elem(pm, "LineString")
    elem(ls, "tessellate", "1")
    coords = list(line.coords)
    if local:
        coords = [TO_WGS(x, y) for x, y in coords]
    elem(ls, "coordinates", " ".join(f"{x:.8f},{y:.8f},0" for x, y in coords))


def add_point(pm, point, *, local=True):
    if local:
        point = transform(TO_WGS, point)
    elem(elem(pm, "Point"), "coordinates", f"{point.x:.8f},{point.y:.8f},0")


def line_part(line, start, end):
    if end <= start:
        return None
    part = substring(line, max(0, start), min(line.length, end))
    return part if part.geom_type == "LineString" and part.length > 0.05 else None


def main():
    # Retain exact input coordinate sequences and feature IDs from the source KMZ.
    source_features = []
    with zipfile.ZipFile(SOURCE) as z:
        kml_name = next(n for n in z.namelist() if n.lower().endswith(".kml"))
        root_in = ET.fromstring(z.read(kml_name))
    for pm_in in root_in.findall(".//k:Placemark", NS):
        fid = pm_in.findtext("k:name", default="", namespaces=NS)
        if not fid.startswith("S1-"):
            continue
        text = pm_in.findtext(".//k:coordinates", default="", namespaces=NS)
        coords = [tuple(map(float, c.split(",")[:2])) for c in text.split()]
        if len(coords) < 2:
            continue
        source_features.append({"id": fid, "coords": coords, "coordinate_text": " ".join(text.split()),
                                "line": transform(TO_LOCAL, LineString(coords))})
    source_features.sort(key=lambda f: int(f["id"].split("-")[1][1:]))
    by_id = {f["id"]: f for f in source_features}

    root = ET.Element(f"{{{KML}}}kml")
    doc = elem(root, "Document")
    elem(doc, "name", "Segment 1 Vendor Screening Exhibit — unchanged customer alignment")
    elem(doc, "description", (
        "Segment 1 public-record/GIS screening exhibit. Customer route geometry is copied unchanged. "
        "Station annotations reference distance in feet from each KMZ feature's first vertex. "
        "Authority overlays show administrative boundaries only; they do not establish road ownership, "
        "legal ROW, easements, title, access rights, or permit issuer. Parcel polygons are assessor tax "
        "parcel geometries, not road ROW limits or authorization to enter. Water, rail, highway and bridge "
        "markers are desktop screening candidates pending records, survey, and owner confirmation."
    ))
    for sid, color, width in [
        ("route_bore", "ff00ffff", "3"), ("route_water", "ffff0000", "5"),
        ("route_hw", "ff00a5ff", "5"), ("route_rr", "ff0000ff", "5"),
        ("county", "ff8000ff", "7"), ("place", "ff00a5ff", "7"),
        ("township", "ff00a000", "4"), ("highway", "ff0080ff", "8"),
        ("parcel", "ff555555", "1"), ("row_generic", "ff00a5ff", "3"),
    ]:
        add_style(doc, sid, color, width)
    for sid, color in [("water_pt", "ff0000ff"), ("rail_pt", "ff0000ff"),
                       ("highway_pt", "ff00a5ff"), ("authority_pt", "ff8000ff")]:
        st = elem(doc, "Style", id=sid)
        icon = elem(st, "IconStyle")
        elem(icon, "color", color)
        elem(icon, "scale", "1.05")
        icon_obj = elem(icon, "Icon")
        elem(icon_obj, "href", "http://maps.google.com/mapfiles/kml/paddle/wht-circle.png")
        elem(elem(st, "LabelStyle"), "scale", "0.85")

    folders = {}
    def folder(name):
        if name not in folders:
            folders[name] = elem(doc, "Folder")
            elem(folders[name], "name", name)
        return folders[name]

    # Original feature lines are kept separately for a clean on/off switch.
    for f in source_features:
        fid = f["id"]
        typ = fid.rsplit("-", 1)[-1].lower()
        pm = elem(folder("01 — Original RFP route (unchanged)"), "Placemark")
        elem(pm, "name", fid)
        elem(pm, "description", f"Original source KMZ feature; copied coordinate sequence unchanged. Source label: {typ.upper()} (unverified).")
        elem(pm, "styleUrl", f"#route_{typ}")
        ls = elem(pm, "LineString")
        elem(ls, "tessellate", "1")
        elem(ls, "coordinates", f["coordinate_text"])

    # Administrative boundary intervals are drawn directly on the route chainage.
    boundary_rows = rows(ROOT / "segment1_ahj_station_intervals.csv")
    for r in boundary_rows:
        fid = r["feature_id"]
        if fid not in by_id:
            continue
        start, end = float(r["feature_station_start_ft"]), float(r["feature_station_end_ft"])
        part = line_part(by_id[fid]["line"], start, end)
        if part is None:
            continue
        kind = r["boundary_type"]
        pm = elem(folder("02 — County, city, township boundary overlays (not road jurisdiction)"), "Placemark")
        elem(pm, "name", f"{r['boundary_name']} — {fid} {start:,.0f}–{end:,.0f} ft")
        elem(pm, "description", f"{kind.title()} boundary polygon overlay. Station is from KMZ feature start. {r['evidence_status']}. Source: {r['source_url']}")
        add_line(pm, part, f"#{kind}", local=True)

    # ODOT state-route candidates; these are 30 m inventory-screen intervals, not ROW limits.
    highway_candidates = [r for r in rows(ROOT / "segment1_road_station_candidates.csv")
                          if r["odot_route_type"] in {"US", "SR"} and r["feature_id"] in by_id]
    for r in highway_candidates:
        start, end = float(r["feature_station_start_ft"]), float(r["feature_station_end_ft"])
        part = line_part(by_id[r["feature_id"]]["line"], start, end)
        if part is None:
            continue
        route_name = r["road_label_candidate"]
        pm = elem(folder("03 — State-route gates (ODOT inventory proximity; not ROW)"), "Placemark")
        elem(pm, "name", f"{route_name} — {r['feature_id']} {start:,.0f}–{end:,.0f} ft")
        elem(pm, "description", f"ODOT road inventory candidate, district {r['odot_district'] or 'unknown'}, access code {r['access_control_code_raw'] or 'not populated'}, minimum route-to-road offset {r['route_to_road_min_distance_m']} m. {r['evidence_status']}. Source: {r['source_url']}")
        add_line(pm, part, "#highway", local=True)

    # Water marker at exact hydro intersections; unresolved labels get a feature midpoint marker.
    waters = rows(ROOT / "segment1_water_crossings_station.csv")
    for r in waters:
        fid = r["feature_id"]
        if fid not in by_id:
            continue
        line = by_id[fid]["line"]
        exact = r["exact_centerline_intersection"] == "Y" and r["intersection_stations_ft_from_KMZ_start"]
        station = float(r["intersection_stations_ft_from_KMZ_start"]) if exact else line.length / 2
        point = line.interpolate(station)
        label = r["water_feature_name"].strip() or "Unresolved water label"
        pm = elem(folder("04 — Water and drainage screening gates"), "Placemark")
        elem(pm, "name", f"{'Water candidate' if exact else 'Unresolved label'} — {fid} Sta {station:,.1f} ft")
        elem(pm, "description", f"Feature: {fid}; station {station:,.1f} ft from feature start. Hydro candidate: {label}. Exact centerline match: {r['exact_centerline_intersection'] or 'N'}. Angle: {r['acute_intersection_angle_deg'] or 'n/a'} degrees. Concept/evidence: {r['evidence_status']}. Source: {r['source_url']}")
        elem(pm, "styleUrl", "#water_pt")
        add_point(pm, point)

    # Exact track intersections from route/rail geometry register.
    for r in rows(ROOT / "route_rail_intersections_all_features.csv"):
        fid = r["feature_id"]
        if not fid.startswith("S1-") or r["exact_geometry_intersection"] != "Y" or fid not in by_id:
            continue
        station_text = r.get("feature_station_ft_from_KMZ_start", "")
        if not station_text:
            continue
        station = float(station_text)
        point = by_id[fid]["line"].interpolate(station)
        pm = elem(folder("05 — Rail crossing gates (operator/ownership to confirm)"), "Placemark")
        elem(pm, "name", f"CSXT track intersection candidate — {fid} Sta {station:.1f} ft")
        elem(pm, "description", f"Track: {r['subdivision']} / {r['branch']}; rail GIS reports {r['reported_owner_or_operator_codes']}. Parcel/title records do not establish the fee owner or agreement signer. Exact route-track geometry intersection is a screening result. Confirm valuation map, title/lease, permit and signatory with CSX. Source: {r['source_url']}")
        elem(pm, "styleUrl", "#rail_pt")
        add_point(pm, point)

    # Direct assessor parcel polygons only; owner names and site addresses intentionally omitted.
    gpath = ROOT / "parcel_data" / "ohio_route_corridor_parcels.geojson"
    geo = json.loads(gpath.read_text(encoding="utf-8"))
    parcel_geometries = []
    for feat in geo["features"]:
        p = feat.get("properties", {})
        if (p.get("direct_route_intersection") != "Y" or
                not any(fid.startswith("S1-") for fid in str(p.get("direct_intersection_feature_ids", "")).replace("|", ";").split(";"))):
            continue
        county = str(p.get("county", ""))
        raw_id = str(p.get("parcel_id", ""))
        secondary = str(p.get("parcel_id_secondary", ""))
        # Delaware stores SUBPARCEL/MAPSHEET separately; Union uses GISNO/CAMANO.
        parcel_key = f"{secondary}-{raw_id}" if secondary else raw_id
        feature_ids = sorted(x for x in str(p.get("direct_intersection_feature_ids", "")).replace("|", ";").split(";") if x)
        parcel_geometries.append({"county": county, "parcel_key": parcel_key,
                                  "geometry": shape(feat["geometry"]), "props": p,
                                  "feature_ids": feature_ids, "secondary": secondary})
    public_ids = {
        ("Delaware", "500310-0"), ("Delaware", "600240-0"), ("Delaware", "319240-0"),
        ("Delaware", "319240-2"), ("Delaware", "319240-3"), ("Delaware", "319132-4"),
        ("Delaware", "319132-1"), ("Delaware", "319133-0"),
        ("Union", "1020000012001-2900210030090"),
        ("Union", "1020100900000-2900022300010"),
    }
    for info in parcel_geometries:
        county, pid, p = info["county"], info["parcel_key"], info["props"]
        g = info["geometry"]
        if g.is_empty:
            continue
        pm = elem(folder("06 — Direct assessor source geometries (screening only; not legal ROW)"), "Placemark")
        is_generic_row = pid == "999999-0"
        source_oid = p.get("parcel_source_oid") or "not provided by source layer"
        elem(pm, "name", f"{county} {'generic ROW/map placeholder' if is_generic_row else 'assessor parcel'} {pid} — source {source_oid}")
        public_label = " Public/entity ownership candidate in assessor record; title remains unverified." if (county, pid) in public_ids else " Individual owner details intentionally omitted from this exhibit."
        if is_generic_row:
            public_label = " Generic/unmatched assessor map key, not a uniquely identified fee parcel; excluded from take/fee counts. It may represent public-road/ROW mapping, but does not establish legal ROW width or title."
        elem(pm, "description", f"Direct assessor geometry source row. County: {county}; parcel/map key: {pid}; source OID/GIS record: {source_oid}; raw secondary key: {info['secondary'] or 'n/a'}; direct route feature IDs: {', '.join(info['feature_ids']) or 'see parcel register'}; station details are in the source parcel register.{public_label} Polygon intersection does not define the legal road ROW, prove fee title or grant access. Duplicate map keys may refer to different source geometries/OIDs; resolve using source record and deed/ROW plans.")
        polygons = list(g.geoms) if g.geom_type == "MultiPolygon" else [g]
        for polygon in polygons:
            poly = elem(pm, "Polygon")
            elem(poly, "tessellate", "1")
            outer = elem(elem(poly, "outerBoundaryIs"), "LinearRing")
            # Parcel GeoJSON is WGS84; output coordinates directly without reprojection.
            ring = list(polygon.exterior.coords)
            elem(outer, "coordinates", " ".join(f"{x:.8f},{y:.8f},0" for x, y in ring))
        elem(pm, "styleUrl", "#row_generic" if is_generic_row else "#parcel")

    # Explicit ODOT District 6 note is a review lead, not a facility permit determination.
    pm = elem(folder("07 — Authority notes"), "Placemark")
    elem(pm, "name", "ODOT District 6 screening — Segment 1")
    elem(pm, "description", "ODOT state-route inventory candidates along Segment 1 are shown in folder 03. District overlay is not a ROW ownership or permit determination. The US33/US36/ramp crossing at S1-S043 is a P0 gate; seek written ODOT/City/structure-owner determination because corporate-limit and access-control boundaries may affect which office issues the permit. Current road owner, ROW lines, access control, structures and permittee must be verified from plans and written issuer confirmation.")
    elem(pm, "styleUrl", "#authority_pt")
    add_point(pm, by_id["S1-S043-HW"]["line"].interpolate(by_id["S1-S043-HW"]["line"].length / 2))

    with zipfile.ZipFile(OUT, "w", compression=zipfile.ZIP_DEFLATED) as kmz:
        kmz.writestr("doc.kml", ET.tostring(root, encoding="utf-8", xml_declaration=True))
    tax_count = sum(1 for p in parcel_geometries if p["parcel_key"] != "999999-0")
    generic_count = sum(1 for p in parcel_geometries if p["parcel_key"] == "999999-0")
    print(f"Created {OUT} with {len(source_features)} source route features, {len(boundary_rows)} boundary records, {len(highway_candidates)} state-route candidates, {len(waters)} water labels, {tax_count} tax-key source geometries and {generic_count} generic 999999-0 geometries")


if __name__ == "__main__":
    main()
