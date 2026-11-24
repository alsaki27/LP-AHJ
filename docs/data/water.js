window.WATER_CROSSINGS = [
  {
    "id": "CHI-W01",
    "segment": "Spurs",
    "feature": "Spur1-S01-Bore",
    "station": 1615.4,
    "name": "Devon Avenue storm drainage at Arlington Heights Road",
    "priority": "Storm sewer screen",
    "method": "Carry a buried drainage utility conflict within the road bore. IDOT sheet 32 shows an existing 7 × 12 ft box culvert under Devon through the intersection.",
    "blocker": "The intermittent GIS line hits the route about 95 ft south-southeast of the county’s road intersection point. Its position and angle do not locate the culvert. Current box footprint, elevations, owner clearance and dry workspace remain open.",
    "lead": "Start with DuPage Highway Permits and Itasca Public Works for road-leg and drainage limits. Include Elk Grove Village Public Works for contract 63055 and resurfacing closeout records. Confirm who maintains the box and who signs the work permit.",
    "conditional": "Drainage owner approval for clearance. Have DuPage Stormwater screen the complete footprint if it approaches the ditch, outlet, mapped floodplain or wetland. Screen state and federal water permits if the design actually affects regulated resources.",
    "submit": "Send the crossing plan and profile keyed to IDOT 63055 sheet 32, Devon Sta. 62+42.83 / Arlington Heights Sta. 15+99.38. Obtain record plans and survey the box, adjacent sewers and duct banks, ROW, pits and outfall. Show owner-approved clearance, work limits and traffic control.",
    "fallback": "Compare an adjusted bore or surveyed shift within approved ROW if the box or utilities block clearance. Keep pits out of the pond and outlet. If controlled access or clearance cannot be secured, carry a short alignment shift along the permitted road leg.",
    "lat": 41.99238888,
    "lon": -88.00291791,
    "evidence": {
      "segment": "Spurs",
      "feature": "Spur1-S01-Bore",
      "station_ft": "1615.4",
      "latitude": "41.99238888",
      "longitude": "-88.00291791",
      "water_name": "",
      "layer_objectid": "18369",
      "water_fcode": "46003",
      "water_comid": "",
      "water_permanent_id": "109975692",
      "local_gis_angle_deg": "72.4",
      "county_place_township_screen": "DuPage / Itasca / Addison",
      "sampled_road_lead": "Devon Ave",
      "sampled_issuer_lead": "DuPage County DOT",
      "nearby_structure_inventory_leads": "No IDOT Structures point returned in ±0.001° box",
      "parcel_ids_at_point": "",
      "corridor_parcel_ids_within_100ft": "Dupage:0305201059 | Dupage:0305201060",
      "fema_at_point": "X AREA OF MINIMAL FLOOD HAZARD (17043C)",
      "nwi_within_100m": "Freshwater Pond PUBGx",
      "source_layer": "https://geoservices.epa.illinois.gov/arcgis/rest/services/Environmental/WaterFeatures/MapServer/2"
    },
    "review": {
      "classification": "buried",
      "confidence": "High",
      "finding": "IDOT contract 63055 sheet 32 marks an existing 7 × 12 ft box under Devon Avenue through the Arlington Heights Road intersection. The aerial shows pavement at the pin, about 95 ft south-southeast of the county intersection point. The mapped line does not locate the barrel.",
      "next_check": "Get the latest box and adjoining storm sewer as-builts. Survey the outside limits and inverts and clear the full bore envelope with the drainage owner.",
      "image": "img/water-pin-audit/CHI-W01.jpg",
      "imagery_catalog_dates": "2019-08-09",
      "proof": [
        [
          "Official flowline 18369",
          "https://geoservices.epa.illinois.gov/arcgis/rest/services/Environmental/WaterFeatures/MapServer/2/query?objectIds=18369&outFields=%2A&returnGeometry=true&outSR=4326&f=pjson"
        ],
        [
          "IDOT contract 63055, sheet 32",
          "https://apps.dot.illinois.gov/eplan/desenv/110708/63055-064/Plans/110708-63055-064-094-032-11x17.pdf"
        ],
        [
          "Devon plan and pin offset analysis",
          "research.html#proof-CHI-W01"
        ],
        [
          "Original USDA NAIP aerial",
          "https://imagery.nationalmap.gov/arcgis/rest/services/USGSNAIPImagery/ImageServer/exportImage?bbox=416830.374%2C4649317.607%2C417030.374%2C4649517.607&bboxSR=32616&imageSR=32616&size=540%2C540&format=jpg&f=image&interpolation=RSP_Bilinear"
        ],
        [
          "USGS imagery catalog at pin",
          "https://imagery.nationalmap.gov/arcgis/rest/services/USGSNAIPImagery/ImageServer/identify?geometry=%7B%22x%22%3A+-88.00291791%2C+%22y%22%3A+41.99238888%2C+%22spatialReference%22%3A+%7B%22wkid%22%3A+4326%7D%7D&geometryType=esriGeometryPoint&returnCatalogItems=true&maxItemCount=6&f=pjson"
        ]
      ]
    },
    "sources": [
      [
        "Devon drainage investigation",
        "research.html#proof-CHI-W01"
      ],
      [
        "IDOT 63055 drainage plan and profile, sheet 32",
        "https://apps.dot.illinois.gov/eplan/desenv/110708/63055-064/Plans/110708-63055-064-094-032-11x17.pdf"
      ],
      [
        "Itasca hydraulic study, March 2025 packet pp. 24–26 and 33–34",
        "https://www.itasca.com/AgendaCenter/ViewFile/Agenda/_03182025-1164?packet=true#page=24"
      ],
      [
        "DuPage Highway Permits",
        "https://www.dupagecounty.gov/government/departments/transportation/doing_business/permits/construction_permits.php"
      ],
      [
        "Itasca utility plan requirements",
        "https://www.itasca.com/DocumentCenter/View/16622/Utility-Permit-projects-Requirmentspdf"
      ],
      [
        "Official flowline layer",
        "https://geoservices.epa.illinois.gov/arcgis/rest/services/Environmental/WaterFeatures/MapServer/2"
      ]
    ]
  },
  {
    "id": "CHI-W02",
    "segment": "Spurs",
    "feature": "Spur1-S02-Water",
    "station": 197.8,
    "name": "Salt Creek at Arlington Heights Road",
    "priority": "Major crossing",
    "method": "Engineered HDD with lawful upland pits. Check spare bridge duct in parallel.",
    "blocker": "Need verified floodway and wetland boundaries, scour and foundation clearance, geotechnical profile and dry legal pits on both sides. No bridge duct rights or attachment capacity established.",
    "lead": "Cook DoTH Permits and Structures review highway and bridge 016-3014. The owner of any existing duct must grant use.",
    "conditional": "Elk Grove floodplain, MWRD permit determination and IDNR/OWR for actual work limits. USACE Chicago for §10 or §404 determination. Illinois EPA certification where triggered. Obtain land or preserve consent if the workspace enters it.",
    "submit": "Plan/profile of 016-3014 and both approaches with bed/scour, abutments, legal work limits, geotechnical basis, utility elevations and drilling fluid response. Include floodway and temporary/permanent footprint. For attachment add conduit/support details, inspection/clearance and sealed structural review.",
    "fallback": "If HDD is rejected because pits or floodway impacts cannot be accepted, seek a licensed existing duct or approved bridge attachment. If those are unavailable, test a local perpendicular alignment with upland access before considering another crossing road.",
    "lat": 42.01211868,
    "lon": -88.00095631,
    "evidence": {
      "segment": "Spurs",
      "feature": "Spur1-S02-Water",
      "station_ft": "197.8",
      "latitude": "42.01211868",
      "longitude": "-88.00095631",
      "water_name": "Salt Creek",
      "layer_objectid": "16938",
      "water_fcode": "46006",
      "water_comid": "",
      "water_permanent_id": "109975638",
      "local_gis_angle_deg": "86.8",
      "county_place_township_screen": "Cook / Elk Grove Village / Elk Grove",
      "sampled_road_lead": "Arlington Heights Rd",
      "sampled_issuer_lead": "Cook County DOTH",
      "nearby_structure_inventory_leads": "016-3014 (Arlington Heights Rd / Salt Creek; IDOT OID 7553)",
      "parcel_ids_at_point": "",
      "corridor_parcel_ids_within_100ft": "Cook:08283030020000 | Cook:08294020070000",
      "fema_at_point": "Unavailable",
      "nwi_within_100m": "Riverine R2UBHx | Riverine R5UBH",
      "source_layer": "https://geoservices.epa.illinois.gov/arcgis/rest/services/Environmental/WaterFeatures/MapServer/2"
    },
    "review": {
      "classification": "open",
      "confidence": "High",
      "finding": "Salt Creek is visible upstream and downstream of Arlington Heights Road. IDOT structure 016-3014 spans the same creek at the road.",
      "next_check": "Survey the banks, scour and structure limits. Check upland drill pits and bridge duct availability as separate concepts.",
      "image": "img/water-pin-audit/CHI-W02.jpg",
      "imagery_catalog_dates": "2019-08-09",
      "proof": [
        [
          "Official flowline 16938",
          "https://geoservices.epa.illinois.gov/arcgis/rest/services/Environmental/WaterFeatures/MapServer/2/query?objectIds=16938&outFields=%2A&returnGeometry=true&outSR=4326&f=pjson"
        ],
        [
          "IDOT Salt Creek structure 016-3014",
          "https://gis1.dot.illinois.gov/arcgis/rest/services/TrafficSafety/cis_LocationTool2026/MapServer/4/query?objectIds=7553&outFields=%2A&returnGeometry=true&outSR=4326&f=pjson"
        ],
        [
          "Original USDA NAIP aerial",
          "https://imagery.nationalmap.gov/arcgis/rest/services/USGSNAIPImagery/ImageServer/exportImage?bbox=417018.463%2C4651506.319%2C417218.463%2C4651706.319&bboxSR=32616&imageSR=32616&size=540%2C540&format=jpg&f=image&interpolation=RSP_Bilinear"
        ],
        [
          "USGS imagery catalog at pin",
          "https://imagery.nationalmap.gov/arcgis/rest/services/USGSNAIPImagery/ImageServer/identify?geometry=%7B%22x%22%3A+-88.00095631%2C+%22y%22%3A+42.01211868%2C+%22spatialReference%22%3A+%7B%22wkid%22%3A+4326%7D%7D&geometryType=esriGeometryPoint&returnCatalogItems=true&maxItemCount=6&f=pjson"
        ]
      ]
    },
    "sources": [
      [
        "Cook DoTH utility permit intake",
        "https://www.cookcountyil.gov/service/constructionmaintenance-permits"
      ],
      [
        "IDOT structure inventory",
        "https://gis1.dot.illinois.gov/arcgis/rest/services/TrafficSafety/cis_LocationTool2026/MapServer/4"
      ],
      [
        "IDNR waterway permits",
        "https://dnr.illinois.gov/waterresources/permitprograms.html"
      ],
      [
        "MWRD permit determinations",
        "https://www.mwrd.org/doing-business/watershed-management-ordinance-and-infiltrationinflow/watershed-management-ordinance-wmo-and-technical-guidance-manual-tgm/watershed-management-ordinance-wmo-frequently-asked-questions-faqs"
      ],
      [
        "Official flowline layer",
        "https://geoservices.epa.illinois.gov/arcgis/rest/services/Environmental/WaterFeatures/MapServer/2"
      ]
    ]
  },
  {
    "id": "CHI-W03",
    "segment": "Spurs",
    "feature": "Spur4-S01-Bore",
    "station": 7891.3,
    "name": "Willow Creek culvert at Arthur Avenue",
    "priority": "Asset and ROW",
    "method": "Independent bore clear of culvert 016-7861 and its end treatments.",
    "blocker": "Three-cell asset is identified. Actual outside barrel, foundation, headwall and parallel utility limits are still needed. Pits must clear industrial accesses.",
    "lead": "Elk Grove Engineering and culvert owner review village road work and structure clearances. Confirm owner and accepted bore envelope from as-builts.",
    "conditional": "Cook DoTH or IDOT if the work extends to their facilities. MWRD/IDNR and USACE Chicago if the final disturbance footprint reaches regulated areas. Illinois EPA if triggered.",
    "submit": "Culvert as-built, surveyed headwalls/inverts, utility conflict sheet, independent bore profile and pit offsets, truck access and pavement restoration. Include drainage/ROW permit determination.",
    "fallback": "If the side-clearance bore is refused, test a deeper or laterally shifted independent bore on Arthur within approved ROW. If no public workspace fits, secure frontage access and resubmit with a revised work envelope.",
    "lat": 41.99566546,
    "lon": -87.96420817,
    "evidence": {
      "segment": "Spurs",
      "feature": "Spur4-S01-Bore",
      "station_ft": "7891.3",
      "latitude": "41.99566546",
      "longitude": "-87.96420817",
      "water_name": "",
      "layer_objectid": "17019",
      "water_fcode": "46003",
      "water_comid": "",
      "water_permanent_id": "109975676",
      "local_gis_angle_deg": "89.4",
      "county_place_township_screen": "Cook / Elk Grove Village / Elk Grove",
      "sampled_road_lead": "Arthur Ave",
      "sampled_issuer_lead": "Elk Grove Village (Village)",
      "nearby_structure_inventory_leads": "016-7861 (Arthur Ave / Willow Creek; IDOT OID 7192)",
      "parcel_ids_at_point": "",
      "corridor_parcel_ids_within_100ft": "Cook:08344020380000 | Cook:08344020390000 | Cook:08344020470000 | Cook:08344020620000",
      "fema_at_point": "Unavailable",
      "nwi_within_100m": "Riverine R4SBC",
      "source_layer": "https://geoservices.epa.illinois.gov/arcgis/rest/services/Environmental/WaterFeatures/MapServer/2"
    },
    "review": {
      "classification": "buried",
      "confidence": "High",
      "finding": "The grass corridor reaches Arthur Avenue with no exposed channel through the pavement. IDOT structure 016-7861 identifies the Willow Creek crossing as a three-cell culvert.",
      "next_check": "Locate all cells, headwalls, inverts and outside edges before setting the independent bore profile.",
      "image": "img/water-pin-audit/CHI-W03.jpg",
      "imagery_catalog_dates": "2019-08-09",
      "proof": [
        [
          "Official flowline 17019",
          "https://geoservices.epa.illinois.gov/arcgis/rest/services/Environmental/WaterFeatures/MapServer/2/query?objectIds=17019&outFields=%2A&returnGeometry=true&outSR=4326&f=pjson"
        ],
        [
          "IDOT Willow Creek structure 016-7861",
          "https://gis1.dot.illinois.gov/arcgis/rest/services/TrafficSafety/cis_LocationTool2026/MapServer/4/query?objectIds=7192&outFields=%2A&returnGeometry=true&outSR=4326&f=pjson"
        ],
        [
          "Original USDA NAIP aerial",
          "https://imagery.nationalmap.gov/arcgis/rest/services/USGSNAIPImagery/ImageServer/exportImage?bbox=420040.752%2C4649644.580%2C420240.752%2C4649844.580&bboxSR=32616&imageSR=32616&size=540%2C540&format=jpg&f=image&interpolation=RSP_Bilinear"
        ],
        [
          "USGS imagery catalog at pin",
          "https://imagery.nationalmap.gov/arcgis/rest/services/USGSNAIPImagery/ImageServer/identify?geometry=%7B%22x%22%3A+-87.96420817%2C+%22y%22%3A+41.99566546%2C+%22spatialReference%22%3A+%7B%22wkid%22%3A+4326%7D%7D&geometryType=esriGeometryPoint&returnCatalogItems=true&maxItemCount=6&f=pjson"
        ]
      ]
    },
    "sources": [
      [
        "Elk Grove Village utility code",
        "https://codelibrary.amlegal.com/codes/elkgrovevillageil/latest/elkgrovevillage_il/0-0-0-6645"
      ],
      [
        "IDOT structure inventory",
        "https://gis1.dot.illinois.gov/arcgis/rest/services/TrafficSafety/cis_LocationTool2026/MapServer/4"
      ],
      [
        "MWRD permit determinations",
        "https://www.mwrd.org/doing-business/watershed-management-ordinance-and-infiltrationinflow/watershed-management-ordinance-wmo-and-technical-guidance-manual-tgm/watershed-management-ordinance-wmo-frequently-asked-questions-faqs"
      ],
      [
        "Official flowline layer",
        "https://geoservices.epa.illinois.gov/arcgis/rest/services/Environmental/WaterFeatures/MapServer/2"
      ]
    ]
  },
  {
    "id": "S0-W01",
    "segment": "Segment0",
    "feature": "S0-S002-Water",
    "station": 352.5,
    "name": "South Fork Licking River at Worthington Road",
    "priority": "Major crossing",
    "method": "Survey SFN 4538323 and design an independent bore clear of the culvert and end treatments.",
    "blocker": "ODOT lists a 90-ft culvert about 125 ft from the pin. The alignment tie, barrel limits, road controller and legal pit locations still need proof.",
    "lead": "Licking County Engineer/Commissioners and New Albany Public Service assign the relevant CR-162 road and structure approvals under the applicable agreement.",
    "conditional": "Local floodplain administrator and Huntington Regulatory for actual reach and impacts. Ohio EPA if certification or isolated wetland authorization is required. Landowners for work outside documented ROW.",
    "submit": "Show SFN 4538323 as-builts, surveyed headwalls, inverts and barrel limits, CR-162 control, station tie, profile, utilities, easements, access and disturbance.",
    "fallback": "If culvert clearance or pit access prevents the crossing, test a short shift within approved road limits and resurvey each end.",
    "lat": 40.07864939,
    "lon": -82.73696801,
    "evidence": {
      "segment": "Segment0",
      "feature": "S0-S002-Water",
      "station_ft": "352.5",
      "latitude": "40.07864939",
      "longitude": "-82.73696801",
      "water_name": "South Fork Licking River",
      "layer_objectid": "28893",
      "water_fcode": "46006",
      "water_comid": "15363359",
      "water_permanent_id": "",
      "local_gis_angle_deg": "65.8",
      "county_place_township_screen": "LICKING / NEW ALBANY / JERSEY",
      "sampled_road_lead": "Worthington CR-162",
      "sampled_issuer_lead": "Shared by road maintenance agreement – New Albany Ch. 907 + Licking County Commissioners utility permit",
      "nearby_structure_inventory_leads": "4538323 @ 125 ft (Worthington Rd / South Fork, maintain code 02)",
      "parcel_ids_at_point": "Licking:094-107514-00.000",
      "corridor_parcel_ids_within_100ft": "Licking:035-106566-00.004 | Licking:094-107514-00.000",
      "fema_at_point": "X AREA OF MINIMAL FLOOD HAZARD (39089C)",
      "nwi_within_100m": "Riverine R5UBH",
      "source_layer": "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0"
    },
    "review": {
      "classification": "buried",
      "confidence": "Medium",
      "finding": "The aerial shows the low corridor meeting the road embankment. ODOT lists SFN 4538323 as a 90-ft culvert carrying Worthington Road over the South Fork, about 125 ft from the pin.",
      "next_check": "Trace the same-road culvert to both ends and tie it to the alignment. Use surveyed barrel clearance to set the bore profile.",
      "image": "img/water-pin-audit/S0-W01.jpg",
      "imagery_catalog_dates": "2023-05-21",
      "proof": [
        [
          "Official flowline 28893",
          "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0/query?objectIds=28893&outFields=%2A&returnGeometry=true&outSR=4326&f=pjson"
        ],
        [
          "ODOT structure 4538323",
          "https://tims.dot.state.oh.us/ags/rest/services/Assets/Bridge_Inventory/MapServer/0/query?where=SFN+IN+%28%274538323%27%29&outFields=SFN%2CSTR_LOC_CARRIED%2CINVENT_FEAT%2CMAIN_STR_TYPE_CD%2CCULVERT_LEN%2CMAINT_RESP_CD&returnGeometry=true&outSR=4326&f=pjson"
        ],
        [
          "Original USDA NAIP aerial",
          "https://imagery.nationalmap.gov/arcgis/rest/services/USGSNAIPImagery/ImageServer/exportImage?bbox=351799.250%2C4437832.185%2C351999.250%2C4438032.185&bboxSR=32617&imageSR=32617&size=540%2C540&format=jpg&f=image&interpolation=RSP_Bilinear"
        ],
        [
          "Ohio statewide aerial",
          "https://maps.ohio.gov/image/rest/services/osip_most_current/ImageServer/exportImage?bbox=351799.250%2C4437832.185%2C351999.250%2C4438032.185&bboxSR=32617&imageSR=32617&size=540%2C540&format=jpg&f=image&interpolation=RSP_Bilinear"
        ],
        [
          "USGS imagery catalog at pin",
          "https://imagery.nationalmap.gov/arcgis/rest/services/USGSNAIPImagery/ImageServer/identify?geometry=%7B%22x%22%3A+-82.73696801%2C+%22y%22%3A+40.07864939%2C+%22spatialReference%22%3A+%7B%22wkid%22%3A+4326%7D%7D&geometryType=esriGeometryPoint&returnCatalogItems=true&maxItemCount=6&f=pjson"
        ]
      ]
    },
    "sources": [
      [
        "Licking County Engineer utility permit",
        "https://lickingcounty.gov/depts/engineer/permits.htm"
      ],
      [
        "New Albany ROW application and checklist",
        "https://newalbanyohio.org/right-of-way/"
      ],
      [
        "Official flowline layer",
        "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0"
      ]
    ]
  },
  {
    "id": "S0-W02",
    "segment": "Segment0",
    "feature": "S0-S003-Bore",
    "station": 15719.3,
    "name": "Dublin–Granville tributary near SFN 2536137",
    "priority": "Asset and ROW",
    "method": "Separate short bore clear of the local structure.",
    "blocker": "Local tributary structure is about 20 ft away. Need barrel/end treatment limits and confirmation that the local work package clears the nearby SR 161 Geiger Run crossing.",
    "lead": "Franklin County Engineer for candidate structure 2536137. New Albany for city work if the governing street segment falls under city control.",
    "conditional": "ODOT D6 only if state property or SFN 2509490 is affected. Local floodplain and Ohio water agency review as the surveyed impacts warrant.",
    "submit": "Local and state limits on one exhibit, surveyed pipe/structure envelope, crossing profile, pits, utilities, traffic and any temporary disturbance.",
    "fallback": "If the local bore side is rejected, use a revised local road offset clear of the foundations. Treat any move toward SR 161 as a new state ROW and access decision.",
    "lat": 40.07956108,
    "lon": -82.77829792,
    "evidence": {
      "segment": "Segment0",
      "feature": "S0-S003-Bore",
      "station_ft": "15719.3",
      "latitude": "40.07956108",
      "longitude": "-82.77829792",
      "water_name": "",
      "layer_objectid": "21930",
      "water_fcode": "46003",
      "water_comid": "5213289",
      "water_permanent_id": "",
      "local_gis_angle_deg": "57.6",
      "county_place_township_screen": "FRANKLIN / NEW ALBANY / PLAIN",
      "sampled_road_lead": "Dublin-Granville CR-546",
      "sampled_issuer_lead": "Franklin County Engineer",
      "nearby_structure_inventory_leads": "2536137 @ 20 ft (DUBLIN-GRANVILLE / TRIBUTARY(DUBLIN-GRANVIL, maintain code 02) | 2509490 @ 221 ft (SR-161 / GEIGER RUN, maintain code 01)",
      "parcel_ids_at_point": "Franklin:222-002921",
      "corridor_parcel_ids_within_100ft": "Franklin:220-000555 | Franklin:220-000703 | Franklin:222-002921",
      "fema_at_point": "X AREA OF MINIMAL FLOOD HAZARD (39049C)",
      "nwi_within_100m": "Riverine R4SBC",
      "source_layer": "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0"
    },
    "review": {
      "classification": "open",
      "confidence": "High",
      "finding": "The wooded channel meets Dublin–Granville Road at frame structure 2536137, about 20 ft from the pin. Inventory code 07 identifies a frame structure. The SR 161 Geiger Run culvert is a separate structure north of the road.",
      "next_check": "Tie the channel and frame foundations to the alignment. Keep the SR 161 structure separate unless the work limits reach it.",
      "image": "img/water-pin-audit/S0-W02.jpg",
      "imagery_catalog_dates": "2023-05-21",
      "proof": [
        [
          "Official flowline 21930",
          "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0/query?objectIds=21930&outFields=%2A&returnGeometry=true&outSR=4326&f=pjson"
        ],
        [
          "ODOT structure 2536137",
          "https://tims.dot.state.oh.us/ags/rest/services/Assets/Bridge_Inventory/MapServer/0/query?where=SFN+IN+%28%272536137%27%29&outFields=SFN%2CSTR_LOC_CARRIED%2CINVENT_FEAT%2CMAIN_STR_TYPE_CD%2CCULVERT_LEN%2CMAINT_RESP_CD&returnGeometry=true&outSR=4326&f=pjson"
        ],
        [
          "ODOT structure 2509490",
          "https://tims.dot.state.oh.us/ags/rest/services/Assets/Bridge_Inventory/MapServer/0/query?where=SFN+IN+%28%272509490%27%29&outFields=SFN%2CSTR_LOC_CARRIED%2CINVENT_FEAT%2CMAIN_STR_TYPE_CD%2CCULVERT_LEN%2CMAINT_RESP_CD&returnGeometry=true&outSR=4326&f=pjson"
        ],
        [
          "Original USDA NAIP aerial",
          "https://imagery.nationalmap.gov/arcgis/rest/services/USGSNAIPImagery/ImageServer/exportImage?bbox=348277.128%2C4438003.009%2C348477.128%2C4438203.009&bboxSR=32617&imageSR=32617&size=540%2C540&format=jpg&f=image&interpolation=RSP_Bilinear"
        ],
        [
          "Ohio statewide aerial",
          "https://maps.ohio.gov/image/rest/services/osip_most_current/ImageServer/exportImage?bbox=348277.128%2C4438003.009%2C348477.128%2C4438203.009&bboxSR=32617&imageSR=32617&size=540%2C540&format=jpg&f=image&interpolation=RSP_Bilinear"
        ],
        [
          "USGS imagery catalog at pin",
          "https://imagery.nationalmap.gov/arcgis/rest/services/USGSNAIPImagery/ImageServer/identify?geometry=%7B%22x%22%3A+-82.77829792%2C+%22y%22%3A+40.07956108%2C+%22spatialReference%22%3A+%7B%22wkid%22%3A+4326%7D%7D&geometryType=esriGeometryPoint&returnCatalogItems=true&maxItemCount=6&f=pjson"
        ]
      ]
    },
    "sources": [
      [
        "Franklin County Engineer utility application",
        "https://www.franklincountyengineer.org/wp-content/uploads/2016/04/Application-for-permit-pdf.pdf"
      ],
      [
        "New Albany ROW application and checklist",
        "https://newalbanyohio.org/right-of-way/"
      ],
      [
        "ODOT ROW permit intake",
        "https://www.transportation.ohio.gov/business/permits/row-permits"
      ],
      [
        "Official flowline layer",
        "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0"
      ]
    ]
  },
  {
    "id": "S0-W03",
    "segment": "Segment0",
    "feature": "S0-S004-Water",
    "station": 214.3,
    "name": "Blacklick Creek at Dublin–Granville Road",
    "priority": "Major crossing",
    "method": "Local-corridor HDD with staging outside the mapped floodway where feasible.",
    "blocker": "FEMA returned AE floodway. SFN 2536110 is about 22 ft away, while the two nearby SR 161 structures sit on a different road. Need surveyed bridge, state access and upland pit limits.",
    "lead": "New Albany for its street occupation and Franklin County Engineer for the local bridge envelope. Confirm the document that assigns each role.",
    "conditional": "Local floodplain administrator for the mapped floodway. Huntington and Ohio EPA as triggered. ODOT D6 for any SR 161 ROW, structure or access impact.",
    "submit": "SFN 2536110 and SR 161 limits with survey ties, floodway and temporary work, bank/scour profile, utilities, wetland limits, easements and fluid contingency.",
    "fallback": "Compare the other side of the local corridor. If no workable HDD footprint is accepted, test the local bridge attachment with Franklin. A shift onto the SR 161 bridge needs its own ODOT approval.",
    "lat": 40.07983666,
    "lon": -82.78426909,
    "evidence": {
      "segment": "Segment0",
      "feature": "S0-S004-Water",
      "station_ft": "214.3",
      "latitude": "40.07983666",
      "longitude": "-82.78426909",
      "water_name": "Blacklick Creek",
      "layer_objectid": "21929",
      "water_fcode": "46006",
      "water_comid": "5213287",
      "water_permanent_id": "",
      "local_gis_angle_deg": "67.3",
      "county_place_township_screen": "FRANKLIN / NEW ALBANY / PLAIN",
      "sampled_road_lead": "Dublin-Granville CR-546",
      "sampled_issuer_lead": "City of New Albany – maintains street; Ch. 907 permit (FCEO at county bridges, e.g., Rocky Fork)",
      "nearby_structure_inventory_leads": "2536110 @ 22 ft (DUBLIN-GRANVILLE / BLACKLICK CR (DUBLIN-GRA, maintain code 02) | 2509474 @ 162 ft (SR 161 EB / BLACKLICK CREEK, maintain code 01) | 2509466 @ 252 ft (SR 161 WB / BLACKLICK CREEK, maintain code 01)",
      "parcel_ids_at_point": "Franklin:222-002931",
      "corridor_parcel_ids_within_100ft": "Franklin:222-002931 | Franklin:222-004501",
      "fema_at_point": "AE FLOODWAY (39049C)",
      "nwi_within_100m": "Riverine R5UBH",
      "source_layer": "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0"
    },
    "review": {
      "classification": "open",
      "confidence": "High",
      "finding": "Blacklick Creek and its banks line up with the Dublin–Granville Road bridge. ODOT SFN 2536110 is about 22 ft from the pin. The inventory has two additional SR 161 bridge records north of this crossing.",
      "next_check": "Survey the creek, bridge foundations and floodway limits near the local-road bore. Check state bridge limits only if staging or drilling reaches SR 161.",
      "image": "img/water-pin-audit/S0-W03.jpg",
      "imagery_catalog_dates": "2023-05-21",
      "proof": [
        [
          "Official flowline 21929",
          "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0/query?objectIds=21929&outFields=%2A&returnGeometry=true&outSR=4326&f=pjson"
        ],
        [
          "ODOT structure 2536110",
          "https://tims.dot.state.oh.us/ags/rest/services/Assets/Bridge_Inventory/MapServer/0/query?where=SFN+IN+%28%272536110%27%29&outFields=SFN%2CSTR_LOC_CARRIED%2CINVENT_FEAT%2CMAIN_STR_TYPE_CD%2CCULVERT_LEN%2CMAINT_RESP_CD&returnGeometry=true&outSR=4326&f=pjson"
        ],
        [
          "Original USDA NAIP aerial",
          "https://imagery.nationalmap.gov/arcgis/rest/services/USGSNAIPImagery/ImageServer/exportImage?bbox=347768.594%2C4438043.794%2C347968.594%2C4438243.794&bboxSR=32617&imageSR=32617&size=540%2C540&format=jpg&f=image&interpolation=RSP_Bilinear"
        ],
        [
          "Ohio statewide aerial",
          "https://maps.ohio.gov/image/rest/services/osip_most_current/ImageServer/exportImage?bbox=347768.594%2C4438043.794%2C347968.594%2C4438243.794&bboxSR=32617&imageSR=32617&size=540%2C540&format=jpg&f=image&interpolation=RSP_Bilinear"
        ],
        [
          "USGS imagery catalog at pin",
          "https://imagery.nationalmap.gov/arcgis/rest/services/USGSNAIPImagery/ImageServer/identify?geometry=%7B%22x%22%3A+-82.78426909%2C+%22y%22%3A+40.07983666%2C+%22spatialReference%22%3A+%7B%22wkid%22%3A+4326%7D%7D&geometryType=esriGeometryPoint&returnCatalogItems=true&maxItemCount=6&f=pjson"
        ]
      ]
    },
    "sources": [
      [
        "Franklin County Engineer utility application",
        "https://www.franklincountyengineer.org/wp-content/uploads/2016/04/Application-for-permit-pdf.pdf"
      ],
      [
        "New Albany ROW application and checklist",
        "https://newalbanyohio.org/right-of-way/"
      ],
      [
        "ODOT ROW permit intake",
        "https://www.transportation.ohio.gov/business/permits/row-permits"
      ],
      [
        "Official flowline layer",
        "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0"
      ]
    ]
  },
  {
    "id": "S0-W04",
    "segment": "Segment0",
    "feature": "S0-S007-Bore",
    "station": 1554.6,
    "name": "Rose Run near Dublin–Granville Road",
    "priority": "Project coordination",
    "method": "Trace the active drainage and confirm new grading before including a drainage-specific bore.",
    "blocker": "The flowline is mapped but the current channel or pipe alignment and Rose Run Phase Two construction/restoration limits may differ from the source GIS.",
    "lead": "New Albany Public Service for road occupation. City project engineer and drainage owner confirm final channel, storm and joint-work limitations.",
    "conditional": "Huntington and Ohio EPA when work impacts trigger review. Local floodplain or private access approvals if the new footprint requires them.",
    "submit": "Overlay exact route station with Phase Two issued plans and final grading. Submit as-built or proposed storm profiles, bore/pit details, restoration tie and staging or shared-work exhibit.",
    "fallback": "If staged work or conduit sharing is refused, wait for as-builts and bore outside the restored project limits. Shift the pits away from the final grading and retain lawful access.",
    "lat": 40.08069869,
    "lon": -82.80288701,
    "evidence": {
      "segment": "Segment0",
      "feature": "S0-S007-Bore",
      "station_ft": "1554.6",
      "latitude": "40.08069869",
      "longitude": "-82.80288701",
      "water_name": "Rose Run",
      "layer_objectid": "21928",
      "water_fcode": "46003",
      "water_comid": "5213285",
      "water_permanent_id": "",
      "local_gis_angle_deg": "65.4",
      "county_place_township_screen": "FRANKLIN / NEW ALBANY / PLAIN",
      "sampled_road_lead": "Dublin-Granville CR-546",
      "sampled_issuer_lead": "City of New Albany – maintains street; Ch. 907 permit (FCEO at county bridges, e.g., Rocky Fork)",
      "nearby_structure_inventory_leads": "",
      "parcel_ids_at_point": "Franklin:222-000293",
      "corridor_parcel_ids_within_100ft": "Franklin:222-000240 | Franklin:222-000293 | Franklin:222-004730",
      "fema_at_point": "X AREA OF MINIMAL FLOOD HAZARD (39049C)",
      "nwi_within_100m": "Riverine R4SBC",
      "source_layer": "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0"
    },
    "review": {
      "classification": "gis",
      "confidence": "Unverified",
      "finding": "The flowline reaches a developed road shoulder. The visible pond sits to the northwest. Neither aerial establishes a surface channel, and the ODOT query did not identify a matched structure. New Albany confirms Rose Run work in the area.",
      "next_check": "Use New Albany storm plans and subdivision records to trace any pond outlet to the pin before carrying a special crossing item.",
      "image": "img/water-pin-audit/S0-W04.jpg",
      "imagery_catalog_dates": "2023-05-21",
      "proof": [
        [
          "Official flowline 21928",
          "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0/query?objectIds=21928&outFields=%2A&returnGeometry=true&outSR=4326&f=pjson"
        ],
        [
          "New Albany Rose Run project context",
          "https://newalbanyohio.org/news/2026/10/rose-run-phase-two-update-s-high-st-lane-closure-through-nov-25/"
        ],
        [
          "Original USDA NAIP aerial",
          "https://imagery.nationalmap.gov/arcgis/rest/services/USGSNAIPImagery/ImageServer/exportImage?bbox=346183.031%2C4438171.487%2C346383.031%2C4438371.487&bboxSR=32617&imageSR=32617&size=540%2C540&format=jpg&f=image&interpolation=RSP_Bilinear"
        ],
        [
          "Ohio statewide aerial",
          "https://maps.ohio.gov/image/rest/services/osip_most_current/ImageServer/exportImage?bbox=346183.031%2C4438171.487%2C346383.031%2C4438371.487&bboxSR=32617&imageSR=32617&size=540%2C540&format=jpg&f=image&interpolation=RSP_Bilinear"
        ],
        [
          "USGS imagery catalog at pin",
          "https://imagery.nationalmap.gov/arcgis/rest/services/USGSNAIPImagery/ImageServer/identify?geometry=%7B%22x%22%3A+-82.80288701%2C+%22y%22%3A+40.08069869%2C+%22spatialReference%22%3A+%7B%22wkid%22%3A+4326%7D%7D&geometryType=esriGeometryPoint&returnCatalogItems=true&maxItemCount=6&f=pjson"
        ],
        [
          "ODOT nearby bridge inventory query",
          "https://tims.dot.state.oh.us/ags/rest/services/Assets/Bridge_Inventory/MapServer/0/query?where=1%3D1&geometry=-82.80464809%2C40.07935122%2C-82.80112593%2C40.08204616&geometryType=esriGeometryEnvelope&inSR=4326&outFields=%2A&returnGeometry=true&outSR=4326&f=pjson"
        ],
        [
          "ODOT nearby conduit inventory query",
          "https://tims.dot.state.oh.us/ags/rest/services/Assets/Conduit_Inventory/MapServer/0/query?where=1%3D1&geometry=-82.80464809%2C40.07935122%2C-82.80112593%2C40.08204616&geometryType=esriGeometryEnvelope&inSR=4326&outFields=%2A&returnGeometry=true&outSR=4326&f=pjson"
        ]
      ]
    },
    "sources": [
      [
        "New Albany ROW application and checklist",
        "https://newalbanyohio.org/right-of-way/"
      ],
      [
        "New Albany Rose Run project",
        "https://newalbanyohio.org/news/2026/10/rose-run-phase-two-update-s-high-st-lane-closure-through-nov-25/"
      ],
      [
        "Official flowline layer",
        "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0"
      ]
    ]
  },
  {
    "id": "S0-W05",
    "segment": "Segment0",
    "feature": "S0-S008-Water",
    "station": 286.9,
    "name": "Rocky Fork flowline / Sugar Run structure lead",
    "priority": "Asset and ROW",
    "method": "Independent HDD or trenchless clearance at the surveyed hit.",
    "blocker": "ODOT names the intersected line Rocky Fork. SFN 2536072, about 143 ft away, says Sugar Run. Need actual hydraulic connection and bridge influence limits.",
    "lead": "New Albany for roadway work where applicable. Franklin County Engineer for SFN 2536072 and verification of structure and drainage identity.",
    "conditional": "Local floodplain reviewer and Ohio water approvals only as actual work dictates. Private or park rights if work moves beyond public ROW.",
    "submit": "Both source IDs with surveyed channel/barrel and foundation footprints, matched road and ROW stationing, pit plan and bore section. Use surveyed location on permit exhibits.",
    "fallback": "If rejected near the current line, shift locally around the surveyed structure in verified ROW. Evaluate a structure-centered alternative only after the plans connect it to the actual feature.",
    "lat": 40.08005537,
    "lon": -82.83523267,
    "evidence": {
      "segment": "Segment0",
      "feature": "S0-S008-Water",
      "station_ft": "286.9",
      "latitude": "40.08005537",
      "longitude": "-82.83523267",
      "water_name": "Rocky Fork",
      "layer_objectid": "21932",
      "water_fcode": "46006",
      "water_comid": "5213293",
      "water_permanent_id": "",
      "local_gis_angle_deg": "63.7",
      "county_place_township_screen": "FRANKLIN / NEW ALBANY / PLAIN",
      "sampled_road_lead": "Dublin-Granville CR-546",
      "sampled_issuer_lead": "City of New Albany – maintains street; Ch. 907 permit (FCEO at county bridges, e.g., Rocky Fork)",
      "nearby_structure_inventory_leads": "2536072 @ 143 ft (DUBLIN-GRANVILLE / SUGAR RUN (DUBLIN-GRANV, maintain code 02)",
      "parcel_ids_at_point": "Franklin:222-002057",
      "corridor_parcel_ids_within_100ft": "Franklin:010-300543 | Franklin:222-002057 | Franklin:222-005164",
      "fema_at_point": "X AREA OF MINIMAL FLOOD HAZARD (39049C)",
      "nwi_within_100m": "Riverine R5UBH",
      "source_layer": "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0"
    },
    "review": {
      "classification": "open",
      "confidence": "Medium",
      "finding": "The leaf-off aerial supports a wooded channel crossing near Harlem Road. Dublin–Granville Road slab bridge 2536072 is about 143 ft from the pin. The bridge inventory says Sugar Run while the mapped flowline says Rocky Fork. Ohio EPA lists a separate Sugar Run sample north on Harlem Road.",
      "next_check": "Survey the ravine, both bridge locations and the route tie. Confirm the name and asset before sizing or pricing the crossing.",
      "image": "img/water-pin-audit/S0-W05.jpg",
      "imagery_catalog_dates": "2023-05-21",
      "proof": [
        [
          "Official flowline 21932",
          "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0/query?objectIds=21932&outFields=%2A&returnGeometry=true&outSR=4326&f=pjson"
        ],
        [
          "ODOT structure 2536072",
          "https://tims.dot.state.oh.us/ags/rest/services/Assets/Bridge_Inventory/MapServer/0/query?where=SFN+IN+%28%272536072%27%29&outFields=SFN%2CSTR_LOC_CARRIED%2CINVENT_FEAT%2CMAIN_STR_TYPE_CD%2CCULVERT_LEN%2CMAINT_RESP_CD&returnGeometry=true&outSR=4326&f=pjson"
        ],
        [
          "Ohio EPA stream sampling locations, table 4",
          "https://dam.assets.ohio.gov/image/upload/epa.ohio.gov/Portals/35/tmdl/MSWBW-QAPP.pdf#page=36"
        ],
        [
          "Original USDA NAIP aerial",
          "https://imagery.nationalmap.gov/arcgis/rest/services/USGSNAIPImagery/ImageServer/exportImage?bbox=343423.555%2C4438156.475%2C343623.555%2C4438356.475&bboxSR=32617&imageSR=32617&size=540%2C540&format=jpg&f=image&interpolation=RSP_Bilinear"
        ],
        [
          "Ohio statewide aerial",
          "https://maps.ohio.gov/image/rest/services/osip_most_current/ImageServer/exportImage?bbox=343423.555%2C4438156.475%2C343623.555%2C4438356.475&bboxSR=32617&imageSR=32617&size=540%2C540&format=jpg&f=image&interpolation=RSP_Bilinear"
        ],
        [
          "USGS imagery catalog at pin",
          "https://imagery.nationalmap.gov/arcgis/rest/services/USGSNAIPImagery/ImageServer/identify?geometry=%7B%22x%22%3A+-82.83523267%2C+%22y%22%3A+40.08005537%2C+%22spatialReference%22%3A+%7B%22wkid%22%3A+4326%7D%7D&geometryType=esriGeometryPoint&returnCatalogItems=true&maxItemCount=6&f=pjson"
        ]
      ]
    },
    "sources": [
      [
        "Franklin County Engineer utility application",
        "https://www.franklincountyengineer.org/wp-content/uploads/2016/04/Application-for-permit-pdf.pdf"
      ],
      [
        "New Albany ROW application and checklist",
        "https://newalbanyohio.org/right-of-way/"
      ],
      [
        "Official flowline layer",
        "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0"
      ]
    ]
  },
  {
    "id": "S0-W06",
    "segment": "Segment0",
    "feature": "S0-S010-Water",
    "station": 206.6,
    "name": "Rocky Fork bridge area at Dublin–Granville Road",
    "priority": "Major crossing",
    "method": "Near-normal HDD. Check owner-approved bridge duct/attachment if pits are limited.",
    "blocker": "Unnamed intersected hydro line sits about 130 ft from SFN 2536065. FEMA returned AE floodway. Need rebuilt bridge, path, ROW and channel survey.",
    "lead": "Franklin County Engineer for bridge and county facility decisions. New Albany Public Service for applicable street/approach work.",
    "conditional": "Trail operator if work affects trail access. Local floodplain review for mapped floodway. Huntington/Ohio EPA and landowners as the design triggers.",
    "submit": "As-built bridge and trail sheets, surveyed banks/scour, easement rights, bore and pit profile, traffic/trail staging and hydraulic work limits.",
    "fallback": "If dry pits cannot be approved, use accepted bridge duct or engineered attachment. If the bridge owner declines, compare a lateral HDD shift that preserves trail and ROW access.",
    "lat": 40.07925514,
    "lon": -82.84349983,
    "evidence": {
      "segment": "Segment0",
      "feature": "S0-S010-Water",
      "station_ft": "206.6",
      "latitude": "40.07925514",
      "longitude": "-82.84349983",
      "water_name": "",
      "layer_objectid": "21933",
      "water_fcode": "46006",
      "water_comid": "5213295",
      "water_permanent_id": "",
      "local_gis_angle_deg": "80.4",
      "county_place_township_screen": "FRANKLIN / NEW ALBANY / PLAIN",
      "sampled_road_lead": "Dublin-Granville CR-546",
      "sampled_issuer_lead": "City of New Albany – maintains street; Ch. 907 permit (FCEO at county bridges, e.g., Rocky Fork)",
      "nearby_structure_inventory_leads": "2536065 @ 130 ft (DUBLIN-GRANVILLE / Rocky Fork (Dublin-Granv, maintain code 02)",
      "parcel_ids_at_point": "Franklin:222-002057",
      "corridor_parcel_ids_within_100ft": "Franklin:010-217754 | Franklin:010-298375 | Franklin:222-002057 | Franklin:222-005165",
      "fema_at_point": "AE FLOODWAY (39049C)",
      "nwi_within_100m": "Riverine R5UBH",
      "source_layer": "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0"
    },
    "review": {
      "classification": "open",
      "confidence": "High",
      "finding": "Rocky Fork is visible on both sides of Old SR 161. Dublin–Granville Road bridge 2536065 is about 130 ft west of the pin. Ohio EPA sampling location V05S38 identifies Rocky Fork at Old SR 161 near the pin.",
      "next_check": "Tie the route to the actual banks, deck and foundations before selecting lawful pits or an approved duct.",
      "image": "img/water-pin-audit/S0-W06.jpg",
      "imagery_catalog_dates": "2023-05-21",
      "proof": [
        [
          "Official flowline 21933",
          "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0/query?objectIds=21933&outFields=%2A&returnGeometry=true&outSR=4326&f=pjson"
        ],
        [
          "ODOT structure 2536065",
          "https://tims.dot.state.oh.us/ags/rest/services/Assets/Bridge_Inventory/MapServer/0/query?where=SFN+IN+%28%272536065%27%29&outFields=SFN%2CSTR_LOC_CARRIED%2CINVENT_FEAT%2CMAIN_STR_TYPE_CD%2CCULVERT_LEN%2CMAINT_RESP_CD&returnGeometry=true&outSR=4326&f=pjson"
        ],
        [
          "Ohio EPA stream sampling locations, table 4",
          "https://dam.assets.ohio.gov/image/upload/epa.ohio.gov/Portals/35/tmdl/MSWBW-QAPP.pdf#page=36"
        ],
        [
          "Original USDA NAIP aerial",
          "https://imagery.nationalmap.gov/arcgis/rest/services/USGSNAIPImagery/ImageServer/exportImage?bbox=342716.794%2C4438082.224%2C342916.794%2C4438282.224&bboxSR=32617&imageSR=32617&size=540%2C540&format=jpg&f=image&interpolation=RSP_Bilinear"
        ],
        [
          "Ohio statewide aerial",
          "https://maps.ohio.gov/image/rest/services/osip_most_current/ImageServer/exportImage?bbox=342716.794%2C4438082.224%2C342916.794%2C4438282.224&bboxSR=32617&imageSR=32617&size=540%2C540&format=jpg&f=image&interpolation=RSP_Bilinear"
        ],
        [
          "USGS imagery catalog at pin",
          "https://imagery.nationalmap.gov/arcgis/rest/services/USGSNAIPImagery/ImageServer/identify?geometry=%7B%22x%22%3A+-82.84349983%2C+%22y%22%3A+40.07925514%2C+%22spatialReference%22%3A+%7B%22wkid%22%3A+4326%7D%7D&geometryType=esriGeometryPoint&returnCatalogItems=true&maxItemCount=6&f=pjson"
        ]
      ]
    },
    "sources": [
      [
        "Franklin County Engineer utility application",
        "https://www.franklincountyengineer.org/wp-content/uploads/2016/04/Application-for-permit-pdf.pdf"
      ],
      [
        "New Albany ROW application and checklist",
        "https://newalbanyohio.org/right-of-way/"
      ],
      [
        "Official flowline layer",
        "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0"
      ]
    ]
  },
  {
    "id": "S0-W07",
    "segment": "Segment0",
    "feature": "S0-S011-Bore",
    "station": 18139.2,
    "name": "Morse Road unnamed drainage east of Big Walnut",
    "priority": "Asset and ROW",
    "method": "Carry a field and record trace. Add a separate trenchless crossing if it identifies a pipe or channel conflict.",
    "blocker": "No nearby inventory structure in the current 600-ft check. Need to locate the storm outlet or buried drainage and establish a dry receiving pit.",
    "lead": "Columbus Department of Public Service for street ROW and Columbus Water & Power/drainage owner for affected assets.",
    "conditional": "Local floodplain administrator and Huntington/Ohio EPA if delineated impacts warrant. Any non-ROW pit requires rights.",
    "submit": "Storm as-built tie, invert/utility survey, plan/profile, conduit method, dry access and city pavement restoration exhibit.",
    "fallback": "If the chosen pit hits a storm trunk or outlet, relocate it along permitted Morse frontage or shift to the opposite side after checking utility and traffic impacts.",
    "lat": 40.05629125,
    "lon": -82.88296779,
    "evidence": {
      "segment": "Segment0",
      "feature": "S0-S011-Bore",
      "station_ft": "18139.2",
      "latitude": "40.05629125",
      "longitude": "-82.88296779",
      "water_name": "",
      "layer_objectid": "21955",
      "water_fcode": "46003",
      "water_comid": "5213339",
      "water_permanent_id": "",
      "local_gis_angle_deg": "68.7",
      "county_place_township_screen": "FRANKLIN / COLUMBUS / BLENDON",
      "sampled_road_lead": "Morse CR-17",
      "sampled_issuer_lead": "City of Columbus – maintains street; Ch. 903 permit (county-numbered road; FCEO/DCEO only at county bridges)",
      "nearby_structure_inventory_leads": "",
      "parcel_ids_at_point": "",
      "corridor_parcel_ids_within_100ft": "Franklin:025-007634 | Franklin:025-007635 | Franklin:025-008474 | Franklin:600-171530 | Franklin:600-171531",
      "fema_at_point": "X AREA OF MINIMAL FLOOD HAZARD (39049C)",
      "nwi_within_100m": "Riverine R4SBC",
      "source_layer": "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0"
    },
    "review": {
      "classification": "gis",
      "confidence": "Unverified",
      "finding": "The mapped line meets wooded strips along Morse Road. The available leaf-off and summer imagery does not establish a continuous crossing or show a headwall. The ODOT search found no matched asset.",
      "next_check": "Trace the low ground and road inlets. Obtain the applicable Morse Road storm plan and stream mapping before carrying a special crossing.",
      "image": "img/water-pin-audit/S0-W07.jpg",
      "imagery_catalog_dates": "2023-05-21",
      "proof": [
        [
          "Official flowline 21955",
          "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0/query?objectIds=21955&outFields=%2A&returnGeometry=true&outSR=4326&f=pjson"
        ],
        [
          "Franklin SWCD stream verification",
          "https://www.franklinswcd.org/stream-verification-and-stream-resource-geodatabase"
        ],
        [
          "Original USDA NAIP aerial",
          "https://imagery.nationalmap.gov/arcgis/rest/services/USGSNAIPImagery/ImageServer/exportImage?bbox=339297.468%2C4435603.676%2C339497.468%2C4435803.676&bboxSR=32617&imageSR=32617&size=540%2C540&format=jpg&f=image&interpolation=RSP_Bilinear"
        ],
        [
          "Ohio statewide aerial",
          "https://maps.ohio.gov/image/rest/services/osip_most_current/ImageServer/exportImage?bbox=339297.468%2C4435603.676%2C339497.468%2C4435803.676&bboxSR=32617&imageSR=32617&size=540%2C540&format=jpg&f=image&interpolation=RSP_Bilinear"
        ],
        [
          "USGS imagery catalog at pin",
          "https://imagery.nationalmap.gov/arcgis/rest/services/USGSNAIPImagery/ImageServer/identify?geometry=%7B%22x%22%3A+-82.88296779%2C+%22y%22%3A+40.05629125%2C+%22spatialReference%22%3A+%7B%22wkid%22%3A+4326%7D%7D&geometryType=esriGeometryPoint&returnCatalogItems=true&maxItemCount=6&f=pjson"
        ],
        [
          "ODOT nearby bridge inventory query",
          "https://tims.dot.state.oh.us/ags/rest/services/Assets/Bridge_Inventory/MapServer/0/query?where=1%3D1&geometry=-82.88472824%2C40.05494378%2C-82.88120734%2C40.05763872&geometryType=esriGeometryEnvelope&inSR=4326&outFields=%2A&returnGeometry=true&outSR=4326&f=pjson"
        ],
        [
          "ODOT nearby conduit inventory query",
          "https://tims.dot.state.oh.us/ags/rest/services/Assets/Conduit_Inventory/MapServer/0/query?where=1%3D1&geometry=-82.88472824%2C40.05494378%2C-82.88120734%2C40.05763872&geometryType=esriGeometryEnvelope&inSR=4326&outFields=%2A&returnGeometry=true&outSR=4326&f=pjson"
        ]
      ]
    },
    "sources": [
      [
        "Columbus Chapter 903 utility ROW rules",
        "https://columbus.legistar.com/LegislationDetail.aspx?FullText=1&GUID=3522B4CF-33A3-4278-A9E9-EED1F2325E6E&ID=7480234"
      ],
      [
        "Official flowline layer",
        "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0"
      ]
    ]
  },
  {
    "id": "S0-W08",
    "segment": "Segment0",
    "feature": "S0-S012-Water",
    "station": 167.8,
    "name": "Big Walnut Creek at Morse Road",
    "priority": "Major crossing",
    "method": "Near-perpendicular HDD with upland rig and pit locations.",
    "blocker": "AE floodway, forested wetland screening and bridge 2530872 about 42 ft away. Need dry legal work areas, scour and geotechnical feasibility.",
    "lead": "Columbus for street work. Franklin County Engineer for SFN 2530872 structure and county bridge envelope. Seek bridge owner approval only for attachment or affected works.",
    "conditional": "Local floodplain administrator for actual work areas. Huntington Regulatory, Ohio EPA and private/park landowner where triggered.",
    "submit": "Bridge and ROW survey, bed/scour profile, geotechnical and wetland exhibits, drilling fluid response, full pit/access placement, authority and property limits.",
    "fallback": "If HDD staging is denied, evaluate owner-approved duct/attachment with work access out of the wetland. If the structure cannot be used, compare a longer bore or authorized road-side landfall.",
    "lat": 40.05657282,
    "lon": -82.88852146,
    "evidence": {
      "segment": "Segment0",
      "feature": "S0-S012-Water",
      "station_ft": "167.8",
      "latitude": "40.05657282",
      "longitude": "-82.88852146",
      "water_name": "Big Walnut Creek",
      "layer_objectid": "21956",
      "water_fcode": "46006",
      "water_comid": "5213341",
      "water_permanent_id": "",
      "local_gis_angle_deg": "88.4",
      "county_place_township_screen": "FRANKLIN / COLUMBUS / BLENDON",
      "sampled_road_lead": "Morse CR-17",
      "sampled_issuer_lead": "City of Columbus – maintains street; Ch. 903 permit (county-numbered road; FCEO/DCEO only at county bridges)",
      "nearby_structure_inventory_leads": "2530872 @ 42 ft (MORSE RD. / BIG WALNUT CREEK, maintain code 02)",
      "parcel_ids_at_point": "",
      "corridor_parcel_ids_within_100ft": "Franklin:025-010853 | Franklin:600-168457 | Franklin:VNP-WATER",
      "fema_at_point": "AE FLOODWAY (39049C)",
      "nwi_within_100m": "Freshwater Forested/Shrub Wetland PFO1C | Riverine R2UBH | Riverine R5UBH",
      "source_layer": "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0"
    },
    "review": {
      "classification": "open",
      "confidence": "High",
      "finding": "Big Walnut Creek and both banks are visible at the Morse Road bridge. ODOT SFN 2530872 is about 42 ft from the pin.",
      "next_check": "Survey banks, bed, foundations and work limits in the mapped floodway. Tie each pit to legal access before selecting HDD.",
      "image": "img/water-pin-audit/S0-W08.jpg",
      "imagery_catalog_dates": "2023-05-21",
      "proof": [
        [
          "Official flowline 21956",
          "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0/query?objectIds=21956&outFields=%2A&returnGeometry=true&outSR=4326&f=pjson"
        ],
        [
          "ODOT structure 2530872",
          "https://tims.dot.state.oh.us/ags/rest/services/Assets/Bridge_Inventory/MapServer/0/query?where=SFN+IN+%28%272530872%27%29&outFields=SFN%2CSTR_LOC_CARRIED%2CINVENT_FEAT%2CMAIN_STR_TYPE_CD%2CCULVERT_LEN%2CMAINT_RESP_CD&returnGeometry=true&outSR=4326&f=pjson"
        ],
        [
          "Original USDA NAIP aerial",
          "https://imagery.nationalmap.gov/arcgis/rest/services/USGSNAIPImagery/ImageServer/exportImage?bbox=338824.417%2C4435644.968%2C339024.417%2C4435844.968&bboxSR=32617&imageSR=32617&size=540%2C540&format=jpg&f=image&interpolation=RSP_Bilinear"
        ],
        [
          "Ohio statewide aerial",
          "https://maps.ohio.gov/image/rest/services/osip_most_current/ImageServer/exportImage?bbox=338824.417%2C4435644.968%2C339024.417%2C4435844.968&bboxSR=32617&imageSR=32617&size=540%2C540&format=jpg&f=image&interpolation=RSP_Bilinear"
        ],
        [
          "USGS imagery catalog at pin",
          "https://imagery.nationalmap.gov/arcgis/rest/services/USGSNAIPImagery/ImageServer/identify?geometry=%7B%22x%22%3A+-82.88852146%2C+%22y%22%3A+40.05657282%2C+%22spatialReference%22%3A+%7B%22wkid%22%3A+4326%7D%7D&geometryType=esriGeometryPoint&returnCatalogItems=true&maxItemCount=6&f=pjson"
        ]
      ]
    },
    "sources": [
      [
        "Columbus Chapter 903 utility ROW rules",
        "https://columbus.legistar.com/LegislationDetail.aspx?FullText=1&GUID=3522B4CF-33A3-4278-A9E9-EED1F2325E6E&ID=7480234"
      ],
      [
        "Franklin County Engineer utility application",
        "https://www.franklincountyengineer.org/wp-content/uploads/2016/04/Application-for-permit-pdf.pdf"
      ],
      [
        "Official flowline layer",
        "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0"
      ]
    ]
  },
  {
    "id": "S0-W09",
    "segment": "Segment0",
    "feature": "S0-S016-Water",
    "station": 163.9,
    "name": "Alum Creek at Morse Road",
    "priority": "Major crossing",
    "method": "Compare existing-side HDD with a surveyed road-side shift before pricing.",
    "blocker": "AE floodway, tax parcel 010-148992 at the hit and no public road assignment there. SFN 2535874 lies about 70 ft away. Need both pit rights and bridge/park limits.",
    "lead": "Franklin County Engineer for bridge and county structure. Columbus Public Service for road-side work and Columbus or other actual property controller for off-ROW occupation.",
    "conditional": "Local floodplain administrator and water agencies for regulated effects. Trail or parks staff if work uses their land or affects public access.",
    "submit": "Compare both routes with same tie-ins, surveyed road and trail limits, parcel instrument, bank/scour and foundation envelope, temporary access, bore profile and traffic impacts.",
    "fallback": "If original land access is denied, pursue the verified roadway-side shift. If its pits or foundations do not fit, check accepted bridge duct/attachment. If that is denied, seek a different surveyed landfall with rights.",
    "lat": 40.05836173,
    "lon": -82.92442546,
    "evidence": {
      "segment": "Segment0",
      "feature": "S0-S016-Water",
      "station_ft": "163.9",
      "latitude": "40.05836173",
      "longitude": "-82.92442546",
      "water_name": "Alum Creek",
      "layer_objectid": "21947",
      "water_fcode": "46006",
      "water_comid": "5213323",
      "water_permanent_id": "",
      "local_gis_angle_deg": "89.0",
      "county_place_township_screen": "FRANKLIN / COLUMBUS / BLENDON",
      "sampled_road_lead": "",
      "sampled_issuer_lead": "No public road within screen (cross-country / private / unverified)",
      "nearby_structure_inventory_leads": "2535874 @ 70 ft (MORSE RD / ALUM CREEK (MORSE), maintain code 02)",
      "parcel_ids_at_point": "Franklin:010-148992",
      "corridor_parcel_ids_within_100ft": "Franklin:010-014172 | Franklin:010-148992 | Franklin:010-242734",
      "fema_at_point": "AE FLOODWAY (39049C)",
      "nwi_within_100m": "Riverine R2UBH | Riverine R5UBH",
      "source_layer": "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0"
    },
    "review": {
      "classification": "open",
      "confidence": "High",
      "finding": "Alum Creek is visible on both sides of Morse Road. The crossing matches bridge 2535874, about 70 ft from the pin. The GIS pin falls within a mapped floodway.",
      "next_check": "Confirm bank and foundation limits, floodway work limits and access at the west approach. Compare the HDD and approved duct paths.",
      "image": "img/water-pin-audit/S0-W09.jpg",
      "imagery_catalog_dates": "2023-05-21",
      "proof": [
        [
          "Official flowline 21947",
          "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0/query?objectIds=21947&outFields=%2A&returnGeometry=true&outSR=4326&f=pjson"
        ],
        [
          "ODOT structure 2535874",
          "https://tims.dot.state.oh.us/ags/rest/services/Assets/Bridge_Inventory/MapServer/0/query?where=SFN+IN+%28%272535874%27%29&outFields=SFN%2CSTR_LOC_CARRIED%2CINVENT_FEAT%2CMAIN_STR_TYPE_CD%2CCULVERT_LEN%2CMAINT_RESP_CD&returnGeometry=true&outSR=4326&f=pjson"
        ],
        [
          "Original USDA NAIP aerial",
          "https://imagery.nationalmap.gov/arcgis/rest/services/USGSNAIPImagery/ImageServer/exportImage?bbox=335766.192%2C4435909.145%2C335966.192%2C4436109.145&bboxSR=32617&imageSR=32617&size=540%2C540&format=jpg&f=image&interpolation=RSP_Bilinear"
        ],
        [
          "Ohio statewide aerial",
          "https://maps.ohio.gov/image/rest/services/osip_most_current/ImageServer/exportImage?bbox=335766.192%2C4435909.145%2C335966.192%2C4436109.145&bboxSR=32617&imageSR=32617&size=540%2C540&format=jpg&f=image&interpolation=RSP_Bilinear"
        ],
        [
          "USGS imagery catalog at pin",
          "https://imagery.nationalmap.gov/arcgis/rest/services/USGSNAIPImagery/ImageServer/identify?geometry=%7B%22x%22%3A+-82.92442546%2C+%22y%22%3A+40.05836173%2C+%22spatialReference%22%3A+%7B%22wkid%22%3A+4326%7D%7D&geometryType=esriGeometryPoint&returnCatalogItems=true&maxItemCount=6&f=pjson"
        ]
      ]
    },
    "sources": [
      [
        "Columbus Chapter 903 utility ROW rules",
        "https://columbus.legistar.com/LegislationDetail.aspx?FullText=1&GUID=3522B4CF-33A3-4278-A9E9-EED1F2325E6E&ID=7480234"
      ],
      [
        "Franklin County Engineer utility application",
        "https://www.franklincountyengineer.org/wp-content/uploads/2016/04/Application-for-permit-pdf.pdf"
      ],
      [
        "Official flowline layer",
        "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0"
      ]
    ]
  },
  {
    "id": "S0-W10",
    "segment": "Segment0",
    "feature": "S0-S017-Bore",
    "station": 926.0,
    "name": "Morse Road tributary near Alum Creek",
    "priority": "Asset and ROW",
    "method": "Separate short bore clear of SFN 2535858. Compare combined mobilization with Alum Creek.",
    "blocker": "Structure point is about 51 ft away. Need actual tributary opening, foundations and utilities to see whether the Alum and tributary profiles can share access.",
    "lead": "Columbus street permit and Franklin County Engineer structure review where work affects SFN 2535858.",
    "conditional": "Owner of any outlet or storm line, local floodplain and Ohio water agencies as triggered by approach effects.",
    "submit": "Survey both sites on one exhibit, structure/pit spacing, two bore profiles and optional shared access, staging and restoration footprint.",
    "fallback": "If combined access or a longer shot is rejected, retain separate short profiles and position both pits outside structure, utility and channel limits.",
    "lat": 40.0585113,
    "lon": -82.92836056,
    "evidence": {
      "segment": "Segment0",
      "feature": "S0-S017-Bore",
      "station_ft": "926.0",
      "latitude": "40.0585113",
      "longitude": "-82.92836056",
      "water_name": "",
      "layer_objectid": "21946",
      "water_fcode": "46003",
      "water_comid": "5213321",
      "water_permanent_id": "",
      "local_gis_angle_deg": "65.9",
      "county_place_township_screen": "FRANKLIN / COLUMBUS / BLENDON",
      "sampled_road_lead": "Morse CR-17",
      "sampled_issuer_lead": "City of Columbus – maintains street; Ch. 903 permit (county-numbered road; FCEO/DCEO only at county bridges)",
      "nearby_structure_inventory_leads": "2535858 @ 51 ft (MORSE ROAD / TRIBUTARY (MORSE ROAD), maintain code 02)",
      "parcel_ids_at_point": "",
      "corridor_parcel_ids_within_100ft": "Franklin:010-255453 | Franklin:115-158434",
      "fema_at_point": "X AREA OF MINIMAL FLOOD HAZARD (39049C)",
      "nwi_within_100m": "Riverine R4SBC",
      "source_layer": "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0"
    },
    "review": {
      "classification": "buried",
      "confidence": "High",
      "finding": "ODOT lists a 108-ft culvert, SFN 2535858, on Morse Road about 51 ft from the pin. It matches this low corridor east of the separate Alum Creek bridge. Tree cover masks the barrel ends.",
      "next_check": "Survey headwalls, aprons, inverts and nearby utilities. Keep the route independent of the culvert and preserve drainage access.",
      "image": "img/water-pin-audit/S0-W10.jpg",
      "imagery_catalog_dates": "2023-05-21",
      "proof": [
        [
          "Official flowline 21946",
          "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0/query?objectIds=21946&outFields=%2A&returnGeometry=true&outSR=4326&f=pjson"
        ],
        [
          "ODOT structure 2535858",
          "https://tims.dot.state.oh.us/ags/rest/services/Assets/Bridge_Inventory/MapServer/0/query?where=SFN+IN+%28%272535858%27%29&outFields=SFN%2CSTR_LOC_CARRIED%2CINVENT_FEAT%2CMAIN_STR_TYPE_CD%2CCULVERT_LEN%2CMAINT_RESP_CD&returnGeometry=true&outSR=4326&f=pjson"
        ],
        [
          "Original USDA NAIP aerial",
          "https://imagery.nationalmap.gov/arcgis/rest/services/USGSNAIPImagery/ImageServer/exportImage?bbox=335430.906%2C4435933.013%2C335630.906%2C4436133.013&bboxSR=32617&imageSR=32617&size=540%2C540&format=jpg&f=image&interpolation=RSP_Bilinear"
        ],
        [
          "Ohio statewide aerial",
          "https://maps.ohio.gov/image/rest/services/osip_most_current/ImageServer/exportImage?bbox=335430.906%2C4435933.013%2C335630.906%2C4436133.013&bboxSR=32617&imageSR=32617&size=540%2C540&format=jpg&f=image&interpolation=RSP_Bilinear"
        ],
        [
          "USGS imagery catalog at pin",
          "https://imagery.nationalmap.gov/arcgis/rest/services/USGSNAIPImagery/ImageServer/identify?geometry=%7B%22x%22%3A+-82.92836056%2C+%22y%22%3A+40.0585113%2C+%22spatialReference%22%3A+%7B%22wkid%22%3A+4326%7D%7D&geometryType=esriGeometryPoint&returnCatalogItems=true&maxItemCount=6&f=pjson"
        ]
      ]
    },
    "sources": [
      [
        "Columbus Chapter 903 utility ROW rules",
        "https://columbus.legistar.com/LegislationDetail.aspx?FullText=1&GUID=3522B4CF-33A3-4278-A9E9-EED1F2325E6E&ID=7480234"
      ],
      [
        "Franklin County Engineer utility application",
        "https://www.franklincountyengineer.org/wp-content/uploads/2016/04/Application-for-permit-pdf.pdf"
      ],
      [
        "Official flowline layer",
        "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0"
      ]
    ]
  },
  {
    "id": "S0-W11",
    "segment": "Segment0",
    "feature": "S0-S023-Bore",
    "station": 2668.6,
    "name": "Sancus Boulevard drainage OID 21911",
    "priority": "Project coordination",
    "method": "Carry the ordinary road bore pending the storm-plan overlay. Adjust angle and clearance if the overlay confirms a conflict.",
    "blocker": "Existing hit is only about 49° to the mapped channel. Sancus project grading, storm plans and future easements can move the useful work envelope.",
    "lead": "Columbus Public Service and Sancus capital project team for city ROW and future drainage fit.",
    "conditional": "Columbus drainage utility, property interests, local floodplain and Ohio water approvals as impacts require.",
    "submit": "Overlay capital project plans, survey channel/storm utilities, angle comparison, pit rights and dates, with revised cut/restoration and traffic plan.",
    "fallback": "If the near-normal shift is refused, test an alternate road side or schedule after storm construction. A broad bypass needs its own crossing overlay and approvals.",
    "lat": 40.11887664,
    "lon": -82.99535789,
    "evidence": {
      "segment": "Segment0",
      "feature": "S0-S023-Bore",
      "station_ft": "2668.6",
      "latitude": "40.11887664",
      "longitude": "-82.99535789",
      "water_name": "",
      "layer_objectid": "21911",
      "water_fcode": "46003",
      "water_comid": "5213251",
      "water_permanent_id": "",
      "local_gis_angle_deg": "49.4",
      "county_place_township_screen": "FRANKLIN / COLUMBUS / SHARON",
      "sampled_road_lead": "Sancus MR-4354",
      "sampled_issuer_lead": "City of Columbus",
      "nearby_structure_inventory_leads": "",
      "parcel_ids_at_point": "",
      "corridor_parcel_ids_within_100ft": "Franklin:610-216016 | Franklin:610-252425 | Franklin:610-255897",
      "fema_at_point": "X AREA OF MINIMAL FLOOD HAZARD (39049C)",
      "nwi_within_100m": "Riverine R4SBC",
      "source_layer": "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0"
    },
    "review": {
      "classification": "gis",
      "confidence": "Unverified",
      "finding": "Flowline 21911 meets a paved, signalized area on Sancus. Neither aerial establishes a crossing at the pin and no ODOT asset matches. The Columbus corridor project includes storm sewer work.",
      "next_check": "Get the existing and proposed Columbus storm sheets. Trace inlets and mains to the route and adjust a road bore if a conflict is found.",
      "image": "img/water-pin-audit/S0-W11.jpg",
      "imagery_catalog_dates": "2023-05-21",
      "proof": [
        [
          "Official flowline 21911",
          "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0/query?objectIds=21911&outFields=%2A&returnGeometry=true&outSR=4326&f=pjson"
        ],
        [
          "Columbus Sancus Boulevard project context",
          "https://engage.columbus.gov/sancusboulevardimprovements"
        ],
        [
          "Columbus stormwater mapping and record requests",
          "https://www.columbus.gov/Services/Columbus-Water-Power/Information-for-Customers/Water-Power-Contractors/Stormwater-Drainage-Manual"
        ],
        [
          "Original USDA NAIP aerial",
          "https://imagery.nationalmap.gov/arcgis/rest/services/USGSNAIPImagery/ImageServer/exportImage?bbox=329866.673%2C4442759.758%2C330066.673%2C4442959.758&bboxSR=32617&imageSR=32617&size=540%2C540&format=jpg&f=image&interpolation=RSP_Bilinear"
        ],
        [
          "Ohio statewide aerial",
          "https://maps.ohio.gov/image/rest/services/osip_most_current/ImageServer/exportImage?bbox=329866.673%2C4442759.758%2C330066.673%2C4442959.758&bboxSR=32617&imageSR=32617&size=540%2C540&format=jpg&f=image&interpolation=RSP_Bilinear"
        ],
        [
          "USGS imagery catalog at pin",
          "https://imagery.nationalmap.gov/arcgis/rest/services/USGSNAIPImagery/ImageServer/identify?geometry=%7B%22x%22%3A+-82.99535789%2C+%22y%22%3A+40.11887664%2C+%22spatialReference%22%3A+%7B%22wkid%22%3A+4326%7D%7D&geometryType=esriGeometryPoint&returnCatalogItems=true&maxItemCount=6&f=pjson"
        ],
        [
          "ODOT nearby bridge inventory query",
          "https://tims.dot.state.oh.us/ags/rest/services/Assets/Bridge_Inventory/MapServer/0/query?where=1%3D1&geometry=-82.99711995%2C40.11752917%2C-82.99359583%2C40.12022411&geometryType=esriGeometryEnvelope&inSR=4326&outFields=%2A&returnGeometry=true&outSR=4326&f=pjson"
        ],
        [
          "ODOT nearby conduit inventory query",
          "https://tims.dot.state.oh.us/ags/rest/services/Assets/Conduit_Inventory/MapServer/0/query?where=1%3D1&geometry=-82.99711995%2C40.11752917%2C-82.99359583%2C40.12022411&geometryType=esriGeometryEnvelope&inSR=4326&outFields=%2A&returnGeometry=true&outSR=4326&f=pjson"
        ]
      ]
    },
    "sources": [
      [
        "Columbus Chapter 903 utility ROW rules",
        "https://columbus.legistar.com/LegislationDetail.aspx?FullText=1&GUID=3522B4CF-33A3-4278-A9E9-EED1F2325E6E&ID=7480234"
      ],
      [
        "Columbus Sancus Boulevard improvements",
        "https://engage.columbus.gov/sancusboulevardimprovements"
      ],
      [
        "Official flowline layer",
        "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0"
      ]
    ]
  },
  {
    "id": "S0-W12",
    "segment": "Segment0",
    "feature": "S0-S023-Bore",
    "station": 6328.2,
    "name": "Sancus Boulevard pond or outlet drainage OID 24959",
    "priority": "Project coordination",
    "method": "Trace the drainage and pond outlet before committing to an independent bore or pit restrictions specific to an outlet.",
    "blocker": "Second Sancus hit. Pond and riverine NWI indicators nearby, FEMA request unavailable. Need ditch/outlet identity, capital project limits and permitted pit access.",
    "lead": "Columbus Public Service and the stormwater/drainage asset controller. Coordinate both Sancus projects for work limits and timing.",
    "conditional": "Local floodplain review after getting effective mapping. Huntington/Ohio EPA if delineated impacts trigger them.",
    "submit": "Pond/outfall and storm as-built, FIRM, combined Sancus project overlay, maintenance easement, bore/pits and a separate work station exhibit.",
    "fallback": "If the outlet buffer or easement prevents the current bore, shift the landfall within authorized ROW or coordinate an owner-approved storm-project window. Keep this crossing quantity separate.",
    "lat": 40.12855953,
    "lon": -82.99336231,
    "evidence": {
      "segment": "Segment0",
      "feature": "S0-S023-Bore",
      "station_ft": "6328.2",
      "latitude": "40.12855953",
      "longitude": "-82.99336231",
      "water_name": "",
      "layer_objectid": "24959",
      "water_fcode": "46003",
      "water_comid": "5213239",
      "water_permanent_id": "",
      "local_gis_angle_deg": "78.3",
      "county_place_township_screen": "FRANKLIN / COLUMBUS / SHARON",
      "sampled_road_lead": "Sancus MR-4354",
      "sampled_issuer_lead": "City of Columbus",
      "nearby_structure_inventory_leads": "",
      "parcel_ids_at_point": "",
      "corridor_parcel_ids_within_100ft": "Franklin:610-222402 | Franklin:610-329246 | Franklin:610-329247 | Franklin:610-329248 | Franklin:610-329249 | Franklin:610-329250 | Franklin:610-329251 | Franklin:610-329252 | Franklin:610-329253 | Franklin:610-329254 | Franklin:610-329255 | Franklin:610-329256 | Franklin:610-329257 | Franklin:610-329258 | Franklin:610-329259 | Franklin:610-329260 | Franklin:610-329261",
      "fema_at_point": "Unavailable",
      "nwi_within_100m": "Freshwater Pond PUBGx | Riverine R4SBC",
      "source_layer": "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0"
    },
    "review": {
      "classification": "gis",
      "confidence": "Unverified",
      "finding": "Flowline 24959 reaches Sancus in a developed corridor. A pond is visible behind development east of the road. Its outlet route and any barrel through the street are unverified.",
      "next_check": "Compare municipal and subdivision storm plans and trace outlet and street inlets. Carry a pond connection only after the plans or inspection tie it to the route.",
      "image": "img/water-pin-audit/S0-W12.jpg",
      "imagery_catalog_dates": "2023-05-21",
      "proof": [
        [
          "Official flowline 24959",
          "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0/query?objectIds=24959&outFields=%2A&returnGeometry=true&outSR=4326&f=pjson"
        ],
        [
          "Columbus Sancus Boulevard project context",
          "https://engage.columbus.gov/sancusboulevardimprovements"
        ],
        [
          "Columbus stormwater mapping and record requests",
          "https://www.columbus.gov/Services/Columbus-Water-Power/Information-for-Customers/Water-Power-Contractors/Stormwater-Drainage-Manual"
        ],
        [
          "Original USDA NAIP aerial",
          "https://imagery.nationalmap.gov/arcgis/rest/services/USGSNAIPImagery/ImageServer/exportImage?bbox=330060.846%2C4443830.782%2C330260.846%2C4444030.782&bboxSR=32617&imageSR=32617&size=540%2C540&format=jpg&f=image&interpolation=RSP_Bilinear"
        ],
        [
          "Ohio statewide aerial",
          "https://maps.ohio.gov/image/rest/services/osip_most_current/ImageServer/exportImage?bbox=330060.846%2C4443830.782%2C330260.846%2C4444030.782&bboxSR=32617&imageSR=32617&size=540%2C540&format=jpg&f=image&interpolation=RSP_Bilinear"
        ],
        [
          "USGS imagery catalog at pin",
          "https://imagery.nationalmap.gov/arcgis/rest/services/USGSNAIPImagery/ImageServer/identify?geometry=%7B%22x%22%3A+-82.99336231%2C+%22y%22%3A+40.12855953%2C+%22spatialReference%22%3A+%7B%22wkid%22%3A+4326%7D%7D&geometryType=esriGeometryPoint&returnCatalogItems=true&maxItemCount=6&f=pjson"
        ],
        [
          "ODOT nearby bridge inventory query",
          "https://tims.dot.state.oh.us/ags/rest/services/Assets/Bridge_Inventory/MapServer/0/query?where=1%3D1&geometry=-82.99512463%2C40.12721206%2C-82.99159999%2C40.12990700&geometryType=esriGeometryEnvelope&inSR=4326&outFields=%2A&returnGeometry=true&outSR=4326&f=pjson"
        ],
        [
          "ODOT nearby conduit inventory query",
          "https://tims.dot.state.oh.us/ags/rest/services/Assets/Conduit_Inventory/MapServer/0/query?where=1%3D1&geometry=-82.99512463%2C40.12721206%2C-82.99159999%2C40.12990700&geometryType=esriGeometryEnvelope&inSR=4326&outFields=%2A&returnGeometry=true&outSR=4326&f=pjson"
        ]
      ]
    },
    "sources": [
      [
        "Columbus Chapter 903 utility ROW rules",
        "https://columbus.legistar.com/LegislationDetail.aspx?FullText=1&GUID=3522B4CF-33A3-4278-A9E9-EED1F2325E6E&ID=7480234"
      ],
      [
        "Columbus Sancus Boulevard improvements",
        "https://engage.columbus.gov/sancusboulevardimprovements"
      ],
      [
        "Official flowline layer",
        "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0"
      ]
    ]
  },
  {
    "id": "S0-W13",
    "segment": "Segment0",
    "feature": "S0-S025-Bore",
    "station": 2693.0,
    "name": "Lazelle Road drainage near the county line",
    "priority": "Asset and ROW",
    "method": "Locate the ditch, pipe or storm connection before using the mapped angle to realign the bore.",
    "blocker": "About 46° on the mapped perennial line, near a road-control transition and mapped pond. FEMA response is unavailable. Ownership and outlet/pit positions remain open.",
    "lead": "Columbus Public Service starts road control check. Delaware County/Orange and actual drainage owner confirm applicable road segments and permit roles.",
    "conditional": "Local floodplain and Huntington/Ohio EPA as triggered. Access right holder if there is a frontage easement or private work.",
    "submit": "Road maintenance boundary and parcel sheets, surveyed outlet/channel and utilities, FIRM, both proposed pit locations and revised profile.",
    "fallback": "If jurisdiction or pond work blocks the chosen side, shift to a surveyed adjacent public corridor away from the outlet, or secure a documented frontage easement.",
    "lat": 40.13675263,
    "lon": -83.0154464,
    "evidence": {
      "segment": "Segment0",
      "feature": "S0-S025-Bore",
      "station_ft": "2693.0",
      "latitude": "40.13675263",
      "longitude": "-83.0154464",
      "water_name": "",
      "layer_objectid": "22645",
      "water_fcode": "46006",
      "water_comid": "5214965",
      "water_permanent_id": "",
      "local_gis_angle_deg": "45.5",
      "county_place_township_screen": "DELAWARE / COLUMBUS / ORANGE",
      "sampled_road_lead": "Lazelle CR-21",
      "sampled_issuer_lead": "City of Columbus – maintains street; Ch. 903 permit (county-numbered road; FCEO/DCEO only at county bridges)",
      "nearby_structure_inventory_leads": "",
      "parcel_ids_at_point": "Delaware:999999-0 (OID 98686)",
      "corridor_parcel_ids_within_100ft": "Delaware:318343-0 (OID 28605) | Delaware:999999-0 (OID 98686) | Franklin:255-268865 | Franklin:610-200937",
      "fema_at_point": "Unavailable",
      "nwi_within_100m": "Freshwater Pond PUBFh | Riverine R5UBH",
      "source_layer": "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0"
    },
    "review": {
      "classification": "gis",
      "confidence": "Unverified",
      "finding": "The flowline reaches Lazelle Road at a wooded edge and continues into developed lots south of the road. A swale is possible. No same-site barrel or defined surface passage was found in the images or inventory.",
      "next_check": "Check road and subdivision grading sheets and trace the ditch or storm pipe on both sides. Screen the nearby wetland against the final work limits.",
      "image": "img/water-pin-audit/S0-W13.jpg",
      "imagery_catalog_dates": "2023-05-21",
      "proof": [
        [
          "Official flowline 22645",
          "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0/query?objectIds=22645&outFields=%2A&returnGeometry=true&outSR=4326&f=pjson"
        ],
        [
          "Franklin SWCD stream verification",
          "https://www.franklinswcd.org/stream-verification-and-stream-resource-geodatabase"
        ],
        [
          "Columbus stormwater mapping and record requests",
          "https://www.columbus.gov/Services/Columbus-Water-Power/Information-for-Customers/Water-Power-Contractors/Stormwater-Drainage-Manual"
        ],
        [
          "Original USDA NAIP aerial",
          "https://imagery.nationalmap.gov/arcgis/rest/services/USGSNAIPImagery/ImageServer/exportImage?bbox=328199.726%2C4444782.699%2C328399.726%2C4444982.699&bboxSR=32617&imageSR=32617&size=540%2C540&format=jpg&f=image&interpolation=RSP_Bilinear"
        ],
        [
          "Ohio statewide aerial",
          "https://maps.ohio.gov/image/rest/services/osip_most_current/ImageServer/exportImage?bbox=328199.726%2C4444782.699%2C328399.726%2C4444982.699&bboxSR=32617&imageSR=32617&size=540%2C540&format=jpg&f=image&interpolation=RSP_Bilinear"
        ],
        [
          "USGS imagery catalog at pin",
          "https://imagery.nationalmap.gov/arcgis/rest/services/USGSNAIPImagery/ImageServer/identify?geometry=%7B%22x%22%3A+-83.0154464%2C+%22y%22%3A+40.13675263%2C+%22spatialReference%22%3A+%7B%22wkid%22%3A+4326%7D%7D&geometryType=esriGeometryPoint&returnCatalogItems=true&maxItemCount=6&f=pjson"
        ],
        [
          "ODOT nearby bridge inventory query",
          "https://tims.dot.state.oh.us/ags/rest/services/Assets/Bridge_Inventory/MapServer/0/query?where=1%3D1&geometry=-83.01720893%2C40.13540516%2C-83.01368387%2C40.13810010&geometryType=esriGeometryEnvelope&inSR=4326&outFields=%2A&returnGeometry=true&outSR=4326&f=pjson"
        ],
        [
          "ODOT nearby conduit inventory query",
          "https://tims.dot.state.oh.us/ags/rest/services/Assets/Conduit_Inventory/MapServer/0/query?where=1%3D1&geometry=-83.01720893%2C40.13540516%2C-83.01368387%2C40.13810010&geometryType=esriGeometryEnvelope&inSR=4326&outFields=%2A&returnGeometry=true&outSR=4326&f=pjson"
        ]
      ]
    },
    "sources": [
      [
        "Columbus Chapter 903 utility ROW rules",
        "https://columbus.legistar.com/LegislationDetail.aspx?FullText=1&GUID=3522B4CF-33A3-4278-A9E9-EED1F2325E6E&ID=7480234"
      ],
      [
        "Delaware County utility and ROW permits",
        "https://engineer.co.delaware.oh.us/permits/"
      ],
      [
        "Official flowline layer",
        "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0"
      ]
    ]
  },
  {
    "id": "S0-W14",
    "segment": "Segment0",
    "feature": "S0-S025-Bore",
    "station": 10909.5,
    "name": "US-23 corridor unnamed intermittent drainage",
    "priority": "Asset and ROW",
    "method": "Confirm state ROW and trace US 23 frontage drainage before carrying a drainage-specific crossing.",
    "blocker": "The route sample has no road assignment. Need to locate the pipe/ditch and prove state ROW or off-road title, access and pit positions. FEMA lookup unavailable.",
    "lead": "ODOT D6 Utility Coordinator and drainage staff if the work occupies state ROW or drainage. Actual property owner or local road controller if outside.",
    "conditional": "Local floodplain and Ohio water review from work limits. Written property instrument where required for state telecom occupancy.",
    "submit": "State ROW and access-control sheets, alternative private rights exhibits, drainage pipe/ditch/utility profile and pit locations. Add parcel and FIRM verification.",
    "fallback": "If state occupancy is refused, shift into an authorized frontage or seek a permitted private corridor. US23-B still hits OID 22608, so it needs a crossing plan too.",
    "lat": 40.15799426,
    "lon": -83.01888098,
    "evidence": {
      "segment": "Segment0",
      "feature": "S0-S025-Bore",
      "station_ft": "10909.5",
      "latitude": "40.15799426",
      "longitude": "-83.01888098",
      "water_name": "",
      "layer_objectid": "22608",
      "water_fcode": "46003",
      "water_comid": "5214885",
      "water_permanent_id": "",
      "local_gis_angle_deg": "53.3",
      "county_place_township_screen": "DELAWARE / unincorp. or blank / ORANGE",
      "sampled_road_lead": "",
      "sampled_issuer_lead": "No public road within screen (cross-country / private / unverified)",
      "nearby_structure_inventory_leads": "",
      "parcel_ids_at_point": "Delaware:999999-0 (OID 98682)",
      "corridor_parcel_ids_within_100ft": "Delaware:318324-0 (OID 99928) | Delaware:999999-0 (OID 98682)",
      "fema_at_point": "Unavailable",
      "nwi_within_100m": "Riverine R4SBC",
      "source_layer": "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0"
    },
    "review": {
      "classification": "gis",
      "confidence": "Unverified",
      "finding": "The hit is at US 23 frontage beside development and a grass strip. The nearest candidate ODOT conduit is on SR 750 about 354 ft away. Neither aerial ties that conduit or an open channel to this pin.",
      "next_check": "Get ODOT US 23 drainage and ROW plans and follow the ditch/inlets through the frontage. Verify the SR 750 conduit separately if work reaches it.",
      "image": "img/water-pin-audit/S0-W14.jpg",
      "imagery_catalog_dates": "2023-05-21",
      "proof": [
        [
          "Official flowline 22608",
          "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0/query?objectIds=22608&outFields=%2A&returnGeometry=true&outSR=4326&f=pjson"
        ],
        [
          "ODOT conduit 1875214",
          "https://tims.dot.state.oh.us/ags/rest/services/Assets/Conduit_Inventory/MapServer/0/query?where=CULVERT_FILE_NUMBER%3D1875214&outFields=%2A&returnGeometry=true&outSR=4326&f=pjson"
        ],
        [
          "ODOT utility occupancy and district intake",
          "https://www.transportation.ohio.gov/business/permits/row-permits"
        ],
        [
          "Original USDA NAIP aerial",
          "https://imagery.nationalmap.gov/arcgis/rest/services/USGSNAIPImagery/ImageServer/exportImage?bbox=327960.698%2C4447147.265%2C328160.698%2C4447347.265&bboxSR=32617&imageSR=32617&size=540%2C540&format=jpg&f=image&interpolation=RSP_Bilinear"
        ],
        [
          "Ohio statewide aerial",
          "https://maps.ohio.gov/image/rest/services/osip_most_current/ImageServer/exportImage?bbox=327960.698%2C4447147.265%2C328160.698%2C4447347.265&bboxSR=32617&imageSR=32617&size=540%2C540&format=jpg&f=image&interpolation=RSP_Bilinear"
        ],
        [
          "USGS imagery catalog at pin",
          "https://imagery.nationalmap.gov/arcgis/rest/services/USGSNAIPImagery/ImageServer/identify?geometry=%7B%22x%22%3A+-83.01888098%2C+%22y%22%3A+40.15799426%2C+%22spatialReference%22%3A+%7B%22wkid%22%3A+4326%7D%7D&geometryType=esriGeometryPoint&returnCatalogItems=true&maxItemCount=6&f=pjson"
        ],
        [
          "ODOT nearby bridge inventory query",
          "https://tims.dot.state.oh.us/ags/rest/services/Assets/Bridge_Inventory/MapServer/0/query?where=1%3D1&geometry=-83.02064406%2C40.15664679%2C-83.01711790%2C40.15934173&geometryType=esriGeometryEnvelope&inSR=4326&outFields=%2A&returnGeometry=true&outSR=4326&f=pjson"
        ],
        [
          "ODOT nearby conduit inventory query",
          "https://tims.dot.state.oh.us/ags/rest/services/Assets/Conduit_Inventory/MapServer/0/query?where=1%3D1&geometry=-83.02064406%2C40.15664679%2C-83.01711790%2C40.15934173&geometryType=esriGeometryEnvelope&inSR=4326&outFields=%2A&returnGeometry=true&outSR=4326&f=pjson"
        ]
      ]
    },
    "sources": [
      [
        "ODOT ROW permit intake",
        "https://www.transportation.ohio.gov/business/permits/row-permits"
      ],
      [
        "Official flowline layer",
        "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0"
      ]
    ]
  },
  {
    "id": "S0-W15",
    "segment": "Segment0",
    "feature": "S0-S026-Water",
    "station": 190.9,
    "name": "Deep Run near US-23",
    "priority": "Asset and ROW",
    "method": "Design an independent trenchless crossing clear of ODOT conduit 1876372 and its headwalls after the survey tie.",
    "blocker": "ODOT records show a 72-in pipe about 62 ft from the pin. Establish the tie between the pipe and flowline, the surveyed barrel and wing limits, and ODOT work area and access-control boundaries.",
    "lead": "ODOT District 6 for verified state ROW and drainage occupancy. Confirm controller on plans before applying.",
    "conditional": "Metro Parks or title holder if work leaves verified ROW. Local floodplain and Ohio water approvals if actual footprint triggers them.",
    "submit": "Use ODOT conduit 1876372 at DEL-23-2.269, drainage as-builts and access-control sheets. Show end treatments, pipe elevations, adjacent utilities, ROW, bore and pits, restoration and access.",
    "fallback": "If an ODOT pit or access point is rejected, test an upstream/downstream shift with approved access same tie-ins. Evaluate alternate corridor with all new water and rail checks.",
    "lat": 40.1696005,
    "lon": -83.02084656,
    "evidence": {
      "segment": "Segment0",
      "feature": "S0-S026-Water",
      "station_ft": "190.9",
      "latitude": "40.1696005",
      "longitude": "-83.02084656",
      "water_name": "Deep Run",
      "layer_objectid": "22593",
      "water_fcode": "46003",
      "water_comid": "5214853",
      "water_permanent_id": "",
      "local_gis_angle_deg": "89.4",
      "county_place_township_screen": "DELAWARE / unincorp. or blank / ORANGE",
      "sampled_road_lead": "Columbus US-23",
      "sampled_issuer_lead": "ODOT District 6",
      "nearby_structure_inventory_leads": "",
      "parcel_ids_at_point": "Delaware:999999-0 (OID 98682)",
      "corridor_parcel_ids_within_100ft": "Delaware:318321-0 (OID 99904) | Delaware:318321-8 (OID 23359) | Delaware:999999-0 (OID 98682)",
      "fema_at_point": "X AREA OF MINIMAL FLOOD HAZARD (39041C)",
      "nwi_within_100m": "Riverine R4SBC",
      "source_layer": "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0"
    },
    "review": {
      "classification": "buried",
      "confidence": "Medium",
      "finding": "ODOT conduit 1876372 at DEL-23-2.269 is about 62 ft from the pin. It inventories a 72-in circular concrete pipe, 120 ft long, with headwalls under US 23 near the wooded Deep Run approaches.",
      "next_check": "Tie the surveyed west ditch and both pipe ends to the route. Use the pipe’s actual envelope in the ODOT clearance and work-limit submittal.",
      "image": "img/water-pin-audit/S0-W15.jpg",
      "imagery_catalog_dates": "2023-05-21",
      "proof": [
        [
          "Official flowline 22593",
          "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0/query?objectIds=22593&outFields=%2A&returnGeometry=true&outSR=4326&f=pjson"
        ],
        [
          "ODOT conduit 1876372",
          "https://tims.dot.state.oh.us/ags/rest/services/Assets/Conduit_Inventory/MapServer/0/query?where=CULVERT_FILE_NUMBER%3D1876372&outFields=%2A&returnGeometry=true&outSR=4326&f=pjson"
        ],
        [
          "Original USDA NAIP aerial",
          "https://imagery.nationalmap.gov/arcgis/rest/services/USGSNAIPImagery/ImageServer/exportImage?bbox=327822.606%2C4448439.425%2C328022.606%2C4448639.425&bboxSR=32617&imageSR=32617&size=540%2C540&format=jpg&f=image&interpolation=RSP_Bilinear"
        ],
        [
          "Ohio statewide aerial",
          "https://maps.ohio.gov/image/rest/services/osip_most_current/ImageServer/exportImage?bbox=327822.606%2C4448439.425%2C328022.606%2C4448639.425&bboxSR=32617&imageSR=32617&size=540%2C540&format=jpg&f=image&interpolation=RSP_Bilinear"
        ],
        [
          "USGS imagery catalog at pin",
          "https://imagery.nationalmap.gov/arcgis/rest/services/USGSNAIPImagery/ImageServer/identify?geometry=%7B%22x%22%3A+-83.02084656%2C+%22y%22%3A+40.1696005%2C+%22spatialReference%22%3A+%7B%22wkid%22%3A+4326%7D%7D&geometryType=esriGeometryPoint&returnCatalogItems=true&maxItemCount=6&f=pjson"
        ]
      ]
    },
    "sources": [
      [
        "ODOT ROW permit intake",
        "https://www.transportation.ohio.gov/business/permits/row-permits"
      ],
      [
        "Highbanks Metro Park",
        "https://www.metroparks.net/parks-and-trails/highbanks/"
      ],
      [
        "Official flowline layer",
        "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0"
      ]
    ]
  },
  {
    "id": "S1-W01",
    "segment": "Segment1",
    "feature": "S1-S029-Water",
    "station": 659.5,
    "name": "Olentangy River at Home Road",
    "priority": "Major crossing",
    "method": "Advance bridge attachment and independent HDD in parallel.",
    "blocker": "AE floodway and scenic river. Need SFN 2131870 capacity or available duct, lawful approach work areas, SR 315 limits and exact Section 10 and resource review.",
    "lead": "Delaware County Structures and Commissioners for county bridge attachment/occupancy. Huntington Regulatory determines exact §10 reach and PCN pathway.",
    "conditional": "ODOT D6 for SR 315 work, applicable floodplain administrator, ODNR Scenic Rivers and ODNR/USFWS for actual effects. Ohio EPA if triggered.",
    "submit": "Two concept sections with bridge inspection/utility and support details or HDD geotechnical/scour profile. Show navigation clearance, temporary access, wetlands and species work limits, traffic and same endpoints.",
    "fallback": "If attachment is rejected, pursue independent HDD from surveyed upland pits below scour and outside foundations. If in-water access is refused for either option, redesign for deck-only attachment access or dry HDD staging and resubmit.",
    "lat": 40.19416461,
    "lon": -83.05245199,
    "evidence": {
      "segment": "Segment1",
      "feature": "S1-S029-Water",
      "station_ft": "659.5",
      "latitude": "40.19416461",
      "longitude": "-83.05245199",
      "water_name": "Olentangy River",
      "layer_objectid": "22562",
      "water_fcode": "46006",
      "water_comid": "5214791",
      "water_permanent_id": "",
      "local_gis_angle_deg": "69.1",
      "county_place_township_screen": "DELAWARE / unincorp. or blank / LIBERTY",
      "sampled_road_lead": "Olentangy River Sr 00315 SR-315",
      "sampled_issuer_lead": "ODOT District 6",
      "nearby_structure_inventory_leads": "2131870 @ 64 ft (HOME RD. / OLENTANGY RIVER, maintain code 02)",
      "parcel_ids_at_point": "Delaware:319140-0 (OID 34764)",
      "corridor_parcel_ids_within_100ft": "Delaware:319140-0 (OID 33662) | Delaware:319140-0 (OID 34764)",
      "fema_at_point": "AE FLOODWAY (39041C)",
      "nwi_within_100m": "Riverine R5UBH",
      "source_layer": "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0"
    },
    "review": {
      "classification": "open",
      "confidence": "High",
      "finding": "The Olentangy is visible on both sides of Home Road. The Delaware County bridge project and ODOT SFN 2131870, about 64 ft from the pin, identify the same crossing.",
      "next_check": "Obtain the current bridge and approach drawings. Survey floodway, bank access and foundations for the HDD or approved duct decision.",
      "image": "img/water-pin-audit/S1-W01.jpg",
      "imagery_catalog_dates": "2023-05-18",
      "proof": [
        [
          "Official flowline 22562",
          "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0/query?objectIds=22562&outFields=%2A&returnGeometry=true&outSR=4326&f=pjson"
        ],
        [
          "ODOT structure 2131870",
          "https://tims.dot.state.oh.us/ags/rest/services/Assets/Bridge_Inventory/MapServer/0/query?where=SFN+IN+%28%272131870%27%29&outFields=SFN%2CSTR_LOC_CARRIED%2CINVENT_FEAT%2CMAIN_STR_TYPE_CD%2CCULVERT_LEN%2CMAINT_RESP_CD&returnGeometry=true&outSR=4326&f=pjson"
        ],
        [
          "Delaware County Home Road bridge and SR 315",
          "https://engineer.co.delaware.oh.us/projects/home315/"
        ],
        [
          "Original USDA NAIP aerial",
          "https://imagery.nationalmap.gov/arcgis/rest/services/USGSNAIPImagery/ImageServer/exportImage?bbox=325194.225%2C4451227.921%2C325394.225%2C4451427.921&bboxSR=32617&imageSR=32617&size=540%2C540&format=jpg&f=image&interpolation=RSP_Bilinear"
        ],
        [
          "Ohio statewide aerial",
          "https://maps.ohio.gov/image/rest/services/osip_most_current/ImageServer/exportImage?bbox=325194.225%2C4451227.921%2C325394.225%2C4451427.921&bboxSR=32617&imageSR=32617&size=540%2C540&format=jpg&f=image&interpolation=RSP_Bilinear"
        ],
        [
          "USGS imagery catalog at pin",
          "https://imagery.nationalmap.gov/arcgis/rest/services/USGSNAIPImagery/ImageServer/identify?geometry=%7B%22x%22%3A+-83.05245199%2C+%22y%22%3A+40.19416461%2C+%22spatialReference%22%3A+%7B%22wkid%22%3A+4326%7D%7D&geometryType=esriGeometryPoint&returnCatalogItems=true&maxItemCount=6&f=pjson"
        ]
      ]
    },
    "sources": [
      [
        "Delaware County utility and ROW permits",
        "https://engineer.co.delaware.oh.us/permits/"
      ],
      [
        "Home Road bridge and SR 315 project",
        "https://engineer.co.delaware.oh.us/projects/home315/"
      ],
      [
        "ODNR Olentangy Scenic River",
        "https://ohiodnr.gov/go-and-do/plan-a-visit/find-a-property/olentangy-scenic-river"
      ],
      [
        "Official flowline layer",
        "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0"
      ]
    ]
  },
  {
    "id": "S1-W02",
    "segment": "Segment1",
    "feature": "S1-S030-Bore",
    "station": 2313.1,
    "name": "Wildcat Run at Home Road",
    "priority": "Asset and ROW",
    "method": "Trenchless bore clear of Home Road structure 2133261.",
    "blocker": "Need headwall or foundation envelope and ditch limits. Inventory point is about 51 ft from the exact line intersection.",
    "lead": "Delaware County Engineer for CR-124 and structure plans. County approval for road/asset interference.",
    "conditional": "Floodplain and Ohio water authorities as actual work requires. Verify title at both pit limits.",
    "submit": "Home Road structure plan, crossing and drainage survey, bore section and dry pits, traffic and clearance at approaches.",
    "fallback": "Shift around the foundations within approved frontage if the preferred pit is rejected. Check a bridge conduit only against confirmed owner and duct rights.",
    "lat": 40.19451286,
    "lon": -83.06135313,
    "evidence": {
      "segment": "Segment1",
      "feature": "S1-S030-Bore",
      "station_ft": "2313.1",
      "latitude": "40.19451286",
      "longitude": "-83.06135313",
      "water_name": "",
      "layer_objectid": "22557",
      "water_fcode": "46006",
      "water_comid": "5214781",
      "water_permanent_id": "",
      "local_gis_angle_deg": "69.7",
      "county_place_township_screen": "DELAWARE / unincorp. or blank / LIBERTY",
      "sampled_road_lead": "Home Cr 00124 CR-124",
      "sampled_issuer_lead": "Delaware County Engineer",
      "nearby_structure_inventory_leads": "2133261 @ 51 ft (HOME RD. / WILDCAT RUN, maintain code 02)",
      "parcel_ids_at_point": "Delaware:319140-7 (OID 34493)",
      "corridor_parcel_ids_within_100ft": "Delaware:319131-1 (OID 33867) | Delaware:319131-3 (OID 33868) | Delaware:319140-6 (OID 34767) | Delaware:319140-7 (OID 34493)",
      "fema_at_point": "X AREA OF MINIMAL FLOOD HAZARD (39041C)",
      "nwi_within_100m": "Riverine R5UBH",
      "source_layer": "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0"
    },
    "review": {
      "classification": "open",
      "confidence": "Medium",
      "finding": "A wooded Wildcat Run ravine lines up with Home Road structure 2133261, about 51 ft from the pin. The inventory identifies a frame structure, code 07. Trees obscure the bed in the aerial.",
      "next_check": "Survey the opening, seasonal channel and foundations before setting the profile. Check the crossing separately from the Liberty Road culvert.",
      "image": "img/water-pin-audit/S1-W02.jpg",
      "imagery_catalog_dates": "2023-05-18, 2023-07-30",
      "proof": [
        [
          "Official flowline 22557",
          "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0/query?objectIds=22557&outFields=%2A&returnGeometry=true&outSR=4326&f=pjson"
        ],
        [
          "ODOT structure 2133261",
          "https://tims.dot.state.oh.us/ags/rest/services/Assets/Bridge_Inventory/MapServer/0/query?where=SFN+IN+%28%272133261%27%29&outFields=SFN%2CSTR_LOC_CARRIED%2CINVENT_FEAT%2CMAIN_STR_TYPE_CD%2CCULVERT_LEN%2CMAINT_RESP_CD&returnGeometry=true&outSR=4326&f=pjson"
        ],
        [
          "Original USDA NAIP aerial",
          "https://imagery.nationalmap.gov/arcgis/rest/services/USGSNAIPImagery/ImageServer/exportImage?bbox=324437.398%2C4451284.143%2C324637.398%2C4451484.143&bboxSR=32617&imageSR=32617&size=540%2C540&format=jpg&f=image&interpolation=RSP_Bilinear"
        ],
        [
          "Ohio statewide aerial",
          "https://maps.ohio.gov/image/rest/services/osip_most_current/ImageServer/exportImage?bbox=324437.398%2C4451284.143%2C324637.398%2C4451484.143&bboxSR=32617&imageSR=32617&size=540%2C540&format=jpg&f=image&interpolation=RSP_Bilinear"
        ],
        [
          "USGS imagery catalog at pin",
          "https://imagery.nationalmap.gov/arcgis/rest/services/USGSNAIPImagery/ImageServer/identify?geometry=%7B%22x%22%3A+-83.06135313%2C+%22y%22%3A+40.19451286%2C+%22spatialReference%22%3A+%7B%22wkid%22%3A+4326%7D%7D&geometryType=esriGeometryPoint&returnCatalogItems=true&maxItemCount=6&f=pjson"
        ]
      ]
    },
    "sources": [
      [
        "Delaware County utility and ROW permits",
        "https://engineer.co.delaware.oh.us/permits/"
      ],
      [
        "Official flowline layer",
        "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0"
      ]
    ]
  },
  {
    "id": "S1-W03",
    "segment": "Segment1",
    "feature": "S1-S030-Bore",
    "station": 7749.8,
    "name": "Wildcat Run at Liberty Road",
    "priority": "Asset and ROW",
    "method": "Separate short bore near SFN 2134810.",
    "blocker": "Distinct crossing from Home Road on the same flowline. Need Liberty Road culvert and road/roundabout drainage geometry. FEMA lookup unavailable.",
    "lead": "Delaware County Engineer for Liberty road/structure pathway. Confirm city or township involvement if the final footprint overlaps their segment.",
    "conditional": "Actual drainage owner, floodplain office after effective FIRM check, federal/state review if disturbed waters are implicated.",
    "submit": "Liberty Road as-built, roundabout storm/ROW overlay, crossing profile and pit exhibits; tie both Wildcat sites on the route plan.",
    "fallback": "If the local bore is refused, shift beside the existing road structure. Compare the S1D-01 Home Road alternative only with Powell frontage, rail overpass and customer tie-in checks.",
    "lat": 40.19275204,
    "lon": -83.07731301,
    "evidence": {
      "segment": "Segment1",
      "feature": "S1-S030-Bore",
      "station_ft": "7749.8",
      "latitude": "40.19275204",
      "longitude": "-83.07731301",
      "water_name": "",
      "layer_objectid": "22557",
      "water_fcode": "46006",
      "water_comid": "5214781",
      "water_permanent_id": "",
      "local_gis_angle_deg": "56.5",
      "county_place_township_screen": "DELAWARE / unincorp. or blank / LIBERTY",
      "sampled_road_lead": "Liberty Cr 00009 CR-9",
      "sampled_issuer_lead": "Delaware County Engineer",
      "nearby_structure_inventory_leads": "2134810 @ 43 ft (LIBERTY RD. / WILDCAT RUN, maintain code 02)",
      "parcel_ids_at_point": "",
      "corridor_parcel_ids_within_100ft": "Delaware:319132-0 (OID 32417) | Delaware:319132-0 (OID 32588) | Delaware:319132-0 (OID 33100)",
      "fema_at_point": "Unavailable",
      "nwi_within_100m": "Riverine R5UBH",
      "source_layer": "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0"
    },
    "review": {
      "classification": "buried",
      "confidence": "High",
      "finding": "Tree-lined Wildcat Run approaches Liberty Road. ODOT SFN 2134810, about 43 ft from the pin, identifies a 64-ft culvert under the road.",
      "next_check": "Survey both wingwall and barrel limits and fit an independent bore with the owner’s clearance.",
      "image": "img/water-pin-audit/S1-W03.jpg",
      "imagery_catalog_dates": "2023-07-30",
      "proof": [
        [
          "Official flowline 22557",
          "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0/query?objectIds=22557&outFields=%2A&returnGeometry=true&outSR=4326&f=pjson"
        ],
        [
          "ODOT structure 2134810",
          "https://tims.dot.state.oh.us/ags/rest/services/Assets/Bridge_Inventory/MapServer/0/query?where=SFN+IN+%28%272134810%27%29&outFields=SFN%2CSTR_LOC_CARRIED%2CINVENT_FEAT%2CMAIN_STR_TYPE_CD%2CCULVERT_LEN%2CMAINT_RESP_CD&returnGeometry=true&outSR=4326&f=pjson"
        ],
        [
          "Original USDA NAIP aerial",
          "https://imagery.nationalmap.gov/arcgis/rest/services/USGSNAIPImagery/ImageServer/exportImage?bbox=323074.215%2C4451120.362%2C323274.215%2C4451320.362&bboxSR=32617&imageSR=32617&size=540%2C540&format=jpg&f=image&interpolation=RSP_Bilinear"
        ],
        [
          "Ohio statewide aerial",
          "https://maps.ohio.gov/image/rest/services/osip_most_current/ImageServer/exportImage?bbox=323074.215%2C4451120.362%2C323274.215%2C4451320.362&bboxSR=32617&imageSR=32617&size=540%2C540&format=jpg&f=image&interpolation=RSP_Bilinear"
        ],
        [
          "USGS imagery catalog at pin",
          "https://imagery.nationalmap.gov/arcgis/rest/services/USGSNAIPImagery/ImageServer/identify?geometry=%7B%22x%22%3A+-83.07731301%2C+%22y%22%3A+40.19275204%2C+%22spatialReference%22%3A+%7B%22wkid%22%3A+4326%7D%7D&geometryType=esriGeometryPoint&returnCatalogItems=true&maxItemCount=6&f=pjson"
        ]
      ]
    },
    "sources": [
      [
        "Delaware County utility and ROW permits",
        "https://engineer.co.delaware.oh.us/permits/"
      ],
      [
        "Official flowline layer",
        "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0"
      ]
    ]
  },
  {
    "id": "S1-W04",
    "segment": "Segment1",
    "feature": "S1-S030-Bore",
    "station": 12404.0,
    "name": "Lick Run at Liberty Road",
    "priority": "Asset and ROW",
    "method": "Separate short bore with upland pits outside pond/outlet limits.",
    "blocker": "SFN 2135620 is about 75 ft away. Need pond edge/outlet, culvert and pit rights. FEMA lookup unavailable.",
    "lead": "Delaware County Engineer utility and structure review for Liberty Road. Actual pond/drainage controller for impacts.",
    "conditional": "Local floodplain administrator with effective map and Ohio water agency review as applicable. Obtain rights at any private pit.",
    "submit": "Liberty crossing plan, pond/outlet survey, structure/utility profile, extent of work and driveway access. Compare setup sharing with Rutherford.",
    "fallback": "If one pit conflicts with pond operations, shift to a dry lawful side. Share mobilization with Rutherford only after plans prove separate works and access fit.",
    "lat": 40.17998818,
    "lon": -83.07799773,
    "evidence": {
      "segment": "Segment1",
      "feature": "S1-S030-Bore",
      "station_ft": "12404.0",
      "latitude": "40.17998818",
      "longitude": "-83.07799773",
      "water_name": "",
      "layer_objectid": "22575",
      "water_fcode": "46003",
      "water_comid": "5214817",
      "water_permanent_id": "",
      "local_gis_angle_deg": "71.1",
      "county_place_township_screen": "DELAWARE / unincorp. or blank / LIBERTY",
      "sampled_road_lead": "Liberty Cr 00009 CR-9",
      "sampled_issuer_lead": "Delaware County Engineer",
      "nearby_structure_inventory_leads": "2135620 @ 75 ft (LIBERTY RD. / LICK RUN, maintain code 02) | 2135671 @ 400 ft (RUTHERFORD RD. / LICK RUN, maintain code 02)",
      "parcel_ids_at_point": "",
      "corridor_parcel_ids_within_100ft": "Delaware:319133-0 (OID 33237) | Delaware:319133-0 (OID 34087) | Delaware:319133-0 (OID 34089) | Delaware:319133-1 (OID 34086) | Delaware:319133-2 (OID 32736) | Delaware:999999-0 (OID 99040)",
      "fema_at_point": "Unavailable",
      "nwi_within_100m": "Freshwater Pond PUBGx | Riverine R5UBH",
      "source_layer": "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0"
    },
    "review": {
      "classification": "buried",
      "confidence": "Medium",
      "finding": "ODOT SFN 2135620 places a 56-ft Lick Run culvert under Liberty Road about 75 ft from the pin. The aerial shows drainage and a nearby pond. The pond outlet connection remains unverified.",
      "next_check": "Trace the actual road barrel and pond drainage separately. Survey headwalls, property and pits before fixing the bore.",
      "image": "img/water-pin-audit/S1-W04.jpg",
      "imagery_catalog_dates": "2023-07-30",
      "proof": [
        [
          "Official flowline 22575",
          "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0/query?objectIds=22575&outFields=%2A&returnGeometry=true&outSR=4326&f=pjson"
        ],
        [
          "ODOT structure 2135620",
          "https://tims.dot.state.oh.us/ags/rest/services/Assets/Bridge_Inventory/MapServer/0/query?where=SFN+IN+%28%272135620%27%29&outFields=SFN%2CSTR_LOC_CARRIED%2CINVENT_FEAT%2CMAIN_STR_TYPE_CD%2CCULVERT_LEN%2CMAINT_RESP_CD&returnGeometry=true&outSR=4326&f=pjson"
        ],
        [
          "Original USDA NAIP aerial",
          "https://imagery.nationalmap.gov/arcgis/rest/services/USGSNAIPImagery/ImageServer/exportImage?bbox=322982.753%2C4449704.860%2C323182.753%2C4449904.860&bboxSR=32617&imageSR=32617&size=540%2C540&format=jpg&f=image&interpolation=RSP_Bilinear"
        ],
        [
          "Ohio statewide aerial",
          "https://maps.ohio.gov/image/rest/services/osip_most_current/ImageServer/exportImage?bbox=322982.753%2C4449704.860%2C323182.753%2C4449904.860&bboxSR=32617&imageSR=32617&size=540%2C540&format=jpg&f=image&interpolation=RSP_Bilinear"
        ],
        [
          "USGS imagery catalog at pin",
          "https://imagery.nationalmap.gov/arcgis/rest/services/USGSNAIPImagery/ImageServer/identify?geometry=%7B%22x%22%3A+-83.07799773%2C+%22y%22%3A+40.17998818%2C+%22spatialReference%22%3A+%7B%22wkid%22%3A+4326%7D%7D&geometryType=esriGeometryPoint&returnCatalogItems=true&maxItemCount=6&f=pjson"
        ]
      ]
    },
    "sources": [
      [
        "Delaware County utility and ROW permits",
        "https://engineer.co.delaware.oh.us/permits/"
      ],
      [
        "Official flowline layer",
        "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0"
      ]
    ]
  },
  {
    "id": "S1-W05",
    "segment": "Segment1",
    "feature": "S1-S030-Bore",
    "station": 13003.3,
    "name": "Lick Run at Rutherford Road",
    "priority": "Asset and ROW",
    "method": "Separate pipe or channel clearance bore at Rutherford.",
    "blocker": "Need turn-area and driveway access, foundation limits and division of county structure vs. township roadway responsibility. SFN 2135671 about 79 ft away.",
    "lead": "Delaware County Engineer for structure and utility coordination. Liberty Township for its own ROW work path where applicable.",
    "conditional": "Drainage owner, floodplain and Ohio water review if footprint touches regulated limits.",
    "submit": "Rutherford structure, roadway and ROW profile, agreed county/township scope, driveway/truck access, pit and utility clearance exhibits.",
    "fallback": "If the current pit blocks a turning movement or driveway, move it along authorized Rutherford frontage and retain an independent crossing profile.",
    "lat": 40.17922551,
    "lon": -83.07910023,
    "evidence": {
      "segment": "Segment1",
      "feature": "S1-S030-Bore",
      "station_ft": "13003.3",
      "latitude": "40.17922551",
      "longitude": "-83.07910023",
      "water_name": "",
      "layer_objectid": "22575",
      "water_fcode": "46003",
      "water_comid": "5214817",
      "water_permanent_id": "",
      "local_gis_angle_deg": "63.6",
      "county_place_township_screen": "DELAWARE / unincorp. or blank / LIBERTY",
      "sampled_road_lead": "Rutherford Tr 00122 TR-122",
      "sampled_issuer_lead": "Liberty Township (self-issuer) + Delaware Co Engineer",
      "nearby_structure_inventory_leads": "2135671 @ 79 ft (RUTHERFORD RD. / LICK RUN, maintain code 02) | 2135620 @ 346 ft (LIBERTY RD. / LICK RUN, maintain code 02)",
      "parcel_ids_at_point": "Delaware:319133-0 (OID 33237)",
      "corridor_parcel_ids_within_100ft": "Delaware:319133-0 (OID 33237) | Delaware:319422-0 (OID 41150) | Delaware:319422-0 (OID 44507)",
      "fema_at_point": "X AREA OF MINIMAL FLOOD HAZARD (39041C)",
      "nwi_within_100m": "Freshwater Pond PUBGx | Riverine R5UBH",
      "source_layer": "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0"
    },
    "review": {
      "classification": "buried",
      "confidence": "Medium",
      "finding": "The vegetated Lick Run corridor reaches Rutherford Road. ODOT SFN 2135671 places a 64-ft culvert about 79 ft from the pin. It is a separate structure from the Liberty Road culvert.",
      "next_check": "Tie the two barrel ends to the route and check clearance with the Rutherford road authority. Use a separate survey and profile for Liberty.",
      "image": "img/water-pin-audit/S1-W05.jpg",
      "imagery_catalog_dates": "2023-07-30",
      "proof": [
        [
          "Official flowline 22575",
          "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0/query?objectIds=22575&outFields=%2A&returnGeometry=true&outSR=4326&f=pjson"
        ],
        [
          "ODOT structure 2135671",
          "https://tims.dot.state.oh.us/ags/rest/services/Assets/Bridge_Inventory/MapServer/0/query?where=SFN+IN+%28%272135671%27%29&outFields=SFN%2CSTR_LOC_CARRIED%2CINVENT_FEAT%2CMAIN_STR_TYPE_CD%2CCULVERT_LEN%2CMAINT_RESP_CD&returnGeometry=true&outSR=4326&f=pjson"
        ],
        [
          "Original USDA NAIP aerial",
          "https://imagery.nationalmap.gov/arcgis/rest/services/USGSNAIPImagery/ImageServer/exportImage?bbox=322886.898%2C4449622.397%2C323086.898%2C4449822.397&bboxSR=32617&imageSR=32617&size=540%2C540&format=jpg&f=image&interpolation=RSP_Bilinear"
        ],
        [
          "Ohio statewide aerial",
          "https://maps.ohio.gov/image/rest/services/osip_most_current/ImageServer/exportImage?bbox=322886.898%2C4449622.397%2C323086.898%2C4449822.397&bboxSR=32617&imageSR=32617&size=540%2C540&format=jpg&f=image&interpolation=RSP_Bilinear"
        ],
        [
          "USGS imagery catalog at pin",
          "https://imagery.nationalmap.gov/arcgis/rest/services/USGSNAIPImagery/ImageServer/identify?geometry=%7B%22x%22%3A+-83.07910023%2C+%22y%22%3A+40.17922551%2C+%22spatialReference%22%3A+%7B%22wkid%22%3A+4326%7D%7D&geometryType=esriGeometryPoint&returnCatalogItems=true&maxItemCount=6&f=pjson"
        ]
      ]
    },
    "sources": [
      [
        "Delaware County utility and ROW permits",
        "https://engineer.co.delaware.oh.us/permits/"
      ],
      [
        "County and Liberty Township permit assignments",
        "https://engineer.co.delaware.oh.us/permits/"
      ],
      [
        "Official flowline layer",
        "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0"
      ]
    ]
  },
  {
    "id": "S1-W06",
    "segment": "Segment1",
    "feature": "S1-S032-Bore",
    "station": 6321.6,
    "name": "Unnamed Sawmill Parkway drainage OID 22561",
    "priority": "Asset and ROW",
    "method": "Use road and subdivision drainage records to establish a crossing before pricing a separate bore or changing the angle.",
    "blocker": "About 30° to the mapped line. Need storm trunk, pond outlet and wet limit position plus ROW control. FEMA lookup unavailable.",
    "lead": "Powell Engineering for in-city permit and provider requirements. Delaware County for boundary/county segments as the actual footprint dictates.",
    "conditional": "Drainage owner, local floodplain, Ohio water agencies if regulated work is triggered. Golf property approval only if work affects it.",
    "submit": "Storm as-built and pond outlet survey, compare skews and pit areas, verify registration/ROW documents and any separate cart-path structure interference.",
    "fallback": "If the shorter skew shift crosses an outlet or requires unavailable rights, use the existing side with a longer clear bore or move staging to another approved part of Sawmill.",
    "lat": 40.19104101,
    "lon": -83.09555509,
    "evidence": {
      "segment": "Segment1",
      "feature": "S1-S032-Bore",
      "station_ft": "6321.6",
      "latitude": "40.19104101",
      "longitude": "-83.09555509",
      "water_name": "",
      "layer_objectid": "22561",
      "water_fcode": "46003",
      "water_comid": "5214789",
      "water_permanent_id": "",
      "local_gis_angle_deg": "29.7",
      "county_place_township_screen": "DELAWARE / POWELL / LIBERTY",
      "sampled_road_lead": "Sawmill Cr 00609 CR-609",
      "sampled_issuer_lead": "City of Powell – maintains in-city stretch; ROW permit + registration (County Engineer on boundary stretches)",
      "nearby_structure_inventory_leads": "",
      "parcel_ids_at_point": "Delaware:999999-0 (OID 99040)",
      "corridor_parcel_ids_within_100ft": "Delaware:319240-0 (OID 100598) | Delaware:319240-0 (OID 36454) | Delaware:319240-0 (OID 36455) | Delaware:319240-1 (OID 37282) | Delaware:319240-1 (OID 37285) | Delaware:319240-1 (OID 39131) | Delaware:319240-2 (OID 36451) | Delaware:319240-2 (OID 37245) | Delaware:319240-2 (OID 39134) | Delaware:319240-2 (OID 39250) | Delaware:319240-3 (OID 36452) | Delaware:319240-3 (OID 37283) | Delaware:319240-3 (OID 39254) | Delaware:319240-4 (OID 37246) | Delaware:319240-4 (OID 39251) | Delaware:319240-4 (OID 39255) | Delaware:319240-5 (OID 39132) | Delaware:319240-5 (OID 39248) | Delaware:319240-6 (OID 37247) | Delaware:319240-6 (OID 39252) | Delaware:319240-7 (OID 37248) | Delaware:319240-7 (OID 39253) | Delaware:319240-8 (OID 39133) | Delaware:319240-8 (OID 39249) | Delaware:319240-9 (OID 36453) | Delaware:319240-9 (OID 37284) | Delaware:999999-0 (OID 99040)",
      "fema_at_point": "Unavailable",
      "nwi_within_100m": "Freshwater Pond PUBGx | Riverine R4SBC",
      "source_layer": "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0"
    },
    "review": {
      "classification": "gis",
      "confidence": "Unverified",
      "finding": "Flowline 22561 crosses the Sawmill Parkway corridor beside a neighborhood access and tree strip. The images show no identifiable inlet/outlet pair or visible open passage and the inventory has no matched structure.",
      "next_check": "Obtain Sawmill road and subdivision drainage sheets and trace the low path through approved plans and a field walk.",
      "image": "img/water-pin-audit/S1-W06.jpg",
      "imagery_catalog_dates": "2023-07-30",
      "proof": [
        [
          "Official flowline 22561",
          "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0/query?objectIds=22561&outFields=%2A&returnGeometry=true&outSR=4326&f=pjson"
        ],
        [
          "Delaware County road and drainage permit intake",
          "https://engineer.co.delaware.oh.us/permits/"
        ],
        [
          "Original USDA NAIP aerial",
          "https://imagery.nationalmap.gov/arcgis/rest/services/USGSNAIPImagery/ImageServer/exportImage?bbox=321516.805%2C4450966.938%2C321716.805%2C4451166.938&bboxSR=32617&imageSR=32617&size=540%2C540&format=jpg&f=image&interpolation=RSP_Bilinear"
        ],
        [
          "Ohio statewide aerial",
          "https://maps.ohio.gov/image/rest/services/osip_most_current/ImageServer/exportImage?bbox=321516.805%2C4450966.938%2C321716.805%2C4451166.938&bboxSR=32617&imageSR=32617&size=540%2C540&format=jpg&f=image&interpolation=RSP_Bilinear"
        ],
        [
          "USGS imagery catalog at pin",
          "https://imagery.nationalmap.gov/arcgis/rest/services/USGSNAIPImagery/ImageServer/identify?geometry=%7B%22x%22%3A+-83.09555509%2C+%22y%22%3A+40.19104101%2C+%22spatialReference%22%3A+%7B%22wkid%22%3A+4326%7D%7D&geometryType=esriGeometryPoint&returnCatalogItems=true&maxItemCount=6&f=pjson"
        ],
        [
          "ODOT nearby bridge inventory query",
          "https://tims.dot.state.oh.us/ags/rest/services/Assets/Bridge_Inventory/MapServer/0/query?where=1%3D1&geometry=-83.09731903%2C40.18969354%2C-83.09379115%2C40.19238848&geometryType=esriGeometryEnvelope&inSR=4326&outFields=%2A&returnGeometry=true&outSR=4326&f=pjson"
        ],
        [
          "ODOT nearby conduit inventory query",
          "https://tims.dot.state.oh.us/ags/rest/services/Assets/Conduit_Inventory/MapServer/0/query?where=1%3D1&geometry=-83.09731903%2C40.18969354%2C-83.09379115%2C40.19238848&geometryType=esriGeometryEnvelope&inSR=4326&outFields=%2A&returnGeometry=true&outSR=4326&f=pjson"
        ]
      ]
    },
    "sources": [
      [
        "Powell ROW ordinance",
        "https://www.cityofpowell.us/files/assets/city/v/1/city-council/documents/ordinances/2022/ordinance-2022-11.pdf"
      ],
      [
        "Delaware County utility and ROW permits",
        "https://engineer.co.delaware.oh.us/permits/"
      ],
      [
        "Official flowline layer",
        "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0"
      ]
    ]
  },
  {
    "id": "S1-W07",
    "segment": "Segment1",
    "feature": "S1-S032-Bore",
    "station": 15696.7,
    "name": "Unnamed Home Road drainage OID 22560",
    "priority": "Asset and ROW",
    "method": "Trace the pond outlet and road drainage first. Determine whether the road bore needs a drainage-specific profile.",
    "blocker": "About 33° to the mapped drainage with pond/riverine screening. Need actual outlet, banks, trail/cart path limits and dry pits. FEMA lookup unavailable.",
    "lead": "Delaware County Engineer for Home Road. Get pond/drainage and cart-path clearance from actual owner if work reaches them.",
    "conditional": "Local floodplain office and Huntington/Ohio EPA as actual effects require. Private recreation property consent if applicable.",
    "submit": "Subdivision and Home Road drainage plans, survey of the outlet and approaches, alternative local profile and traffic/trail/access plan.",
    "fallback": "If a direct crossing cannot be approved with dry pits, move the tie-in along Home Road to a narrower surveyed drainage section and rescreen ROW and work access.",
    "lat": 40.19682676,
    "lon": -83.12343107,
    "evidence": {
      "segment": "Segment1",
      "feature": "S1-S032-Bore",
      "station_ft": "15696.7",
      "latitude": "40.19682676",
      "longitude": "-83.12343107",
      "water_name": "",
      "layer_objectid": "22560",
      "water_fcode": "46003",
      "water_comid": "5214787",
      "water_permanent_id": "",
      "local_gis_angle_deg": "33.4",
      "county_place_township_screen": "DELAWARE / unincorp. or blank / CONCORD",
      "sampled_road_lead": "Home Cr 00124 CR-124",
      "sampled_issuer_lead": "Delaware County Engineer",
      "nearby_structure_inventory_leads": "",
      "parcel_ids_at_point": "Delaware:999999-0 (OID 99034)",
      "corridor_parcel_ids_within_100ft": "Delaware:319230-0 (OID 37677) | Delaware:319230-0 (OID 37803) | Delaware:319230-0 (OID 38482) | Delaware:319230-1 (OID 37804) | Delaware:999999-0 (OID 99034)",
      "fema_at_point": "Unavailable",
      "nwi_within_100m": "Freshwater Pond PUBGh | Riverine R4SBC | Riverine R5UBH",
      "source_layer": "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0"
    },
    "review": {
      "classification": "gis",
      "confidence": "Unverified",
      "finding": "Home Road separates visible pond and drainage features around a developing subdivision. Summer and Ohio leaf-off imagery differ in grading. Neither establishes a continuous ditch or pipe through the pin.",
      "next_check": "Get the approved grading, storm plan and closeout records for the development. Confirm the pond outlet and road crossing before locating pits.",
      "image": "img/water-pin-audit/S1-W07.jpg",
      "imagery_catalog_dates": "2023-05-18, 2023-07-30",
      "proof": [
        [
          "Official flowline 22560",
          "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0/query?objectIds=22560&outFields=%2A&returnGeometry=true&outSR=4326&f=pjson"
        ],
        [
          "Delaware County road and drainage permit intake",
          "https://engineer.co.delaware.oh.us/permits/"
        ],
        [
          "Original USDA NAIP aerial",
          "https://imagery.nationalmap.gov/arcgis/rest/services/USGSNAIPImagery/ImageServer/exportImage?bbox=319159.061%2C4451665.607%2C319359.061%2C4451865.607&bboxSR=32617&imageSR=32617&size=540%2C540&format=jpg&f=image&interpolation=RSP_Bilinear"
        ],
        [
          "Ohio statewide aerial",
          "https://maps.ohio.gov/image/rest/services/osip_most_current/ImageServer/exportImage?bbox=319159.061%2C4451665.607%2C319359.061%2C4451865.607&bboxSR=32617&imageSR=32617&size=540%2C540&format=jpg&f=image&interpolation=RSP_Bilinear"
        ],
        [
          "USGS imagery catalog at pin",
          "https://imagery.nationalmap.gov/arcgis/rest/services/USGSNAIPImagery/ImageServer/identify?geometry=%7B%22x%22%3A+-83.12343107%2C+%22y%22%3A+40.19682676%2C+%22spatialReference%22%3A+%7B%22wkid%22%3A+4326%7D%7D&geometryType=esriGeometryPoint&returnCatalogItems=true&maxItemCount=6&f=pjson"
        ],
        [
          "ODOT nearby bridge inventory query",
          "https://tims.dot.state.oh.us/ags/rest/services/Assets/Bridge_Inventory/MapServer/0/query?where=1%3D1&geometry=-83.12519516%2C40.19547929%2C-83.12166698%2C40.19817423&geometryType=esriGeometryEnvelope&inSR=4326&outFields=%2A&returnGeometry=true&outSR=4326&f=pjson"
        ],
        [
          "ODOT nearby conduit inventory query",
          "https://tims.dot.state.oh.us/ags/rest/services/Assets/Conduit_Inventory/MapServer/0/query?where=1%3D1&geometry=-83.12519516%2C40.19547929%2C-83.12166698%2C40.19817423&geometryType=esriGeometryEnvelope&inSR=4326&outFields=%2A&returnGeometry=true&outSR=4326&f=pjson"
        ]
      ]
    },
    "sources": [
      [
        "Delaware County utility and ROW permits",
        "https://engineer.co.delaware.oh.us/permits/"
      ],
      [
        "Official flowline layer",
        "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0"
      ]
    ]
  },
  {
    "id": "S1-W08",
    "segment": "Segment1",
    "feature": "S1-S033-Water",
    "station": 682.2,
    "name": "O’Shaughnessy Reservoir at the Fred L. Stults Bridge",
    "priority": "Major crossing",
    "method": "Lead with licensed existing duct or sealed supported conduit on SFN 2134462.",
    "blocker": "Need verified duct capacity or attachment zone and structural acceptance, executed 01-957 agreement and amendments, approach rights, SR 257 ties, temporary access and Corps §10 reach decision.",
    "lead": "Delaware County Engineer Structures and Commissioners for attachment and occupation. Columbus Water & Power Watershed/real estate for affected City land, reservoir interests and written concurrence. Huntington Regulatory for federal determination.",
    "conditional": "ODOT D6 for SR 257 scope. Floodplain, Ohio EPA and dam safety review where work triggers them. Coordinate boat-ramp/park access with actual operators.",
    "submit": "Send separate west landfall, bridge and east approach exhibits. Include as-builts and inspection, sealed load/support/expansion design, conduit capacity and use rights, clearance/temporary access, land instrument, impact table and construction traffic plan.",
    "fallback": "If no duct is available, move to new supported conduit. If the attachment is refused, evaluate a long HDD with written shore/subsurface rights, bathymetry, geotechnical and drilling-fluid plan. A different road crossing is the later fallback, requiring new permits and same tie-ins.",
    "lat": 40.19676272,
    "lon": -83.13946656,
    "evidence": {
      "segment": "Segment1",
      "feature": "S1-S033-Water",
      "station_ft": "682.2",
      "latitude": "40.19676272",
      "longitude": "-83.13946656",
      "water_name": "Scioto River",
      "layer_objectid": "22955",
      "water_fcode": "55800",
      "water_comid": "5215631",
      "water_permanent_id": "",
      "local_gis_angle_deg": "80.7",
      "county_place_township_screen": "DELAWARE / unincorp. or blank / CONCORD",
      "sampled_road_lead": "Home Cr 00124 CR-124",
      "sampled_issuer_lead": "Delaware County Engineer",
      "nearby_structure_inventory_leads": "2134462 @ 40 ft (HOME ROAD / O'SHAUGHNESSY RESERVOIR, maintain code 02)",
      "parcel_ids_at_point": "Delaware:500310-0 (OID 74513)",
      "corridor_parcel_ids_within_100ft": "Delaware:500310-0 (OID 74513)",
      "fema_at_point": "A  (39041C)",
      "nwi_within_100m": "Lake L1UBHh",
      "source_layer": "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0"
    },
    "review": {
      "classification": "open",
      "confidence": "High",
      "finding": "O’Shaughnessy Reservoir is visibly open across the full span. ODOT identifies Home Road bridge 2134462 about 40 ft from the pin. The GIS line represents the Scioto through the impoundment.",
      "next_check": "Use the bridge-attachment pathway. Obtain bridge as-builts, verify duct/support options and approach rights, and coordinate Delaware County and Columbus Watershed review.",
      "image": "img/water-pin-audit/S1-W08.jpg",
      "imagery_catalog_dates": "2023-05-18",
      "proof": [
        [
          "Official flowline 22955",
          "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0/query?objectIds=22955&outFields=%2A&returnGeometry=true&outSR=4326&f=pjson"
        ],
        [
          "ODOT structure 2134462",
          "https://tims.dot.state.oh.us/ags/rest/services/Assets/Bridge_Inventory/MapServer/0/query?where=SFN+IN+%28%272134462%27%29&outFields=SFN%2CSTR_LOC_CARRIED%2CINVENT_FEAT%2CMAIN_STR_TYPE_CD%2CCULVERT_LEN%2CMAINT_RESP_CD&returnGeometry=true&outSR=4326&f=pjson"
        ],
        [
          "County–Columbus bridge agreement, Resolution 01-957",
          "https://co.delaware.oh.us/wp-content/uploads/commissioners/journal/2001/jnlaug27.pdf"
        ],
        [
          "Original USDA NAIP aerial",
          "https://imagery.nationalmap.gov/arcgis/rest/services/USGSNAIPImagery/ImageServer/exportImage?bbox=317793.883%2C4451691.287%2C317993.883%2C4451891.287&bboxSR=32617&imageSR=32617&size=540%2C540&format=jpg&f=image&interpolation=RSP_Bilinear"
        ],
        [
          "Ohio statewide aerial",
          "https://maps.ohio.gov/image/rest/services/osip_most_current/ImageServer/exportImage?bbox=317793.883%2C4451691.287%2C317993.883%2C4451891.287&bboxSR=32617&imageSR=32617&size=540%2C540&format=jpg&f=image&interpolation=RSP_Bilinear"
        ],
        [
          "USGS imagery catalog at pin",
          "https://imagery.nationalmap.gov/arcgis/rest/services/USGSNAIPImagery/ImageServer/identify?geometry=%7B%22x%22%3A+-83.13946656%2C+%22y%22%3A+40.19676272%2C+%22spatialReference%22%3A+%7B%22wkid%22%3A+4326%7D%7D&geometryType=esriGeometryPoint&returnCatalogItems=true&maxItemCount=6&f=pjson"
        ]
      ]
    },
    "sources": [
      [
        "Delaware County utility and ROW permits",
        "https://engineer.co.delaware.oh.us/permits/"
      ],
      [
        "Delaware–Columbus agreement, Resolution 01-957",
        "https://co.delaware.oh.us/wp-content/uploads/commissioners/journal/2001/jnlaug27.pdf"
      ],
      [
        "Columbus Watershed Management",
        "https://www.columbus.gov/Services/Columbus-Water-Power/About-Columbus-Water-Power/The-Division-of-Water/Reservoir-Land-Stewardship-Program/About-the-Columbus-Watershed-Management-Section"
      ],
      [
        "Official flowline layer",
        "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0"
      ]
    ]
  },
  {
    "id": "S1-W09",
    "segment": "Segment1",
    "feature": "S1-S034-Bore",
    "station": 3984.2,
    "name": "North Branch Eversole Run at Home Road",
    "priority": "Project coordination",
    "method": "Independent bore clear of SFN 2135957, coordinated with current utility plans.",
    "blocker": "Structure nearby at about 30 ft. Need approach pit coordinates, bridge/culvert foundation and intersection or transmission main work limits.",
    "lead": "Delaware County Engineer for structure and road. Columbus Water & Power or relevant owner resolves overlaps with its transmission facilities.",
    "conditional": "Floodplain and Ohio water approvals from footprint. Easement holder for any water main site or temporary access.",
    "submit": "Survey both approaches and work limits, SFN plan, West Home Road utility and roundabout overlay, bore depth/clearance and restoration.",
    "fallback": "If pits conflict with the utility or intersection package, shift along documented Home Road ROW or coordinate a separate construction window to clear planned work.",
    "lat": 40.19540865,
    "lon": -83.15677345,
    "evidence": {
      "segment": "Segment1",
      "feature": "S1-S034-Bore",
      "station_ft": "3984.2",
      "latitude": "40.19540865",
      "longitude": "-83.15677345",
      "water_name": "",
      "layer_objectid": "22572",
      "water_fcode": "46006",
      "water_comid": "5214811",
      "water_permanent_id": "",
      "local_gis_angle_deg": "77.0",
      "county_place_township_screen": "DELAWARE / unincorp. or blank / CONCORD",
      "sampled_road_lead": "Home Cr 00124 CR-124",
      "sampled_issuer_lead": "Delaware County Engineer",
      "nearby_structure_inventory_leads": "2135957 @ 30 ft (HOME RD. / N. BRANCH EVERSOLE RUN, maintain code 02)",
      "parcel_ids_at_point": "Delaware:600240-0 (OID 93044)",
      "corridor_parcel_ids_within_100ft": "Delaware:600240-0 (OID 93041) | Delaware:600240-0 (OID 93042) | Delaware:600240-0 (OID 93043) | Delaware:600240-0 (OID 93044)",
      "fema_at_point": "X AREA OF MINIMAL FLOOD HAZARD (39041C)",
      "nwi_within_100m": "Riverine R3UBH",
      "source_layer": "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0"
    },
    "review": {
      "classification": "buried",
      "confidence": "High",
      "finding": "A vegetated channel approaches Home Road at SFN 2135957, a 56-ft culvert about 30 ft from the pin. This is the North Branch Eversole Run crossing west of the reservoir.",
      "next_check": "Survey pipe, headwalls and apron levels. Protect the drainage envelope and keep this clearance review distinct from the reservoir bridge license.",
      "image": "img/water-pin-audit/S1-W09.jpg",
      "imagery_catalog_dates": "2023-05-18",
      "proof": [
        [
          "Official flowline 22572",
          "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0/query?objectIds=22572&outFields=%2A&returnGeometry=true&outSR=4326&f=pjson"
        ],
        [
          "ODOT structure 2135957",
          "https://tims.dot.state.oh.us/ags/rest/services/Assets/Bridge_Inventory/MapServer/0/query?where=SFN+IN+%28%272135957%27%29&outFields=SFN%2CSTR_LOC_CARRIED%2CINVENT_FEAT%2CMAIN_STR_TYPE_CD%2CCULVERT_LEN%2CMAINT_RESP_CD&returnGeometry=true&outSR=4326&f=pjson"
        ],
        [
          "Original USDA NAIP aerial",
          "https://imagery.nationalmap.gov/arcgis/rest/services/USGSNAIPImagery/ImageServer/exportImage?bbox=316316.993%2C4451576.641%2C316516.993%2C4451776.641&bboxSR=32617&imageSR=32617&size=540%2C540&format=jpg&f=image&interpolation=RSP_Bilinear"
        ],
        [
          "Ohio statewide aerial",
          "https://maps.ohio.gov/image/rest/services/osip_most_current/ImageServer/exportImage?bbox=316316.993%2C4451576.641%2C316516.993%2C4451776.641&bboxSR=32617&imageSR=32617&size=540%2C540&format=jpg&f=image&interpolation=RSP_Bilinear"
        ],
        [
          "USGS imagery catalog at pin",
          "https://imagery.nationalmap.gov/arcgis/rest/services/USGSNAIPImagery/ImageServer/identify?geometry=%7B%22x%22%3A+-83.15677345%2C+%22y%22%3A+40.19540865%2C+%22spatialReference%22%3A+%7B%22wkid%22%3A+4326%7D%7D&geometryType=esriGeometryPoint&returnCatalogItems=true&maxItemCount=6&f=pjson"
        ]
      ]
    },
    "sources": [
      [
        "Delaware County utility and ROW permits",
        "https://engineer.co.delaware.oh.us/permits/"
      ],
      [
        "Home Road and SR 745 County project",
        "https://engineer.co.delaware.oh.us/home-road-sr-745-intersection-improvements/"
      ],
      [
        "Official flowline layer",
        "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0"
      ]
    ]
  },
  {
    "id": "S1-W10",
    "segment": "Segment1",
    "feature": "S1-S034-Bore",
    "station": 6319.4,
    "name": "Concord Road unnamed drainage OID 22551",
    "priority": "Asset and ROW",
    "method": "Tie the route to the current Home/Concord drainage as-builts before including a separate bore at this pin.",
    "blocker": "SFN 2136333 and 2136341 are roughly 278 and 284 ft away. Need to trace outlets and avoid attributing the line to either structure without survey.",
    "lead": "Delaware County Engineer for structures/utility and Concord Township for its applicable ROW work path. Identify drainage controller from plans.",
    "conditional": "Local floodplain and Ohio water review as footprint triggers. Land consent if proposed alignment leaves verified corridor.",
    "submit": "Both bridge/culvert plans and field connectivity, exact route and structure station tie, pits, separate ditch effects, ROW and drainage restoration.",
    "fallback": "If neither structure clearance profile works, shift locally to a surveyed branch crossing with lawful access. Preserve each distinct structure check after realignment.",
    "lat": 40.19643704,
    "lon": -83.16438955,
    "evidence": {
      "segment": "Segment1",
      "feature": "S1-S034-Bore",
      "station_ft": "6319.4",
      "latitude": "40.19643704",
      "longitude": "-83.16438955",
      "water_name": "",
      "layer_objectid": "22551",
      "water_fcode": "46003",
      "water_comid": "5214769",
      "water_permanent_id": "",
      "local_gis_angle_deg": "80.6",
      "county_place_township_screen": "DELAWARE / unincorp. or blank / CONCORD",
      "sampled_road_lead": "Concord Cr 00129 CR-129",
      "sampled_issuer_lead": "Delaware County Engineer",
      "nearby_structure_inventory_leads": "2136333 @ 278 ft (HOME RD. / BRANCH OF EVERSOLE RUN, maintain code 02) | 2136341 @ 284 ft (CONCORD RD. / TRIB TO EVERSOLE RUN, maintain code 02)",
      "parcel_ids_at_point": "Delaware:600230-0 (OID 89637)",
      "corridor_parcel_ids_within_100ft": "Delaware:600230-0 (OID 89637) | Delaware:600230-0 (OID 89638) | Delaware:600230-0 (OID 95388) | Delaware:999999-0 (OID 98731)",
      "fema_at_point": "X AREA OF MINIMAL FLOOD HAZARD (39041C)",
      "nwi_within_100m": "Riverine R4SBC",
      "source_layer": "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0"
    },
    "review": {
      "classification": "gis",
      "confidence": "Unverified",
      "finding": "The pin is on the Concord approach north of the Home Road roundabout. The county describes culvert work around the junction. ODOT candidates 2136333 and 2136341 are about 278 and 284 ft from the pin. The aerial does not tie the mapped line to either asset.",
      "next_check": "Request Home/Concord closeout plans and profiles of the current north and west arms. Check actual pipe extent against the alignment.",
      "image": "img/water-pin-audit/S1-W10.jpg",
      "imagery_catalog_dates": "2023-05-18",
      "proof": [
        [
          "Official flowline 22551",
          "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0/query?objectIds=22551&outFields=%2A&returnGeometry=true&outSR=4326&f=pjson"
        ],
        [
          "Delaware County Home/Concord culvert project",
          "https://engineer.co.delaware.oh.us/projects/home-concord/"
        ],
        [
          "ODOT nearby structures 2136333, 2136341",
          "https://tims.dot.state.oh.us/ags/rest/services/Assets/Bridge_Inventory/MapServer/0/query?where=SFN+IN+%28%272136333%27%2C%272136341%27%29&outFields=SFN%2CSTR_LOC_CARRIED%2CINVENT_FEAT%2CMAIN_STR_TYPE_CD%2CCULVERT_LEN%2CMAINT_RESP_CD&returnGeometry=true&outSR=4326&f=pjson"
        ],
        [
          "Original USDA NAIP aerial",
          "https://imagery.nationalmap.gov/arcgis/rest/services/USGSNAIPImagery/ImageServer/exportImage?bbox=315671.449%2C4451706.586%2C315871.449%2C4451906.586&bboxSR=32617&imageSR=32617&size=540%2C540&format=jpg&f=image&interpolation=RSP_Bilinear"
        ],
        [
          "Ohio statewide aerial",
          "https://maps.ohio.gov/image/rest/services/osip_most_current/ImageServer/exportImage?bbox=315671.449%2C4451706.586%2C315871.449%2C4451906.586&bboxSR=32617&imageSR=32617&size=540%2C540&format=jpg&f=image&interpolation=RSP_Bilinear"
        ],
        [
          "USGS imagery catalog at pin",
          "https://imagery.nationalmap.gov/arcgis/rest/services/USGSNAIPImagery/ImageServer/identify?geometry=%7B%22x%22%3A+-83.16438955%2C+%22y%22%3A+40.19643704%2C+%22spatialReference%22%3A+%7B%22wkid%22%3A+4326%7D%7D&geometryType=esriGeometryPoint&returnCatalogItems=true&maxItemCount=6&f=pjson"
        ],
        [
          "ODOT nearby bridge inventory query",
          "https://tims.dot.state.oh.us/ags/rest/services/Assets/Bridge_Inventory/MapServer/0/query?where=1%3D1&geometry=-83.16615363%2C40.19508957%2C-83.16262547%2C40.19778451&geometryType=esriGeometryEnvelope&inSR=4326&outFields=%2A&returnGeometry=true&outSR=4326&f=pjson"
        ],
        [
          "ODOT nearby conduit inventory query",
          "https://tims.dot.state.oh.us/ags/rest/services/Assets/Conduit_Inventory/MapServer/0/query?where=1%3D1&geometry=-83.16615363%2C40.19508957%2C-83.16262547%2C40.19778451&geometryType=esriGeometryEnvelope&inSR=4326&outFields=%2A&returnGeometry=true&outSR=4326&f=pjson"
        ]
      ]
    },
    "sources": [
      [
        "Delaware County utility and ROW permits",
        "https://engineer.co.delaware.oh.us/permits/"
      ],
      [
        "County and Concord Township permit assignments",
        "https://engineer.co.delaware.oh.us/permits/"
      ],
      [
        "Official flowline layer",
        "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0"
      ]
    ]
  },
  {
    "id": "S1-W11",
    "segment": "Segment1",
    "feature": "S1-S036-Bore",
    "station": 187.8,
    "name": "Concord Road mapped drainage near Duffy Road",
    "priority": "Asset and ROW",
    "method": "Trace the Concord ditch and nearby Duffy structure before assigning a separate crossing allowance to this pin.",
    "blocker": "Flowline 22545 intersects S036. The short S035 feature does not intersect it and SFN 2133709 is about 269 ft away. Hinkle Ditch is a separate structure lead. FEMA point unavailable.",
    "lead": "Delaware County Engineer structures/utility and Concord Township where township permits apply.",
    "conditional": "Local floodplain administrator after viewing effective map. Huntington and Ohio EPA as actual impacts warrant.",
    "submit": "Survey S035 and S036 together with SFNs 2133709 and 2135280, flow paths, asset limit, country-road ROW and culvert clearances; show proposed pits separately.",
    "fallback": "If the current bore area is denied for outlet or foundation conflict, move to a clear near-normal crossing in verified corridor. Combine S035/S036 work only if field plans prove the same work envelope.",
    "lat": 40.20194347,
    "lon": -83.16526942,
    "evidence": {
      "segment": "Segment1",
      "feature": "S1-S036-Bore",
      "station_ft": "187.8",
      "latitude": "40.20194347",
      "longitude": "-83.16526942",
      "water_name": "",
      "layer_objectid": "22545",
      "water_fcode": "46003",
      "water_comid": "5214757",
      "water_permanent_id": "",
      "local_gis_angle_deg": "85.4",
      "county_place_township_screen": "DELAWARE / unincorp. or blank / CONCORD",
      "sampled_road_lead": "Concord Cr 00129 CR-129",
      "sampled_issuer_lead": "Delaware County Engineer",
      "nearby_structure_inventory_leads": "2133709 @ 269 ft (CONCORD RD. / N. BRANCH EVERSOLE RUN, maintain code 02)",
      "parcel_ids_at_point": "Delaware:600220-5 (OID 95286)",
      "corridor_parcel_ids_within_100ft": "Delaware:600220-0 (OID 89992) | Delaware:600220-4 (OID 89982) | Delaware:600220-5 (OID 95286)",
      "fema_at_point": "Unavailable",
      "nwi_within_100m": "Riverine R4SBC",
      "source_layer": "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0"
    },
    "review": {
      "classification": "gis",
      "confidence": "Unverified",
      "finding": "The line reaches Concord Road along a wooded low area near Duffy. Inventory bridge 2133709 is about 269 ft south of the pin at the Duffy crossing. Neither image establishes a connection to that bridge or a distinct crossing here.",
      "next_check": "Walk the road ditch and trace any driveway or roadway pipe to the Duffy drainage. Establish whether a separate crossing is needed.",
      "image": "img/water-pin-audit/S1-W11.jpg",
      "imagery_catalog_dates": "2023-05-18",
      "proof": [
        [
          "Official flowline 22545",
          "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0/query?objectIds=22545&outFields=%2A&returnGeometry=true&outSR=4326&f=pjson"
        ],
        [
          "ODOT structure 2133709",
          "https://tims.dot.state.oh.us/ags/rest/services/Assets/Bridge_Inventory/MapServer/0/query?where=SFN+IN+%28%272133709%27%29&outFields=SFN%2CSTR_LOC_CARRIED%2CINVENT_FEAT%2CMAIN_STR_TYPE_CD%2CCULVERT_LEN%2CMAINT_RESP_CD&returnGeometry=true&outSR=4326&f=pjson"
        ],
        [
          "Delaware County road and drainage permit intake",
          "https://engineer.co.delaware.oh.us/permits/"
        ],
        [
          "Original USDA NAIP aerial",
          "https://imagery.nationalmap.gov/arcgis/rest/services/USGSNAIPImagery/ImageServer/exportImage?bbox=315611.467%2C4452319.668%2C315811.467%2C4452519.668&bboxSR=32617&imageSR=32617&size=540%2C540&format=jpg&f=image&interpolation=RSP_Bilinear"
        ],
        [
          "Ohio statewide aerial",
          "https://maps.ohio.gov/image/rest/services/osip_most_current/ImageServer/exportImage?bbox=315611.467%2C4452319.668%2C315811.467%2C4452519.668&bboxSR=32617&imageSR=32617&size=540%2C540&format=jpg&f=image&interpolation=RSP_Bilinear"
        ],
        [
          "USGS imagery catalog at pin",
          "https://imagery.nationalmap.gov/arcgis/rest/services/USGSNAIPImagery/ImageServer/identify?geometry=%7B%22x%22%3A+-83.16526942%2C+%22y%22%3A+40.20194347%2C+%22spatialReference%22%3A+%7B%22wkid%22%3A+4326%7D%7D&geometryType=esriGeometryPoint&returnCatalogItems=true&maxItemCount=6&f=pjson"
        ],
        [
          "ODOT nearby bridge inventory query",
          "https://tims.dot.state.oh.us/ags/rest/services/Assets/Bridge_Inventory/MapServer/0/query?where=1%3D1&geometry=-83.16703364%2C40.20059600%2C-83.16350520%2C40.20329094&geometryType=esriGeometryEnvelope&inSR=4326&outFields=%2A&returnGeometry=true&outSR=4326&f=pjson"
        ],
        [
          "ODOT nearby conduit inventory query",
          "https://tims.dot.state.oh.us/ags/rest/services/Assets/Conduit_Inventory/MapServer/0/query?where=1%3D1&geometry=-83.16703364%2C40.20059600%2C-83.16350520%2C40.20329094&geometryType=esriGeometryEnvelope&inSR=4326&outFields=%2A&returnGeometry=true&outSR=4326&f=pjson"
        ]
      ]
    },
    "sources": [
      [
        "Delaware County utility and ROW permits",
        "https://engineer.co.delaware.oh.us/permits/"
      ],
      [
        "County and Concord Township permit assignments",
        "https://engineer.co.delaware.oh.us/permits/"
      ],
      [
        "Official flowline layer",
        "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0"
      ]
    ]
  },
  {
    "id": "S1-W12",
    "segment": "Segment1",
    "feature": "S1-S038-Bore",
    "station": 1308.8,
    "name": "Watkins Road unnamed stream near the quarry",
    "priority": "Asset and ROW",
    "method": "Separate narrow trenchless bore near SFN 8036640.",
    "blocker": "Exact stream hit about 82 ft from the structure. Haul-road access, ditch/pond extent and right-of-way are unresolved. FEMA lookup unavailable.",
    "lead": "Union County Engineer for CR-104 and SFN 8036640. Quarry operator/property controller for any work or access onto its land.",
    "conditional": "Local floodplain and Ohio water review for actual aquatic impact. Verify right-of-way from recorded plans before using it for privately operated facilities.",
    "submit": "Tie SFNs 8036640 and distinct 8031045 to route, survey drainage, roadway section and legal pits, submit haul/access protection and bore profile.",
    "fallback": "If quarry operator or county refuses the work area, relocate pits wholly to approved public frontage or secure a separate authorized easement and submit the revised profile.",
    "lat": 40.21316693,
    "lon": -83.20777554,
    "evidence": {
      "segment": "Segment1",
      "feature": "S1-S038-Bore",
      "station_ft": "1308.8",
      "latitude": "40.21316693",
      "longitude": "-83.20777554",
      "water_name": "",
      "layer_objectid": "22534",
      "water_fcode": "46003",
      "water_comid": "5214735",
      "water_permanent_id": "",
      "local_gis_angle_deg": "57.9",
      "county_place_township_screen": "UNION / unincorp. or blank / MILL CREEK",
      "sampled_road_lead": "Watkins Cr 00104 CR-104",
      "sampled_issuer_lead": "Union County Engineer",
      "nearby_structure_inventory_leads": "8036640 @ 82 ft (C104i WATKINS RD. / STREAM, maintain code 02)",
      "parcel_ids_at_point": "Union:1160000012002",
      "corridor_parcel_ids_within_100ft": "Union:1060000090001 | Union:1060000091000 | Union:1060000092000 | Union:1060000093000 | Union:1160000011000 | Union:1160000012002",
      "fema_at_point": "Unavailable",
      "nwi_within_100m": "Riverine R5UBH",
      "source_layer": "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0"
    },
    "review": {
      "classification": "buried",
      "confidence": "Medium",
      "finding": "ODOT SFN 8036640 identifies the Watkins Road culvert about 82 ft from the pin. Union County contract documents list twin 72-in concrete pipes for this SFN. Grading complicates the centerline tie in the aerial.",
      "next_check": "Survey both pipes and any altered approaches. Confirm the bore and pit limits against the current county asset footprint.",
      "image": "img/water-pin-audit/S1-W12.jpg",
      "imagery_catalog_dates": "2023-07-30",
      "proof": [
        [
          "Official flowline 22534",
          "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0/query?objectIds=22534&outFields=%2A&returnGeometry=true&outSR=4326&f=pjson"
        ],
        [
          "ODOT structure 8036640",
          "https://tims.dot.state.oh.us/ags/rest/services/Assets/Bridge_Inventory/MapServer/0/query?where=SFN+IN+%28%278036640%27%29&outFields=SFN%2CSTR_LOC_CARRIED%2CINVENT_FEAT%2CMAIN_STR_TYPE_CD%2CCULVERT_LEN%2CMAINT_RESP_CD&returnGeometry=true&outSR=4326&f=pjson"
        ],
        [
          "Union County Watkins structures, contract §19",
          "https://www.unioncountyohio.gov/media/Officials/Engineer/home/bid-info/2019HotMix_BidDocuments.pdf"
        ],
        [
          "Original USDA NAIP aerial",
          "https://imagery.nationalmap.gov/arcgis/rest/services/USGSNAIPImagery/ImageServer/exportImage?bbox=312024.431%2C4453654.729%2C312224.431%2C4453854.729&bboxSR=32617&imageSR=32617&size=540%2C540&format=jpg&f=image&interpolation=RSP_Bilinear"
        ],
        [
          "Ohio statewide aerial",
          "https://maps.ohio.gov/image/rest/services/osip_most_current/ImageServer/exportImage?bbox=312024.431%2C4453654.729%2C312224.431%2C4453854.729&bboxSR=32617&imageSR=32617&size=540%2C540&format=jpg&f=image&interpolation=RSP_Bilinear"
        ],
        [
          "USGS imagery catalog at pin",
          "https://imagery.nationalmap.gov/arcgis/rest/services/USGSNAIPImagery/ImageServer/identify?geometry=%7B%22x%22%3A+-83.20777554%2C+%22y%22%3A+40.21316693%2C+%22spatialReference%22%3A+%7B%22wkid%22%3A+4326%7D%7D&geometryType=esriGeometryPoint&returnCatalogItems=true&maxItemCount=6&f=pjson"
        ]
      ]
    },
    "sources": [
      [
        "Union County April 2026 utility requirements",
        "https://www.unioncountyohio.gov/media/Officials/Engineer/road-bridge/workwithinrwrequirements_2026_04_01.pdf"
      ],
      [
        "Official flowline layer",
        "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0"
      ]
    ]
  },
  {
    "id": "S1-W13",
    "segment": "Segment1",
    "feature": "S1-S038-Bore",
    "station": 12499.4,
    "name": "Watkins Ditch near SFN 8034036",
    "priority": "Asset and ROW",
    "method": "Independent bore under surveyed ditch and clear of structure.",
    "blocker": "Structure about 21 ft away. Need invert and cleanout/maintenance space and back of public ROW.",
    "lead": "Union County Engineer for road and structure. County drainage authority or ditch easement holder if maintenance or petitioned ditch is affected.",
    "conditional": "Floodplain, Huntington and Ohio EPA as site impacts trigger. Private easement if permitted ROW width or eligibility is inadequate.",
    "submit": "Ditch/culvert cross-section, ROW survey, approved depth below ditch bottom, entry/exit, preserved grade/outlets, restoration and access.",
    "fallback": "If approved cover or maintenance clearance cannot fit, shift to another authorized profile or obtain easement for off-ROW pits. Retain open channel grade and access.",
    "lat": 40.21235481,
    "lon": -83.24752819,
    "evidence": {
      "segment": "Segment1",
      "feature": "S1-S038-Bore",
      "station_ft": "12499.4",
      "latitude": "40.21235481",
      "longitude": "-83.24752819",
      "water_name": "",
      "layer_objectid": "22529",
      "water_fcode": "46003",
      "water_comid": "5214725",
      "water_permanent_id": "",
      "local_gis_angle_deg": "80.3",
      "county_place_township_screen": "UNION / unincorp. or blank / MILL CREEK",
      "sampled_road_lead": "Watkins Cr 00104 CR-104",
      "sampled_issuer_lead": "Union County Engineer",
      "nearby_structure_inventory_leads": "8034036 @ 21 ft (C104F WATKINS RD / WATKINS DITCH, maintain code 02)",
      "parcel_ids_at_point": "",
      "corridor_parcel_ids_within_100ft": "Union:1150102003000 | Union:1150102004000 | Union:1150102005000 | Union:1150102007000 | Union:1150103002000 | Union:1150103003000 | Union:1150103004000",
      "fema_at_point": "X AREA OF MINIMAL FLOOD HAZARD (39159C)",
      "nwi_within_100m": "Riverine R4SBC",
      "source_layer": "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0"
    },
    "review": {
      "classification": "buried",
      "confidence": "High",
      "finding": "Watkins Ditch approaches both sides of Watkins Road near SFN 8034036, about 21 ft from the pin. Union County lists twin 72-in concrete pipes for this asset.",
      "next_check": "Keep the ditch and both pipes in the profile. Verify headwall limits, maintenance access and clearance with Union County.",
      "image": "img/water-pin-audit/S1-W13.jpg",
      "imagery_catalog_dates": "2023-07-30",
      "proof": [
        [
          "Official flowline 22529",
          "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0/query?objectIds=22529&outFields=%2A&returnGeometry=true&outSR=4326&f=pjson"
        ],
        [
          "ODOT structure 8034036",
          "https://tims.dot.state.oh.us/ags/rest/services/Assets/Bridge_Inventory/MapServer/0/query?where=SFN+IN+%28%278034036%27%29&outFields=SFN%2CSTR_LOC_CARRIED%2CINVENT_FEAT%2CMAIN_STR_TYPE_CD%2CCULVERT_LEN%2CMAINT_RESP_CD&returnGeometry=true&outSR=4326&f=pjson"
        ],
        [
          "Union County Watkins structures, contract §19",
          "https://www.unioncountyohio.gov/media/Officials/Engineer/home/bid-info/2019HotMix_BidDocuments.pdf"
        ],
        [
          "Original USDA NAIP aerial",
          "https://imagery.nationalmap.gov/arcgis/rest/services/USGSNAIPImagery/ImageServer/exportImage?bbox=308639.018%2C4453649.544%2C308839.018%2C4453849.544&bboxSR=32617&imageSR=32617&size=540%2C540&format=jpg&f=image&interpolation=RSP_Bilinear"
        ],
        [
          "Ohio statewide aerial",
          "https://maps.ohio.gov/image/rest/services/osip_most_current/ImageServer/exportImage?bbox=308639.018%2C4453649.544%2C308839.018%2C4453849.544&bboxSR=32617&imageSR=32617&size=540%2C540&format=jpg&f=image&interpolation=RSP_Bilinear"
        ],
        [
          "USGS imagery catalog at pin",
          "https://imagery.nationalmap.gov/arcgis/rest/services/USGSNAIPImagery/ImageServer/identify?geometry=%7B%22x%22%3A+-83.24752819%2C+%22y%22%3A+40.21235481%2C+%22spatialReference%22%3A+%7B%22wkid%22%3A+4326%7D%7D&geometryType=esriGeometryPoint&returnCatalogItems=true&maxItemCount=6&f=pjson"
        ]
      ]
    },
    "sources": [
      [
        "Union County April 2026 utility requirements",
        "https://www.unioncountyohio.gov/media/Officials/Engineer/road-bridge/workwithinrwrequirements_2026_04_01.pdf"
      ],
      [
        "Official flowline layer",
        "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0"
      ]
    ]
  },
  {
    "id": "S1-W14",
    "segment": "Segment1",
    "feature": "S1-S039-Water",
    "station": 140.0,
    "name": "Branch of Mill Creek near SFN 8039187",
    "priority": "Asset and ROW",
    "method": "Independent HDD with dry access beyond mapped wetlands.",
    "blocker": "About 59 ft from SFN 8039187. NWI shows emergent and riverine areas. Need surveyed work footprint and lawful dry access. FEMA lookup unavailable.",
    "lead": "Union County Engineer for Watkins Road and structure. Confirm local floodplain authority for work limits.",
    "conditional": "Huntington and Ohio EPA if wetlands or channel are affected. Owner of affected drainage easement or frontage land.",
    "submit": "Bridge/culvert plans, wetland and effective FIRM, channel/bank and pit profile, access and temporary/permanent wetland impact table.",
    "fallback": "If either end has unacceptable wetland impacts, move to other authorized frontage or use a longer dry-land bore. If neither fits, compare new permitted ROW crossing or access rights.",
    "lat": 40.21227234,
    "lon": -83.2640484,
    "evidence": {
      "segment": "Segment1",
      "feature": "S1-S039-Water",
      "station_ft": "140.0",
      "latitude": "40.21227234",
      "longitude": "-83.2640484",
      "water_name": "",
      "layer_objectid": "22533",
      "water_fcode": "46003",
      "water_comid": "5214733",
      "water_permanent_id": "",
      "local_gis_angle_deg": "72.9",
      "county_place_township_screen": "UNION / unincorp. or blank / MILL CREEK",
      "sampled_road_lead": "Watkins Cr 00104 CR-104",
      "sampled_issuer_lead": "Union County Engineer",
      "nearby_structure_inventory_leads": "8039187 @ 59 ft (CR 104 F WATKINS R / BRANCH OF MILL CREEK, maintain code 02)",
      "parcel_ids_at_point": "Union:1140000002001",
      "corridor_parcel_ids_within_100ft": "Union:1040000036000 | Union:1140000002000 | Union:1140000002001",
      "fema_at_point": "Unavailable",
      "nwi_within_100m": "Freshwater Emergent Wetland PEM1C | Riverine R4SBC",
      "source_layer": "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0"
    },
    "review": {
      "classification": "open",
      "confidence": "High",
      "finding": "A winding branch of Mill Creek is visible at Watkins Road. ODOT SFN 8039187 is about 59 ft from the pin and Union County identifies a single-span concrete slab bridge.",
      "next_check": "Survey the bed, abutments, wetlands and legal pits. Compare an independent bore and structure option after the span owner checks clearance.",
      "image": "img/water-pin-audit/S1-W14.jpg",
      "imagery_catalog_dates": "2023-07-30",
      "proof": [
        [
          "Official flowline 22533",
          "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0/query?objectIds=22533&outFields=%2A&returnGeometry=true&outSR=4326&f=pjson"
        ],
        [
          "ODOT structure 8039187",
          "https://tims.dot.state.oh.us/ags/rest/services/Assets/Bridge_Inventory/MapServer/0/query?where=SFN+IN+%28%278039187%27%29&outFields=SFN%2CSTR_LOC_CARRIED%2CINVENT_FEAT%2CMAIN_STR_TYPE_CD%2CCULVERT_LEN%2CMAINT_RESP_CD&returnGeometry=true&outSR=4326&f=pjson"
        ],
        [
          "Union County Watkins structures, contract §19",
          "https://www.unioncountyohio.gov/media/Officials/Engineer/home/bid-info/2019HotMix_BidDocuments.pdf"
        ],
        [
          "Original USDA NAIP aerial",
          "https://imagery.nationalmap.gov/arcgis/rest/services/USGSNAIPImagery/ImageServer/exportImage?bbox=307232.818%2C4453676.145%2C307432.818%2C4453876.145&bboxSR=32617&imageSR=32617&size=540%2C540&format=jpg&f=image&interpolation=RSP_Bilinear"
        ],
        [
          "Ohio statewide aerial",
          "https://maps.ohio.gov/image/rest/services/osip_most_current/ImageServer/exportImage?bbox=307232.818%2C4453676.145%2C307432.818%2C4453876.145&bboxSR=32617&imageSR=32617&size=540%2C540&format=jpg&f=image&interpolation=RSP_Bilinear"
        ],
        [
          "USGS imagery catalog at pin",
          "https://imagery.nationalmap.gov/arcgis/rest/services/USGSNAIPImagery/ImageServer/identify?geometry=%7B%22x%22%3A+-83.2640484%2C+%22y%22%3A+40.21227234%2C+%22spatialReference%22%3A+%7B%22wkid%22%3A+4326%7D%7D&geometryType=esriGeometryPoint&returnCatalogItems=true&maxItemCount=6&f=pjson"
        ]
      ]
    },
    "sources": [
      [
        "Union County April 2026 utility requirements",
        "https://www.unioncountyohio.gov/media/Officials/Engineer/road-bridge/workwithinrwrequirements_2026_04_01.pdf"
      ],
      [
        "Official flowline layer",
        "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0"
      ]
    ]
  },
  {
    "id": "S1-W15",
    "segment": "Segment1",
    "feature": "S1-S040-Bore",
    "station": 10547.6,
    "name": "Hinderer Ditch at Watkins Road",
    "priority": "Asset and ROW",
    "method": "Independent bore at SFN 8030367 with outlet grade preserved.",
    "blocker": "Structure 27 ft away. Need culvert/outlet and existing pond access plus Marysville vs. county road decision and back of ROW.",
    "lead": "Union County Engineer for structure. Marysville Engineering for any city-controlled road work, after jurisdiction tie.",
    "conditional": "Drainage owner, property interest and Ohio water or floodplain approval if work limits trigger review.",
    "submit": "County structure plan, city/county work envelope, surveyed outlet and drive/farm access, back of ROW, bore section and staging.",
    "fallback": "If the owner rejects operations along the existing frontage, move the pits away from the inlet or private drive. Keep SFN 8033803 as a distinct structure check.",
    "lat": 40.21593461,
    "lon": -83.30188401,
    "evidence": {
      "segment": "Segment1",
      "feature": "S1-S040-Bore",
      "station_ft": "10547.6",
      "latitude": "40.21593461",
      "longitude": "-83.30188401",
      "water_name": "",
      "layer_objectid": "22530",
      "water_fcode": "46003",
      "water_comid": "5214727",
      "water_permanent_id": "",
      "local_gis_angle_deg": "81.7",
      "county_place_township_screen": "UNION / MARYSVILLE / DOVER",
      "sampled_road_lead": "Watkins Cr 00104 CR-104",
      "sampled_issuer_lead": "City of Marysville – maintains in-city rows of Watkins Rd; boundary rows shared with Union County Engineer",
      "nearby_structure_inventory_leads": "8030367 @ 27 ft (C104D WATKINS RD / HINDERER DITCH, maintain code 02)",
      "parcel_ids_at_point": "Union:1030000068000",
      "corridor_parcel_ids_within_100ft": "Union:1030000068000 | Union:1030000069000 | Union:1030000081000",
      "fema_at_point": "X AREA OF MINIMAL FLOOD HAZARD (39159C)",
      "nwi_within_100m": "Freshwater Pond PUBGh | Riverine R4SBC",
      "source_layer": "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0"
    },
    "review": {
      "classification": "buried",
      "confidence": "High",
      "finding": "Hinderer Ditch approaches Watkins Road at SFN 8030367, about 27 ft from the pin. Union County lists twin 144-in steel pipes. A nearby pond does not establish the outlet route.",
      "next_check": "Locate both barrels, aprons and the outlet. Confirm ditch maintenance access and keep the work envelope clear of the culvert.",
      "image": "img/water-pin-audit/S1-W15.jpg",
      "imagery_catalog_dates": "2023-07-30",
      "proof": [
        [
          "Official flowline 22530",
          "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0/query?objectIds=22530&outFields=%2A&returnGeometry=true&outSR=4326&f=pjson"
        ],
        [
          "ODOT structure 8030367",
          "https://tims.dot.state.oh.us/ags/rest/services/Assets/Bridge_Inventory/MapServer/0/query?where=SFN+IN+%28%278030367%27%29&outFields=SFN%2CSTR_LOC_CARRIED%2CINVENT_FEAT%2CMAIN_STR_TYPE_CD%2CCULVERT_LEN%2CMAINT_RESP_CD&returnGeometry=true&outSR=4326&f=pjson"
        ],
        [
          "Union County Watkins structures, contract §19",
          "https://www.unioncountyohio.gov/media/Officials/Engineer/home/bid-info/2019HotMix_BidDocuments.pdf"
        ],
        [
          "Original USDA NAIP aerial",
          "https://imagery.nationalmap.gov/arcgis/rest/services/USGSNAIPImagery/ImageServer/exportImage?bbox=304023.326%2C4454165.572%2C304223.326%2C4454365.572&bboxSR=32617&imageSR=32617&size=540%2C540&format=jpg&f=image&interpolation=RSP_Bilinear"
        ],
        [
          "Ohio statewide aerial",
          "https://maps.ohio.gov/image/rest/services/osip_most_current/ImageServer/exportImage?bbox=304023.326%2C4454165.572%2C304223.326%2C4454365.572&bboxSR=32617&imageSR=32617&size=540%2C540&format=jpg&f=image&interpolation=RSP_Bilinear"
        ],
        [
          "USGS imagery catalog at pin",
          "https://imagery.nationalmap.gov/arcgis/rest/services/USGSNAIPImagery/ImageServer/identify?geometry=%7B%22x%22%3A+-83.30188401%2C+%22y%22%3A+40.21593461%2C+%22spatialReference%22%3A+%7B%22wkid%22%3A+4326%7D%7D&geometryType=esriGeometryPoint&returnCatalogItems=true&maxItemCount=6&f=pjson"
        ]
      ]
    },
    "sources": [
      [
        "Union County April 2026 utility requirements",
        "https://www.unioncountyohio.gov/media/Officials/Engineer/road-bridge/workwithinrwrequirements_2026_04_01.pdf"
      ],
      [
        "Marysville Chapter 901",
        "https://www.marysvilleohio.org/documentview.aspx?did=303"
      ],
      [
        "Official flowline layer",
        "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0"
      ]
    ]
  },
  {
    "id": "S1-W16",
    "segment": "Segment1",
    "feature": "S1-S040-Bore",
    "station": 18554.3,
    "name": "Branch of Mill Creek near SFN 8037558",
    "priority": "Asset and ROW",
    "method": "Short separate trenchless crossing at the first OID 22519 hit.",
    "blocker": "SFN 8037558 is about 19 ft away. Need separate structure limits, developed frontage and ROW. The same hydro line appears twice more on the route.",
    "lead": "Union County Engineer for Watkins structure and road. Confirm Marysville role if field limits enter city-controlled frontage.",
    "conditional": "Private/access holder, local floodplain and Ohio water review if triggered. Drainage owner for maintenance clearance.",
    "submit": "Survey all three 22519 sites as a cluster, structure and ditch limits, each pit and connection, utility clashes and sufficient ROW.",
    "fallback": "If this profile is denied, shift locally or compare a corridor side that removes a recrossing. Demonstrate same endpoints and recheck the other two sites.",
    "lat": 40.23286361,
    "lon": -83.31106586,
    "evidence": {
      "segment": "Segment1",
      "feature": "S1-S040-Bore",
      "station_ft": "18554.3",
      "latitude": "40.23286361",
      "longitude": "-83.31106586",
      "water_name": "",
      "layer_objectid": "22519",
      "water_fcode": "46003",
      "water_comid": "5214705",
      "water_permanent_id": "",
      "local_gis_angle_deg": "74.8",
      "county_place_township_screen": "UNION / unincorp. or blank / DOVER",
      "sampled_road_lead": "Watkins Cr 00104 CR-104",
      "sampled_issuer_lead": "Union County Engineer",
      "nearby_structure_inventory_leads": "8037558 @ 19 ft (C104A WATKINS RD / BRANCH OF MILL CREEK, maintain code 02)",
      "parcel_ids_at_point": "Union:1030603003000",
      "corridor_parcel_ids_within_100ft": "Union:1030000035000 | Union:1030201017000 | Union:1030603003000 | Union:1030603004000",
      "fema_at_point": "X AREA OF MINIMAL FLOOD HAZARD (39159C)",
      "nwi_within_100m": "Riverine R4SBC",
      "source_layer": "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0"
    },
    "review": {
      "classification": "buried",
      "confidence": "High",
      "finding": "ODOT inventories a 48-ft culvert for a Mill Creek branch under Watkins Road, SFN 8037558 about 19 ft from the pin. This mapped reach crosses the alignment again at W17 under another structure.",
      "next_check": "Survey each culvert separately. Tie this barrel, its drainage footprint and the route station to the permit plan.",
      "image": "img/water-pin-audit/S1-W16.jpg",
      "imagery_catalog_dates": "2023-05-18, 2023-07-30",
      "proof": [
        [
          "Official flowline 22519",
          "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0/query?objectIds=22519&outFields=%2A&returnGeometry=true&outSR=4326&f=pjson"
        ],
        [
          "ODOT structure 8037558",
          "https://tims.dot.state.oh.us/ags/rest/services/Assets/Bridge_Inventory/MapServer/0/query?where=SFN+IN+%28%278037558%27%29&outFields=SFN%2CSTR_LOC_CARRIED%2CINVENT_FEAT%2CMAIN_STR_TYPE_CD%2CCULVERT_LEN%2CMAINT_RESP_CD&returnGeometry=true&outSR=4326&f=pjson"
        ],
        [
          "Union County drainage ditch maps",
          "https://www.unioncountyohio.gov/ditch-maps"
        ],
        [
          "Original USDA NAIP aerial",
          "https://imagery.nationalmap.gov/arcgis/rest/services/USGSNAIPImagery/ImageServer/exportImage?bbox=303290.912%2C4456065.175%2C303490.912%2C4456265.175&bboxSR=32617&imageSR=32617&size=540%2C540&format=jpg&f=image&interpolation=RSP_Bilinear"
        ],
        [
          "Ohio statewide aerial",
          "https://maps.ohio.gov/image/rest/services/osip_most_current/ImageServer/exportImage?bbox=303290.912%2C4456065.175%2C303490.912%2C4456265.175&bboxSR=32617&imageSR=32617&size=540%2C540&format=jpg&f=image&interpolation=RSP_Bilinear"
        ],
        [
          "USGS imagery catalog at pin",
          "https://imagery.nationalmap.gov/arcgis/rest/services/USGSNAIPImagery/ImageServer/identify?geometry=%7B%22x%22%3A+-83.31106586%2C+%22y%22%3A+40.23286361%2C+%22spatialReference%22%3A+%7B%22wkid%22%3A+4326%7D%7D&geometryType=esriGeometryPoint&returnCatalogItems=true&maxItemCount=6&f=pjson"
        ]
      ]
    },
    "sources": [
      [
        "Union County April 2026 utility requirements",
        "https://www.unioncountyohio.gov/media/Officials/Engineer/road-bridge/workwithinrwrequirements_2026_04_01.pdf"
      ],
      [
        "Marysville Chapter 901",
        "https://www.marysvilleohio.org/documentview.aspx?did=303"
      ],
      [
        "Official flowline layer",
        "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0"
      ]
    ]
  },
  {
    "id": "S1-W17",
    "segment": "Segment1",
    "feature": "S1-S041-Water",
    "station": 113.3,
    "name": "Branch of Mill Creek near SFN 8032904",
    "priority": "Asset and ROW",
    "method": "Design a separate trenchless crossing clear of the documented 50-ft culvert and its outlet.",
    "blocker": "SFN 8032904 is about 21 ft away and FEMA returned Zone A. Need local floodplain response, actual bank/pit limits and independent structure clearance.",
    "lead": "Union County Engineer for Watkins Road and structure. Local floodplain administrator for actual footprint.",
    "conditional": "Huntington and Ohio EPA where work triggers review. Property rights beyond the surveyed ROW.",
    "submit": "Show Zone A, bed/bank and culvert profile, stage and pit access, bore clearance and restoration. Mark separately from SFNs 8037558 and 8030530.",
    "fallback": "If the pit plan is refused, locate a dry receiving area beyond the mapped/work limits and extend the bore or test the other authorized road side.",
    "lat": 40.23265181,
    "lon": -83.31424043,
    "evidence": {
      "segment": "Segment1",
      "feature": "S1-S041-Water",
      "station_ft": "113.3",
      "latitude": "40.23265181",
      "longitude": "-83.31424043",
      "water_name": "",
      "layer_objectid": "22519",
      "water_fcode": "46003",
      "water_comid": "5214705",
      "water_permanent_id": "",
      "local_gis_angle_deg": "82.1",
      "county_place_township_screen": "UNION / unincorp. or blank / DOVER",
      "sampled_road_lead": "Watkins Cr 00104 CR-104",
      "sampled_issuer_lead": "Union County Engineer",
      "nearby_structure_inventory_leads": "8032904 @ 21 ft (C104A WATKINS RD / BRANCH OF MILLCREEK, maintain code 02)",
      "parcel_ids_at_point": "Union:1030603001000",
      "corridor_parcel_ids_within_100ft": "Union:1030000035000 | Union:1030000047000 | Union:1030603001000",
      "fema_at_point": "A  (39159C)",
      "nwi_within_100m": "Riverine R4SBC",
      "source_layer": "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0"
    },
    "review": {
      "classification": "buried",
      "confidence": "High",
      "finding": "SFN 8032904 is a separate 50-ft culvert at the second mapped hit on this Mill Creek branch, about 21 ft from the pin. The point screens into Zone A.",
      "next_check": "Survey this barrel and road outlet separately from W16. Resolve the Zone A footprint and show the independent bore clearance and legal pits.",
      "image": "img/water-pin-audit/S1-W17.jpg",
      "imagery_catalog_dates": "2023-05-18, 2023-07-30",
      "proof": [
        [
          "Official flowline 22519",
          "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0/query?objectIds=22519&outFields=%2A&returnGeometry=true&outSR=4326&f=pjson"
        ],
        [
          "ODOT structure 8032904",
          "https://tims.dot.state.oh.us/ags/rest/services/Assets/Bridge_Inventory/MapServer/0/query?where=SFN+IN+%28%278032904%27%29&outFields=SFN%2CSTR_LOC_CARRIED%2CINVENT_FEAT%2CMAIN_STR_TYPE_CD%2CCULVERT_LEN%2CMAINT_RESP_CD&returnGeometry=true&outSR=4326&f=pjson"
        ],
        [
          "Union County drainage ditch maps",
          "https://www.unioncountyohio.gov/ditch-maps"
        ],
        [
          "Original USDA NAIP aerial",
          "https://imagery.nationalmap.gov/arcgis/rest/services/USGSNAIPImagery/ImageServer/exportImage?bbox=303020.204%2C4456048.709%2C303220.204%2C4456248.709&bboxSR=32617&imageSR=32617&size=540%2C540&format=jpg&f=image&interpolation=RSP_Bilinear"
        ],
        [
          "Ohio statewide aerial",
          "https://maps.ohio.gov/image/rest/services/osip_most_current/ImageServer/exportImage?bbox=303020.204%2C4456048.709%2C303220.204%2C4456248.709&bboxSR=32617&imageSR=32617&size=540%2C540&format=jpg&f=image&interpolation=RSP_Bilinear"
        ],
        [
          "USGS imagery catalog at pin",
          "https://imagery.nationalmap.gov/arcgis/rest/services/USGSNAIPImagery/ImageServer/identify?geometry=%7B%22x%22%3A+-83.31424043%2C+%22y%22%3A+40.23265181%2C+%22spatialReference%22%3A+%7B%22wkid%22%3A+4326%7D%7D&geometryType=esriGeometryPoint&returnCatalogItems=true&maxItemCount=6&f=pjson"
        ]
      ]
    },
    "sources": [
      [
        "Union County April 2026 utility requirements",
        "https://www.unioncountyohio.gov/media/Officials/Engineer/road-bridge/workwithinrwrequirements_2026_04_01.pdf"
      ],
      [
        "Official flowline layer",
        "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0"
      ]
    ]
  },
  {
    "id": "S1-W18",
    "segment": "Segment1",
    "feature": "S1-S042-Bore",
    "station": 5658.8,
    "name": "Ruhl Ditch near SFN 8030530",
    "priority": "Asset and ROW",
    "method": "Clearance bore around the Watkins/Ruhl drainage asset.",
    "blocker": "Third OID 22519 hit, about 23 ft from the Ruhl Ditch structure. Need field identity, outlet clearance, road jurisdiction and proposed water-main overlap.",
    "lead": "Union County Engineer for structure, Marysville Engineering for city-controlled road work and water-main plan concurrence where applicable.",
    "conditional": "Drainage owner, local floodplain and Ohio water authorities as impacts warrant. Easement consent beyond public corridor.",
    "submit": "Ruhl Ditch plan, all three OID 22519 crossings, recorded Watkins ROW/ditch profile, Marysville utility overlay, screened pits and restoration.",
    "fallback": "If road or utility owner rejects this side, move the pit around the verified outlet or coordinate with Marysville’s work window. Reroute only after water and ROW rescreen.",
    "lat": 40.23404977,
    "lon": -83.33519708,
    "evidence": {
      "segment": "Segment1",
      "feature": "S1-S042-Bore",
      "station_ft": "5658.8",
      "latitude": "40.23404977",
      "longitude": "-83.33519708",
      "water_name": "",
      "layer_objectid": "22519",
      "water_fcode": "46003",
      "water_comid": "5214705",
      "water_permanent_id": "",
      "local_gis_angle_deg": "82.4",
      "county_place_township_screen": "UNION / MARYSVILLE / PARIS",
      "sampled_road_lead": "Watkins Cr 00104 CR-104",
      "sampled_issuer_lead": "City of Marysville – maintains in-city rows of Watkins Rd; boundary rows shared with Union County Engineer",
      "nearby_structure_inventory_leads": "8030530 @ 23 ft (CR104A WATKINS RD / RUHL DITCH, maintain code 02)",
      "parcel_ids_at_point": "Union:1020000014501",
      "corridor_parcel_ids_within_100ft": "Union:1020000008000 | Union:1020000013000 | Union:1020000014500 | Union:1020000014501",
      "fema_at_point": "X AREA OF MINIMAL FLOOD HAZARD (39159C)",
      "nwi_within_100m": "Riverine R4SBC",
      "source_layer": "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0"
    },
    "review": {
      "classification": "buried",
      "confidence": "High",
      "finding": "ODOT SFN 8030530 near Ruhl Road identifies a 48-ft culvert about 23 ft from the pin. The images show drainage approaches at the road and nearby developed frontage.",
      "next_check": "Tie surveyed headwalls to the Ruhl road profile. Overlay any municipal storm mains and preserve drainage and roadside access.",
      "image": "img/water-pin-audit/S1-W18.jpg",
      "imagery_catalog_dates": "2023-05-18",
      "proof": [
        [
          "Official flowline 22519",
          "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0/query?objectIds=22519&outFields=%2A&returnGeometry=true&outSR=4326&f=pjson"
        ],
        [
          "ODOT structure 8030530",
          "https://tims.dot.state.oh.us/ags/rest/services/Assets/Bridge_Inventory/MapServer/0/query?where=SFN+IN+%28%278030530%27%29&outFields=SFN%2CSTR_LOC_CARRIED%2CINVENT_FEAT%2CMAIN_STR_TYPE_CD%2CCULVERT_LEN%2CMAINT_RESP_CD&returnGeometry=true&outSR=4326&f=pjson"
        ],
        [
          "Original USDA NAIP aerial",
          "https://imagery.nationalmap.gov/arcgis/rest/services/USGSNAIPImagery/ImageServer/exportImage?bbox=301241.278%2C4456250.649%2C301441.278%2C4456450.649&bboxSR=32617&imageSR=32617&size=540%2C540&format=jpg&f=image&interpolation=RSP_Bilinear"
        ],
        [
          "Ohio statewide aerial",
          "https://maps.ohio.gov/image/rest/services/osip_most_current/ImageServer/exportImage?bbox=301241.278%2C4456250.649%2C301441.278%2C4456450.649&bboxSR=32617&imageSR=32617&size=540%2C540&format=jpg&f=image&interpolation=RSP_Bilinear"
        ],
        [
          "USGS imagery catalog at pin",
          "https://imagery.nationalmap.gov/arcgis/rest/services/USGSNAIPImagery/ImageServer/identify?geometry=%7B%22x%22%3A+-83.33519708%2C+%22y%22%3A+40.23404977%2C+%22spatialReference%22%3A+%7B%22wkid%22%3A+4326%7D%7D&geometryType=esriGeometryPoint&returnCatalogItems=true&maxItemCount=6&f=pjson"
        ]
      ]
    },
    "sources": [
      [
        "Union County April 2026 utility requirements",
        "https://www.unioncountyohio.gov/media/Officials/Engineer/road-bridge/workwithinrwrequirements_2026_04_01.pdf"
      ],
      [
        "Marysville Chapter 901",
        "https://www.marysvilleohio.org/documentview.aspx?did=303"
      ],
      [
        "Marysville Scottslawn–US 42 water main",
        "https://www.marysvilleohio.org/803/Scottslawn-To-US-42-Water-Main-Extension"
      ],
      [
        "Official flowline layer",
        "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0"
      ]
    ]
  }
];
