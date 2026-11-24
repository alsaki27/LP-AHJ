# Host the Director Brief and engineering map

The atlas is a static site. Its packaged Leaflet library, crossing records, proof images and report data load from relative paths. Deploy the `docs/` directory to Vercel.

## 1. Publish the director view

1. In a Vercel Pro or Enterprise team, [import LP-AHJ](https://vercel.com/new). Select **docs** as the Root Directory and **Other** as the framework. The committed `docs/vercel.json` skips install and build and serves the folder as supplied. Use `main` as the production branch if deploying from GitHub. [Vercel build settings](https://vercel.com/docs/builds/configure-a-build) · [Vercel commercial-use terms](https://vercel.com/docs/limits/fair-use-guidelines)
2. After deployment succeeds, open the production project URL. The Director Brief loads at `/`. For a director-only hosted URL, use **Vercel Authentication** with **All Deployments** and grant the director access to the project. The source repo is public. [Vercel deployment protection](https://vercel.com/docs/deployment-protection)

The deployment serves the atlas directory. The full research archive is available separately in the [GitHub repository](https://github.com/alsaki27/LP-AHJ/tree/main/edpa_workup/atlas_audit).

## 2. Switch basemaps

| Layer | Implementation |
| --- | --- |
| **Streets (OpenStreetMap)** | Default over HTTPS. Loads raster tiles with linked contributor attribution, browser referrer and normal browser caching. The public OSM endpoint is a best-effort service for interactive use. [OSM tile policy](https://operations.osmfoundation.org/policies/tiles/) |
| **Aerial (USGS)** | Uses The National Map Imagery Only. Above zoom 16, the map scales the native imagery. The separately indexed NAIP proof crops remain available in the atlas. [USGS tile service](https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer) |
| **No basemap** | Keeps the vector layers, crossing markers and cards available during a tile outage. Offline copies start here and can use local aerial or street tiles. |

Use the basemap control at the upper right of the engineering map. The route, parcel and crossing overlays stay in place as the background changes. Tile sources and attribution are configured in `docs/assets/config.js`.

## 3. Verify the director experience

- From a browser outside your GitHub account, open the hosted Director Brief and follow each priority decision to its crossing card, zoomed map and proof.
- Switch between streets, aerials and no basemap at a Chicago crossing and both Ohio segments. Verify the route and markers stay visible and tile attribution remains readable on a narrow screen.
- Open a direct link such as `map.html#water=S1-W08`, then test CSV downloads, proof images and the one-page US Letter printout.
