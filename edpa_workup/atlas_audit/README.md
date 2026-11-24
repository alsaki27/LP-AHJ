# Atlas audit and water crossing research

[Director Brief](../../docs/index.html) · [Research process and proof](../../docs/research.html) · [Hosting plan](HOSTING.md)

The November 24, 2026 audit reproduced **11 rail intersections** and identified **36 mapped water points** across the Chicago spurs, Segment 0 and Segment 1. These counts refer to intersections with mapped features. Permit applicability depends on the crossing method and work limits.

| Research | Overall | Chicago spurs | Segment 0 | Segment 1 |
| --- | --- | --- | --- | --- |
| Original atlas audit | [Findings](atlas_audit_review.md) | [Audit](atlas_audit_chicago.md) | [Audit](atlas_audit_segment0.md) | [Audit](atlas_audit_segment1.md) |
| Water crossing follow-up | [Permitting playbook](water_crossing_deep_dive.md) | [Crossings](water_crossings_chicago.md) | [Crossings](water_crossings_segment0.md) | [Crossings](water_crossings_segment1.md) |

- [GIS intersection register](atlas_audit_gis_intersections.csv) records source feature IDs, coordinates and stations.
- [Water point evidence](water_crossing_point_evidence.csv) records nearby structures, parcel hits, local crossing angles, point flood mapping and nearby wetlands.
- [GIS source extracts](source_extracts/) hold the rail and flowline corridor queries, focused feature queries, and saved structure, flood and wetland lookup results.
- [Right-of-way and utility evidence](../waterway_permit_research/) and the [aerial review index](../imagery_audit/) supply the supporting record.

The atlas audit reports evaluate the earlier app. The current [water register](../../docs/water.html) incorporates the water findings. The audit reports remain the reference for outstanding checks on baseline road, rail, construction and jurisdiction data.

## Reproduce the calculations

Run the scripts with Python, Shapely 2 and pyproj. Point `LP_AHJ_ROUTE_INPUT_DIR` at your local copy of the three original route KMZs. The scripts use the saved GIS extracts, exported atlas data and the repository's corridor parcel, structure and boundary data. They do not access live services.

From the repo root, run these commands in order to regenerate the two audit CSVs.

```powershell
$env:LP_AHJ_ROUTE_INPUT_DIR = 'C:\path\to\your\RFP\route\inputs'
python edpa_workup/atlas_audit/scripts/export_intersections.py
python edpa_workup/atlas_audit/scripts/water_deep_evidence.py
```

When updating the atlas, review any changes to both CSVs, copy the reviewed tables into `docs/data/`, and run `python docs/build_water_register.py` to rebuild the offline crossing data. `water_decisions.txt` carries the reviewed engineering and permitting decisions keyed by the crossing locations.
