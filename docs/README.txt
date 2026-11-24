LP AHJ & permitting-risk atlas

HOW TO LAUNCH
1. Unzip the folder anywhere (keep the folder contents together).
2. Double-click index.html (or right-click > Open with > Chrome or Edge).
   index.html opens Director Brief. The four priority decisions link to their crossing cards,
   map points and proof. Select “Print one-page brief” to print on US Letter or save to PDF.
   Other pages: map.html (engineering map), water.html (crossing register), report.html
   (jurisdiction report), construction.html (project risks), jdx.html (requirements and contacts)
   and research.html (research process, downloads and decision evidence).
3. When served over HTTPS, the engineering map opens with OpenStreetMap Streets. Use the
   map's basemap switcher for USGS Aerial or No basemap. Local copies start with No basemap.
   To add local imagery, place tiles in tiles/{z}/{x}/{y}.jpg (zoom 8–18) and select Local aerial tiles.
   See tiles/README.txt and assets/config.js.
If a browser blocks anything when opened from a file, run from the folder:  python -m http.server 8000  and open http://localhost:8000

DATA
data/data.js = all layers, risks, reroutes, permits and contacts (built by build_data.py from the AHJ baseline workbook,
parcel/ROW analysis, reroute study and the LP-AHJ GitHub register). img/ = NAIP review crops and reroute maps.
Screening only: not a permit determination or an engineered alignment. Reroute lines are conceptual.
Proof pages and their bundled data and imagery work offline. External source links need internet.

WATER CROSSING UPDATE — NOVEMBER 24, 2026
The Water crossings page and map layer share the same 36 reviewed GIS points.
Filter by segment or search by name, source ID, structure, station or authority.
Each point has its own blocker, approver, submission list, fallback and source evidence.
Regenerate the offline water layer with python build_water_register.py after changing
data/water_decisions.txt or data/water_crossing_point_evidence.csv.
