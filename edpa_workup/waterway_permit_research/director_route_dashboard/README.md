# Lightpath route intelligence atlas

Interactive, director-facing view of the current public-record screen for the Chicago spurs and Ohio Segments 0 and 1. It is a planning aid, not an engineered alignment or construction clearance.

## Open locally

Double-click `dist/index.html`, or run `python launch_dashboard.py` from this directory. The launcher opens the site in your default browser and serves it until you press Ctrl+C in the terminal. The background map needs an internet connection; the research layers and reports are bundled locally.

Alternatively, serve a fixed port:

```powershell
python -m http.server 8765 --directory dist
```

Open `http://localhost:8765/`. To refresh the exported layers and registers after the research workspace changes, run `python build_data.py` first. That script reads the parent `ROW_and_public_utility_feasibility_overlay.gpkg` and the CSV registers in this workspace and its parent.

## What the site contains

- 52 original route features across three route areas, with feature selection and a watchlist.
- Toggleable corridor parcels (5,061 public tax parcels), mapped ROW polygon leads (313), public utility assets (2,431), 16 water or drainage cases, and 11 geometric rail crossing points.
- Searchable, filterable, CSV-exportable reports: 1,362 AHJ station intervals, 16 water cases, 21 rail screen records, 2,935 asset-to-route utility proximity links, 183 indexed PDF scans, and 94 open record entries or groups.
- Source links where the register has an official URL. The PDF scans themselves remain in the local evidence archive; the hosted site is an index and map, not a copy of the 847 MB archive.

The geometry and report files are static exports under `dist/data/` and bundled in `dist/assets/data.js` for direct file opening. Leaflet is bundled under `dist/assets/`. The background tiles come from USGS The National Map at runtime.

## Interpretation

Parcel outlines are tax GIS, not surveyed property lines. Mapped ROW polygons and candidate PDF references are research leads. Utility features and proximity links do not establish owner consent, precise horizontal position, depth, or clearance. AHJ assignments are candidates derived from road and jurisdiction data. Water and rail records require footprint and authority confirmation. No road side or construction method has been cleared by this screen.

The site starts in Segment 0. Use the scope buttons to switch to Segment 1, the Chicago spurs, or all routes. The Layers panel controls overlays; the report tabs open the underlying registers. Clicking a report's **Focus map** button selects the matching route feature.
