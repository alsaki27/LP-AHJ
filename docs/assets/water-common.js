// Keep the map, register, and older screening references tied to one set of crossing IDs.
window.waterById = new Map(WATER_CROSSINGS.map(crossing => [crossing.id, crossing]));
window.waterByLegacyId = new Map(Object.entries({
  R013: 'CHI-W02', R014: 'S0-W01', R015: 'S0-W03', R016: 'S1-W01',
  R017: 'S1-W08', R018: 'S1-W14', R019: 'S1-W17',
  L001: 'CHI-W03', L003: 'S0-W05', L004: 'S0-W06',
  L005: 'S0-W08', L006: 'S0-W09', L007: 'S0-W15',
}));
window.waterRegisterLink = id => 'water.html#' + encodeURIComponent(id);
window.waterMapLink = id => 'map.html#water=' + encodeURIComponent(id);
window.waterStation = value => value.toLocaleString('en-US', {
  minimumFractionDigits: 1, maximumFractionDigits: 1
});
window.waterCount = segment => WATER_CROSSINGS.filter(
  crossing => !segment || crossing.segment === segment
).length;

window.WATER_SITE_CLASSES = {
  open: { label: 'Open water / channel', symbol: 'W', color: '#0e7490' },
  buried: { label: 'Buried drainage', symbol: 'D', color: '#945113' },
  gis: { label: 'GIS hit only', symbol: '?', color: '#515a6a' },
};

window.waterSiteBadge = function(crossing) {
  const {classification, confidence} = crossing.review;
  return `<span class="water-site-badge ${classification}">${WATER_SITE_CLASSES[classification].label} · ${esc(confidence)}</span>`;
};

window.waterSiteSymbol = type =>
  `<span class="water-marker water-site-${type}" aria-hidden="true">${WATER_SITE_CLASSES[type].symbol}</span>`;

window.waterSiteReview = function(crossing) {
  const review = crossing.review;
  const links = review.proof.map(([label, url]) =>
    `<a href="${esc(url)}" target="_blank" rel="noopener noreferrer">${esc(label)}</a>`
  );
  return `<section class="water-site-review">
    ${waterSiteBadge(crossing)}
    <p>${esc(review.finding)}</p>
    <p><strong>Design check</strong> ${esc(review.next_check)}</p>
    <details class="water-proof"><summary>View aerial and source records</summary>
      <figure><a href="${esc(review.image)}" target="_blank" rel="noopener noreferrer" class="water-audit-image">
        <img src="${esc(review.image)}" loading="lazy" width="540" height="540" alt="USGS aerial centered on ${esc(crossing.id)}">
        </a><figcaption>Center ring marks the GIS pin. USGS / USDA NAIP, 200 m across.${review.imagery_catalog_dates
          ? ' Collection dates in the source catalog at the pin include ' + esc(review.imagery_catalog_dates) + '.'
          : ''} Imagery retrieved November 24, 2026.</figcaption></figure>
      <p class="water-links">${links.join(' · ')}</p>
    </details>
  </section>`;
};

window.waterDecision = function(crossing) {
  const fields = [
    ['Concept method pending site checks', crossing.method],
    ['What is blocking it', crossing.blocker],
    ['Who approves it', crossing.lead],
    ['Approvals that depend on the footprint', crossing.conditional],
    ['What to submit', crossing.submit],
    ['Fallback if rejected', crossing.fallback],
  ];
  return '<dl class="water-decision">' + fields.map(([label, value]) =>
    `<div><dt>${esc(label)}</dt><dd>${esc(value)}</dd></div>`
  ).join('') + '</dl>';
};

window.waterEvidence = function(crossing) {
  const point = crossing.evidence;
  const fields = [
    ['Coordinates', `${point.latitude}, ${point.longitude}`],
    ['Flowline', [`OID ${point.layer_objectid}`,
      point.water_comid && `COMID ${point.water_comid}`,
      point.water_permanent_id && `NHD ${point.water_permanent_id}`].filter(Boolean).join(' · ')],
    ['Local mapped angle', `${point.local_gis_angle_deg}°`],
    ['Road and location screen', [point.sampled_road_lead, point.county_place_township_screen].filter(Boolean).join(' · ')],
    ['Structure inventory leads', point.nearby_structure_inventory_leads || 'No nearby structure identified in this inventory screen'],
    ['FEMA at GIS point', point.fema_at_point],
    ['NWI within 100 m', point.nwi_within_100m],
    ['Parcel screen at point', point.parcel_ids_at_point || 'No tax parcel returned at point'],
    ['Parcel screen within 100 ft', point.corridor_parcel_ids_within_100ft || 'No parcel returned in corridor data'],
  ];
  const links = crossing.sources.map(([name, url]) =>
    `<a href="${esc(url)}" target="_blank" rel="noopener">${esc(name)}</a>`
  );
  return `<details class="water-evidence"><summary>Point evidence and sources</summary>
    <dl>${fields.map(([label, value]) => `<div><dt>${esc(label)}</dt><dd>${esc(value)}</dd></div>`).join('')}</dl>
    <p class="water-links">${links.join(' · ')}</p></details>`;
};
