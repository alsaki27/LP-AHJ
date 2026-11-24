# Host the Director Brief and engineering map

The atlas is a static site. It uses the Leaflet library already bundled in `docs/assets/`, and its crossing records, proof images and report data load from relative paths. GitHub Pages can serve it directly from `docs/`.

## 1. Publish the director view

1. In [LP-AHJ Pages settings](https://github.com/alsaki27/LP-AHJ/settings/pages), select **Deploy from a branch**. Set the branch to **main** and the folder to **/docs**. Save.
2. After the Pages deployment succeeds, open the project URL at [alsaki27.github.io/LP-AHJ/](https://alsaki27.github.io/LP-AHJ/). This opens the Director Brief. Share that address as the entry point for review.

The committed `docs/.nojekyll` serves the static files as supplied. The Pages deploy contains only the atlas directory. The full research archive is available separately in the [GitHub repository](https://github.com/alsaki27/LP-AHJ/tree/main/edpa_workup/atlas_audit). GitHub Pages on this repository is public. [GitHub Pages publishing sources](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site) · [GitHub Pages visibility](https://docs.github.com/en/enterprise-cloud@latest/pages/getting-started-with-github-pages/changing-the-visibility-of-your-github-pages-site)

## 2. Add two basemaps

| Layer | Implementation |
| --- | --- |
| **Streets** (default) | In the hosted configuration, use an OpenStreetMap-derived raster tile layer. For a small interactive pilot, the standard tile endpoint is `https://tile.openstreetmap.org/{z}/{x}/{y}.png`. Display linked © OpenStreetMap contributors attribution in the Leaflet map. Preserve the browser referrer and caching, and request tiles for the visible map only. The public endpoint is best-effort. For a dependable partner demo or sustained use, choose a hosted provider with suitable terms and quota, or host your own tiles. [OSM tile policy](https://operations.osmfoundation.org/policies/tiles/) |
| **Aerial** (optional) | Add USGS National Map Imagery Only using `https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}`. Use the ArcGIS level/row/column order and the service's published native zoom limit. Show source attribution and keep the indexed NAIP proof crops in each crossing record. [USGS tile service](https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer) |
| **No basemap** | Keep the vector view available so decision links and case records still work with a slow network or an unavailable tile provider. Preserve local tile support for the offline ZIP. |

Use a Leaflet base-layer switcher in `docs/map.html` so **Streets**, **Aerial** and **No basemap** are mutually exclusive. Define each source and its attribution in `docs/assets/config.js` and retain the existing route, parcel and crossing overlays above the selected background. For a commercial tile provider, use an origin-restricted browser key and an appropriate tier for the use case. [Leaflet layer control](https://leafletjs.com/reference.html#control-layers) · [Example provider origin controls](https://docs.maptiler.com/cloud/admin-api/reference/)

## 3. Verify the director experience

- From a browser outside your GitHub account, open the hosted Director Brief and follow each priority decision to its crossing card, zoomed map and proof.
- Switch between streets, aerials and no basemap at a Chicago crossing and both Ohio segments. Verify the route and markers stay visible and tile attribution remains readable on a narrow screen.
- Open a direct link such as `map.html#water=S1-W08`, then test CSV downloads, proof images and the one-page US Letter printout.

For a staff-only version, deploy the same static folder to a company-controlled host such as Azure Static Web Apps with tenant-restricted Microsoft Entra sign-in. Apply access controls to the whole site, including its JS data, CSV and image files. Keep any internal-only data in a private source repository or storage location. [Azure Static Web Apps route protection](https://learn.microsoft.com/en-us/azure/static-web-apps/configuration#secure-routes-with-roles)
