window.WATER_CROSSINGS = [
  {
    "id": "CHI-W01",
    "segment": "Spurs",
    "feature": "Spur1-S01-Bore",
    "station": 1615.4,
    "name": "Devon Avenue drainage near Arlington Heights Road",
    "priority": "Asset and ROW",
    "method": "Short trenchless clearance bore after drainage locate.",
    "blocker": "No confirmed pipe or open channel at the mapped hit. The Devon and Arlington Heights road-leg limits and the dry workspace beside the mapped pond remain unresolved.",
    "lead": "DuPage DOT Highway Permits for county road work. Itasca Engineering for village ROW or drainage. Ask both to assign the controller using the plan and recorded ROW.",
    "conditional": "Drainage asset owner for clearance. IDNR and USACE Chicago if the field survey shows regulated water or floodway work. Illinois EPA if the federal authorization and discharge trigger certification.",
    "submit": "Dimension surveyed drainage and possible pipe inverts, road transition, ROW document 507662, nearby pond/outlet, bore and pit locations, traffic and restoration. Ask for both agencies’ jurisdiction limits in writing.",
    "fallback": "If the intersection position or pits are rejected, test a short shift along the owner-confirmed road leg. If the line is a pipe, use a separate bore outside its structural envelope. If it is open and the shift still affects the pond, move to a surveyed upland landfall with access rights.",
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
    "sources": [
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
    "method": "Engineered HDD below surveyed bed and scour.",
    "blocker": "The route point is about 125 ft from SFN 4538323. Exact road controller, structure footprint, legal landfalls, scour and dry pits still need proof.",
    "lead": "Licking County Engineer/Commissioners and New Albany Public Service assign the relevant CR-162 road and structure approvals under the applicable agreement.",
    "conditional": "Local floodplain administrator and Huntington Regulatory for actual reach and impacts. Ohio EPA if certification or isolated wetland authorization is required. Landowners for work outside documented ROW.",
    "submit": "SFN 4538323 plans and CR-162 control limits, station tie, banks/scour, bore section, utility and easement exhibit, access and disturbance table.",
    "fallback": "If the current HDD workspace is refused, shift toward an owner-controlled local corridor. Check licensed duct or structural attachment at SFN 4538323 only after field ties and owner approval.",
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
    "method": "Field-trace the active drainage, then bore outside final project grading.",
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
    "method": "Short independent trenchless crossing after pipe/channel locate.",
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
    "method": "Shorter, closer-to-normal bore within authorized Sancus frontage.",
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
    "method": "Independent bore with pits outside outlet and pond maintenance areas.",
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
    "method": "Short local realignment toward a steeper crossing angle.",
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
    "method": "Clear an ODOT drainage asset by bore if inside state ROW, otherwise use approved local or private corridor.",
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
    "method": "Short trenchless crossing in surveyed drainage envelope.",
    "blocker": "GIS hit is near-normal. Need confirmation of drain/culvert alignment and ODOT access-control and work area limitations. FEMA Zone X at this point leaves pits and access to check.",
    "lead": "ODOT District 6 for verified state ROW and drainage occupancy. Confirm controller on plans before applying.",
    "conditional": "Metro Parks or title holder if work leaves verified ROW. Local floodplain and Ohio water approvals if actual footprint triggers them.",
    "submit": "ODOT drainage/as-built and access-control sheets, slope/bed and utility profile, exact ROW, bore/pits, restoration and access justification.",
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
    "method": "Test a less oblique, shorter crossing in the road corridor.",
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
    "method": "Straighter local HDD across the drainage.",
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
    "method": "Bore the field-located drainage and keep two nearby structure checks open.",
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
    "method": "Independent short bore pending linkage with SFN 2133709.",
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
    "method": "Separate HDD at the second OID 22519 hit.",
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
