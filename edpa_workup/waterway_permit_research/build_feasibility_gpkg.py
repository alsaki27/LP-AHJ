"""Create a GIS-ready route, station/parcel, and public utility screening GeoPackage."""

import csv
from pathlib import Path
import xml.etree.ElementTree as ET
import zipfile

import geopandas as gpd
from pyproj import Transformer
from shapely.geometry import LineString, Point
from shapely.ops import substring, transform


WORK = Path(__file__).resolve().parent
BASE = WORK.parent
NS = {"k": "http://www.opengis.net/kml/2.2"}


def csv_rows(path):
    with path.open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


inventory = {r["feature_id"]: r for r in csv_rows(BASE / "route_feature_inventory.csv")}
overlay = csv_rows(WORK / "ROW_feasibility_station_overlay.csv")
routes = {}
for kmz_path in (WORK / "rfp_source").glob("*.kmz"):
    with zipfile.ZipFile(kmz_path) as archive:
        kml_name = next(name for name in archive.namelist() if name.lower().endswith(".kml"))
        root = ET.fromstring(archive.read(kml_name))
        for placemark in root.findall(".//k:Placemark", NS):
            feature_id = placemark.findtext("k:name", default="", namespaces=NS)
            points = []
            for node in placemark.findall(".//k:coordinates", NS):
                for raw in (node.text or "").split():
                    lon, lat, *_ = raw.split(",")
                    points.append((float(lon), float(lat)))
            routes[feature_id] = LineString(points)
assert set(routes) == set(inventory)

route_gdf = gpd.GeoDataFrame(
    [
        {
            "feature_id": feature_id,
            "route_part": inventory[feature_id]["route_part"],
            "source_label": inventory[feature_id]["source_label"],
            "source_length_ft": float(inventory[feature_id]["length_ft_geodesic"]),
            "geometry": geometry,
        }
        for feature_id, geometry in routes.items()
    ],
    crs=4326,
)

projected_routes = {}
for feature_id, geometry in routes.items():
    crs = 3435 if feature_id.startswith("Spur") else 3734
    forward = Transformer.from_crs(4326, crs, always_xy=True).transform
    inverse = Transformer.from_crs(crs, 4326, always_xy=True).transform
    projected_routes[feature_id] = (transform(forward, geometry), inverse)

station_records = []
for index, row in enumerate(overlay, start=1):
    feature_id = row["feature_id"]
    route, inverse = projected_routes[feature_id]
    source_length = float(inventory[feature_id]["length_ft_geodesic"])
    start = max(0, min(route.length, route.length * float(row["station_start_ft_KMZ"]) / source_length))
    end = max(0, min(route.length, route.length * float(row["station_end_ft_KMZ"]) / source_length))
    geometry = substring(route, start, end)
    if not isinstance(geometry, LineString):
        geometry = LineString([route.interpolate(start), route.interpolate(end + 0.001)])
    station_records.append({
        "station_id": index,
        "feature_id": feature_id,
        "route_part": row["route_part"],
        "start_ft": float(row["station_start_ft_KMZ"]),
        "end_ft": float(row["station_end_ft_KMZ"]),
        "county": row["county_boundary"],
        "place": row["municipality_or_place_boundary"],
        "township": row["township_boundary"],
        "road_candidates": row["candidate_road_names_codes"],
        "tax_parcel_count": int(row["direct_tax_parcel_record_count"]),
        "feature_parcels_250ft": int(row["nearby_250ft_parcel_count_feature_level"]),
        "tax_parcel_ids": row["direct_tax_parcel_ids"],
        "odot_index_oids": row["odot_plan_index_oids_feature_level"],
        "dupage_row_oids": row["dupage_row_gis_oids_feature_level"],
        "dupage_row_station_oids": row["dupage_row_gis_oids_station_match"],
        "dupage_record_refs": row["dupage_record_refs_station_match"],
        "cook_row_screen_ids": row["cook_row_screen_ids_station_match"],
        "cook_row_job_numbers": row["cook_row_job_numbers_station_match"],
        "franklin_row_fids": row["franklin_auditor_row_gis_fids_station_match"],
        "franklin_row_fraction": float(row["franklin_row_mapped_fraction_approx"]),
        "franklin_record_refs": row["franklin_record_refs_station_match"],
        "utility_leads": int(row["public_utility_gis_lead_count"]),
        "utility_gis_x": int(row["public_utility_gis_intersection_count"]),
        "row_status": row["row_document_status"],
        "geometry": transform(inverse, geometry),
    })
station_gdf = gpd.GeoDataFrame(station_records, crs=4326)

utility_events = []
for source, filename, id_field in (
    ("Union County sewer", "Union_County_public_sewer_route_screen.csv", "source_asset_row"),
    ("MWRD sewer", "MWRD_public_sewer_route_screen.csv", "facility_id"),
):
    for row in csv_rows(WORK / filename):
        feature_id = row["feature_id"]
        route, inverse = projected_routes[feature_id]
        source_length = float(inventory[feature_id]["length_ft_geodesic"])
        station = float(row["route_station_ft_projected"])
        at = route.interpolate(max(0, min(route.length, route.length * station / source_length)))
        utility_events.append({
            "feature_id": feature_id,
            "source": source,
            "asset_id": str(row[id_field]),
            "station_ft": station,
            "offset_ft": float(row["minimum_offset_ft_projected"]),
            "gis_intersection": row["gis_geometry_intersection"],
            "geometry": transform(inverse, at),
        })
event_gdf = gpd.GeoDataFrame(utility_events, crs=4326)

