# Host the Director Brief and engineering map

The atlas serves static pages and assets behind a Vercel browser login. The Director Brief is at [lp-ahj.vercel.app](https://lp-ahj.vercel.app/).

## 1. Publish the director view

1. In the Vercel project, use **docs** as the Root Directory, turn off access to source files outside that directory, and use **main** as the production branch. Pushes to `main` build the atlas and update the production URL. [Vercel build settings](https://vercel.com/docs/builds/configure-a-build) · [Vercel for GitHub](https://vercel.com/docs/git/vercel-for-github)
2. The build copies atlas pages and supported assets into `docs/dist/`. The original route KMZs, RFP PDF, build files and development dependencies are outside the deployed static assets.
3. The server requires the `director` login for every request, including direct CSV, image and map links. The password is shared privately. The Vercel production secret `DIRECTOR_AUTH_SHA256` stores the lowercase SHA-256 hash of the Base64 encoding of `director:<password>`. Each new password requires an updated secret and a production deployment. [Vercel Routing Middleware](https://vercel.com/docs/routing-middleware)

The hosted login covers the Vercel site. The full research archive is in the public [GitHub repository](https://github.com/alsaki27/LP-AHJ/tree/main/edpa_workup/atlas_audit).

## 2. Switch basemaps

| Layer | Implementation |
| --- | --- |
| **Streets (OpenStreetMap)** | Default over HTTPS. Loads raster tiles with linked contributor attribution, browser referrer and normal browser caching. The public OSM endpoint is a best-effort service for interactive use. [OSM tile policy](https://operations.osmfoundation.org/policies/tiles/) |
| **Aerial (USGS)** | Uses The National Map Imagery Only. Above zoom 16, the map scales the native imagery. The separately indexed NAIP proof crops remain available in the atlas. [USGS tile service](https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer) |
| **No basemap** | Keeps the vector layers, crossing markers and cards available during a tile outage. Offline copies start here and can use local aerial or street tiles. |

Use the basemap control at the upper right of the engineering map. The route, parcel and crossing overlays stay in place as the background changes. Tile sources and attribution are configured in `docs/assets/config.js`.

## 3. Verify the director experience

- In a private browser window, check that the Director Brief and direct file links prompt for a login. Sign in and follow each priority decision to its crossing card, zoomed map and proof.
- Switch between streets, aerials and no basemap at a Chicago crossing and both Ohio segments. Verify the route and markers stay visible and tile attribution remains readable on a narrow screen.
- Open a direct link such as `map.html#water=S1-W08`, then test CSV downloads, proof images and the one-page US Letter printout.
