// Editorial summaries for the director's four priority decisions.
// Crossing geometry, evidence fields, and permit details live in data/water.js.
window.directorDecisions = [
  {
    id: 'S1-W08',
    title: 'O’Shaughnessy Reservoir',
    decision: 'Advance the Home Road bridge attachment review.',
    finding: 'Located the County–Columbus bridge agreement and matched the crossing to SFN 2134462.',
    owner: 'Delaware County Structures and Columbus Watershed',
    next: 'Request inspection, conduit and attachment records. Confirm both approach rights. Carry a long HDD as the fallback.',
    image: 'img/aer_S1-S033-Water_2134462_40.19686_-83.13953.jpg',
    caption: 'Home Road bridge over the reservoir. The crop shows approach conditions and the SR 257 junction. Attachment capacity and approach rights require owner records.',
    proof: [
      ['County Commissioners’ Resolution 01-957, journal pp. 170–172', 'https://co.delaware.oh.us/wp-content/uploads/commissioners/journal/2001/jnlaug27.pdf', 'The adopted cooperative agreement addresses City-owned lands at portions of the bridge and approaches, City review for the replacement, County administration and shared Phase One maintenance.'],
      ['County bridge dedication and replacement record', 'https://co.delaware.oh.us/2024/11/19/home-road-bridge-renamed-in-honor-of-former-county-engineer/', 'The County identifies the Fred L. Stults Bridge and confirms the County–City collaboration to rebuild it.'],
    ],
  },
  {
    id: 'S0-W09',
    title: 'Alum Creek at Morse Road',
    decision: 'Choose a bore alignment with lawful pit access.',
    finding: 'Mapped the floodway and parcel 010-148992 at the hit. The roadway bridge, SFN 2535874, is about 70 ft away.',
    owner: 'Columbus Public Service, Franklin County Engineer and the affected land controller',
    next: 'Compare the existing-side HDD and road-side shift at matching tie-ins. Show both pit limits and property rights.',
    image: 'img/aer_S0-S016-Water-P01.jpg',
    caption: 'Morse Road and the Alum Creek corridor. The crop does not locate legal ROW or survey the bank and approach limits.',
    proof: [
      ['FEMA National Flood Hazard Layer', 'https://www.fema.gov/flood-maps/national-flood-hazard-layer', 'The point query returned Zone AE floodway on panel dataset 39049C. Approaches and work limits need a separate footprint check. The bundled point evidence identifies the tax parcel and bridge offset.'],
      ['Franklin County Engineer utility application', 'https://www.franklincountyengineer.org/wp-content/uploads/2016/04/Application-for-permit-pdf.pdf', 'The county utility review requires the proposed work and a plan tied to the specific road. The asset and land records determine which office controls each portion of the proposed work.'],
    ],
  },
  {
    id: 'CHI-W02',
    title: 'Salt Creek at Arlington Heights Road',
    decision: 'Keep HDD as the base and check bridge duct in parallel.',
    finding: 'Matched the route hit to Salt Creek and identified IDOT structure 016-3014.',
    owner: 'Cook County DoTH Permits and Structures',
    next: 'Get structure plans, confirm dry legal pits and floodway limits, and ask whether any usable bridge duct is available.',
    image: 'img/aer_T07.jpg',
    caption: 'Arlington Heights Road at Salt Creek. The mapped crossing is in the bridge area. Utility use and staging need separate review.',
    proof: [
      ['IDOT Structures inventory, OID 7553 / 016-3014', 'https://gis1.dot.illinois.gov/arcgis/rest/services/TrafficSafety/cis_LocationTool2026/MapServer/4', 'The inventory match identifies Arlington Heights Road over Salt Creek and reports a 62 ft overall structure length. The measurement describes the bridge. It cannot be used as the bore length.'],
      ['Cook County construction and maintenance permit intake', 'https://www.cookcountyil.gov/service/constructionmaintenance-permits', 'Cook DoTH accepts utility applications in PDF for County highway ROW and asks applicants to file two to three months ahead of when the permit is needed.'],
    ],
  },
  {
    id: 'S1-W01',
    title: 'Olentangy River at Home Road',
    decision: 'Compare attachment and HDD in parallel.',
    finding: 'Matched Home Road bridge SFN 2131870 with the scenic river and mapped floodway near SR 315.',
    owner: 'Delaware County Structures and USACE Huntington Regulatory',
    next: 'Submit both concepts with bridge and scour information, SR 315 approach limits, temporary access and ecological effects.',
    image: 'img/aer_S1-S029-Water_2131870_40.19408_-83.05225.jpg',
    caption: 'The Home Road crossing and SR 315 approach. Survey the work limits before assigning state, county or river approvals.',
    proof: [
      ['Delaware County Home Road / SR 315 project', 'https://engineer.co.delaware.oh.us/projects/home315/', 'County records describe widening Home Road and the Olentangy River bridge near the intersection.'],
      ['ODNR list of designated scenic rivers', 'https://ohiodnr.gov/discover-and-learn/safety-conservation/about-odnr/nature-preserves/scenic-rivers/list-ohio-scenic-rivers', 'The published scenic segment extends from below Delaware Dam to Old Wilson Bridge Road. Confirm method-specific scenic and aquatic review for the crossing.'],
    ],
  },
];

window.directorRoutes = [
  {key: 'Spurs', name: 'Chicago spurs', railLabel: 'Spurs', imageLabel: 'Spurs'},
  {key: 'Segment0', name: 'Segment 0', railLabel: 'Segment 0', imageLabel: 'Segment 0'},
  {key: 'Segment1', name: 'Segment 1', railLabel: 'Segment 1', imageLabel: 'Segment 1'},
].map(route => ({
  ...route,
  water: waterCount(route.key),
  rail: LP.report.rail.filter(row => row.Segment === route.railLabel &&
    row['Exact intersection'] === 'Y').length,
  images: LP.images.filter(row => row.seg === route.imageLabel).length,
}));

window.directorDecisionLinks = id => `<div class="brief-record-links">
  <a href="${waterRegisterLink(id)}">Crossing card</a>
  <a href="${waterMapLink(id)}">Map</a>
  <a href="research.html#proof-${encodeURIComponent(id)}">Proof</a>
</div>`;