asset_geometries = []
union_ids = {}
for row in csv_rows(WORK / "Union_County_public_sewer_route_screen.csv"):
    union_ids.setdefault(row["asset_type"], set()).add(int(row["source_asset_row"]) - 1)
for asset_type, indices in union_ids.items():
    layer = gpd.read_file(WORK / "public_utility_sources" / "union_county_sewer" / f"Utility_Sewer_{asset_type}.shp").to_crs(4326)
    for index in sorted(indices):
        asset_geometries.append({
            "source": "Union County sewer",
            "asset_id": f"{asset_type}:{index + 1}",
            "asset_type": asset_type,
            "geometry": layer.iloc[index].geometry,
        })

mwrd_rows = csv_rows(WORK / "MWRD_public_sewer_route_screen.csv")
for asset_layer, filename in (
    ("Interceptor manhole", "mwrd_interceptor_manholes_chicago_corridor.geojson"),
    ("Pump station", "mwrd_pump_stations_chicago_corridor.geojson"),
    ("Local manhole", "mwrd_local_manholes_chicago_corridor.geojson"),
    ("Interceptor", "mwrd_interceptors_chicago_corridor.geojson"),
    ("Local sewer", "mwrd_local_sewers_chicago_corridor.geojson"),
):
    mwrd_ids = {int(row["mwrd_objectid"]) for row in mwrd_rows if row["mwrd_layer"] == asset_layer}
    mwrd = gpd.read_file(WORK / "public_utility_sources" / filename)
    for _, asset in mwrd[mwrd["OBJECTID"].isin(mwrd_ids)].iterrows():
        asset_geometries.append({
            "source": "MWRD sewer",
            "asset_id": str(asset["FACILITYID"]),
            "asset_type": asset_layer,
            "geometry": asset.geometry,
        })
line_gdf = gpd.GeoDataFrame(
    [r for r in asset_geometries if r["geometry"].geom_type in ("LineString", "MultiLineString")],
    crs=4326,
)
point_gdf = gpd.GeoDataFrame(
    [r for r in asset_geometries if r["geometry"].geom_type in ("Point", "MultiPoint")],
    crs=4326,
)

franklin_rows = csv_rows(WORK / "Franklin_County_mapped_ROW_route_screen.csv")
franklin_ids = {int(row["auditor_row_fid"]) for row in franklin_rows}
franklin_source = gpd.read_file(WORK / "public_utility_sources/franklin_county_row/RIGHTOFWAY.shp")
franklin_row_gdf = franklin_source.iloc[sorted(franklin_ids)][
    ["Name", "TYPE", "RECBOOKCD", "RECBOOK", "RECPAGE", "INSTRUMENT", "OWNERNME1", "RECOFF", "geometry"]
].copy()
franklin_row_gdf["source_fid"] = sorted(franklin_ids)
franklin_row_gdf = franklin_row_gdf.to_crs(4326)

ohio_parcels = gpd.read_file(BASE / "parcel_data/ohio_route_corridor_parcels.gpkg")
ohio_parcels = ohio_parcels[[
    "county", "parcel_id", "parcel_id_secondary", "owner_name", "legal_description_or_start",
    "plat_or_instrument_reference", "route_feature_ids_within_250ft", "minimum_route_offset_ft",
    "direct_route_intersection", "direct_route_station_ranges_ft", "parcel_source_oid", "geometry",
]].to_crs(4326)
illinois_parcels = gpd.read_file(WORK / "public_utility_sources/Illinois_corridor_tax_parcels_250ft.geojson").to_crs(4326)
dupage_mapped_row = gpd.read_file(WORK / "public_utility_sources/Dupage_deeded_ROW_spur1.geojson").to_crs(4326)
cook_mapped_row = gpd.read_file(WORK / "public_utility_sources/Cook_mapped_ROW_route_polygons.geojson").to_crs(4326)

target = WORK / "ROW_and_public_utility_feasibility_overlay.gpkg"
if target.exists():
    target.unlink()
route_gdf.to_file(target, layer="source_route", driver="GPKG")
station_gdf.to_file(target, layer="station_parcel_row_screen", driver="GPKG", mode="a")
event_gdf.to_file(target, layer="public_utility_gis_leads", driver="GPKG", mode="a")
line_gdf.to_file(target, layer="public_sewer_lines", driver="GPKG", mode="a")
point_gdf.to_file(target, layer="public_sewer_structures", driver="GPKG", mode="a")
franklin_row_gdf.to_file(target, layer="franklin_mapped_row_polygons", driver="GPKG", mode="a")
ohio_parcels.to_file(target, layer="ohio_corridor_tax_parcels_250ft", driver="GPKG", mode="a")
illinois_parcels.to_file(target, layer="illinois_corridor_tax_parcels_250ft", driver="GPKG", mode="a")
dupage_mapped_row.to_file(target, layer="dupage_deeded_row_polygons", driver="GPKG", mode="a")
cook_mapped_row.to_file(target, layer="cook_mapped_row_polygons", driver="GPKG", mode="a")

print(f"Wrote {len(route_gdf)} routes, {len(station_gdf)} station bands, {len(event_gdf)} utility leads, {len(line_gdf)} public sewer lines, {len(point_gdf)} public sewer structures, {len(franklin_row_gdf)} Franklin, {len(cook_mapped_row)} Cook, {len(dupage_mapped_row)} DuPage mapped ROW polygons, {len(ohio_parcels)} Ohio parcels, and {len(illinois_parcels)} Illinois parcels to {target}")
