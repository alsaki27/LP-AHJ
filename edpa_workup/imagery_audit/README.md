# Route Imagery Audit

## Purpose

This folder holds an image-led screening pass across all three route groups: Segment 0, Segment 1, and the Chicago spurs. It covers 85 target locations derived from route features, crossing candidates, and the full-route sampling itinerary. Each individual crop is centered on a target coordinate and shows an approximately 900 m by 650 m window; it is a reconnaissance view, not a survey exhibit.

## Find the imagery

- `naip_snapshot_index.csv` maps each target to its image, route feature, coordinates, Google Maps satellite link for live reference, and limitations.
- `segment0/naip_contact_*.jpg`, `segment1/naip_contact_*.jpg`, and `chicago_spurs/naip_contact_*.jpg` provide quick overview sheets. Full-resolution views are in each route's `naip_snapshots/` folder.
- `all_routes_visual_audit.md` gives the director-facing all-route findings and action register.
- The route subfolders contain pre-imagery target registers, row-by-row findings CSVs, and route-specific visual review reports.
- `build_naip_snapshot_atlas.py` records how the snapshots and contact sheets were assembled.

## Coverage and review outcome

The atlas contains 85 crop targets: 30 for Segment 0, 41 for Segment 1, and 14 for the Chicago spurs. Every supplied Segment 0 source feature has at least one crop; longer features have supplemental samples. Crops are discrete windows, not a continuous route mosaic, and no cable centerline is drawn over the images. Reviewers found no new, confirmed major rail or water crossing. The reports identify unresolved rail geometry, additional ODOT structure/ditch candidates, bridge and drainage interfaces, and field/records checks; imagery does not establish jurisdiction, title, utility rights, track count, or permit requirements.

## Imagery source and licensing

The downloadable snapshots use the public USGS/USDA Farm Service Agency National Agriculture Imagery Program (NAIP) image service, not copied Google Earth/Maps images. The service describes its imagery as high-resolution NAIP orthoimagery and provides service attribution as “USGS, USDA, The National Map: Orthoimagery”; USDA states that NAIP imagery is public domain and may be reproduced with credit. Sources: [USGS NAIP ImageServer](https://imagery.nationalmap.gov/arcgis/rest/services/USGSNAIPImagery/ImageServer), [USDA FSA NAIP rights notice](https://www.fsa.usda.gov/Internet/FSA_Notice/ap_26.pdf).

Google Maps satellite links are included only as live, user-opened references. Google’s current [Geo usage guidance](https://about.google/brand-resource-center/products-and-services/geo-guidelines/) bars Google Earth imagery from commercial/promotional web use, so no Google imagery screenshots are stored here or published in this public repository.

The service's copyright metadata displayed a January 9, 2025 date during retrieval; that is the service metadata date, not a confirmed per-image acquisition date. Acquisition dates can vary across the mosaic and remain unresolved in this index.

## Interpretation limits

Aerial imagery can reveal visible bridges, channels, ponds, track geometry, access, road context, and staging constraints. Tree cover, shadows, small culverts, buried utilities, current construction, ownership, legal right-of-way, railroad operator, water jurisdiction, and permit requirements cannot be established from these images. Where a candidate lies near but not on the mapped route, treat the image as a prompt to resolve alignment/offset against survey and current agency records. Each red crosshair is the source register's target coordinate, not a surveyed crossing point.

Use the route registers, cited source documents, and field/agency confirmation for decisions. Do not treat image observations as confirmed crossing counts or permit determinations.
