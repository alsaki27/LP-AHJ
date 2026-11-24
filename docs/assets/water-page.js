nav('water.html');

const segmentOrder = ['Spurs', 'Segment0', 'Segment1'];
const scope = $('#water-scopes');
const search = $('#water-search');
const setting = $('#water-type');
const register = $('#water-register');
const exportButton = $('#water-export');
let segment = '';
let visible = [];

const indexed = WATER_CROSSINGS.map(crossing => ({
  crossing,
  searchText: Object.values(crossing).filter(value => typeof value === 'string')
    .concat(Object.values(crossing.evidence), crossing.review.finding, crossing.review.next_check,
      crossing.review.followup?.record_search || '')
    .join(' ').toLowerCase(),
}));

Object.entries(WATER_SITE_CLASSES).forEach(([key, {label}])=>setting.add(new Option(label, key)));

const siteTypes = Object.keys(WATER_SITE_CLASSES);
const countByType = (type, route) => WATER_CROSSINGS.filter(crossing =>
  crossing.review.classification === type && (!route || crossing.segment === route)
).length;
$('#water-audit-index').innerHTML = `<table class="t water-audit-table"><caption>Physical review by segment</caption>
  <thead><tr><th scope="col">Segment</th>${Object.values(WATER_SITE_CLASSES).map(({label})=>`<th scope="col">${label}</th>`).join('')}</tr></thead>
  <tbody>${segmentOrder.map(key=>`<tr><th scope="row">${esc(SEGS[key])}</th>${siteTypes.map(type=>
    `<td>${countByType(type, key)}</td>`).join('')}</tr>`).join('')}</tbody>
  <tfoot><tr><th scope="row">Total</th>${siteTypes.map(type=>`<td>${countByType(type)}</td>`).join('')}</tr></tfoot>
  </table>
  <p><a href="data/water_pin_audit.csv" download>Download the 36-pin audit</a> ·
  <a href="data/water_drainage_followup.csv" download>Download the 10-pin drainage follow-up</a></p>`;

function crossingCard(crossing) {
  const {lat,lon}=waterMapPosition(crossing);
  return `<article class="water-card" id="${esc(crossing.id)}" tabindex="-1">
    <header><div>
      <div class="note">${esc(crossing.id)} · ${esc(crossing.feature)} · ${waterStation(crossing.station)} ft</div>
      <h3>${esc(crossing.name)}</h3>
    </div><span class="water-priority">${esc(crossing.priority)}</span></header>
    ${waterSiteReview(crossing)}
    ${waterRelatedLeads(crossing.id)}
    ${waterDecision(crossing)}
    ${waterEvidence(crossing)}
    <p class="water-links"><a href="${waterMapLink(crossing.id)}">View crossing on map</a> ·
    <a href="${esc(streetViewLink(lat, lon))}" target="_blank" rel="noopener noreferrer">Google Street View</a></p>
  </article>`;
}

function render() {
  const term = search.value.toLowerCase().trim();
  visible = indexed.filter(({crossing, searchText}) =>
    (!segment || crossing.segment === segment) &&
    (!setting.value || crossing.review.classification === setting.value) &&
    (!term || searchText.includes(term))
  ).map(({crossing}) => crossing);

  register.innerHTML = segmentOrder.map(key => {
    const matches = visible.filter(crossing => crossing.segment === key);
    if (!matches.length) return '';
    return `<section aria-label="${esc(SEGS[key])}">
      <h2>${esc(SEGS[key])} <span class="note">${matches.length} of ${waterCount(key)} points</span></h2>
      ${matches.map(crossingCard).join('')}
    </section>`;
  }).join('') || '<p>No crossings match this search.</p>';

  for (const button of scope.querySelectorAll('button')) {
    const selected = button.dataset.segment === segment;
    button.classList.toggle('on', selected);
    button.setAttribute('aria-pressed', String(selected));
  }
  $('#water-result').textContent = `${visible.length} of ${waterCount()} mapped points`;
  exportButton.disabled = visible.length === 0;
}

scope.innerHTML = ['', ...segmentOrder].map(key =>
  `<button type="button" data-segment="${key}">${SEGS[key] || 'All segments'} · ${waterCount(key)}</button>`
).join('');
for (const button of scope.querySelectorAll('button')) {
  button.addEventListener('click', () => {
    segment = button.dataset.segment;
    history.replaceState(null, '', location.pathname + location.search);
    render();
  });
}
search.addEventListener('input', render);
setting.addEventListener('change', render);
$('#water-print').addEventListener('click', () => print());
exportButton.addEventListener('click', () => {
  csv(visible.map(crossing => ({
    id: crossing.id, segment: SEGS[crossing.segment], feature: crossing.feature,
    station_ft: crossing.station, crossing: crossing.name, priority: crossing.priority,
    physical_setting: WATER_SITE_CLASSES[crossing.review.classification].label,
    confidence: crossing.review.confidence, physical_finding: crossing.review.finding,
    design_check: crossing.review.next_check, aerial_file: crossing.review.image,
    drainage_bid_decision: crossing.review.followup?.decision || '',
    asset_station_ft: crossing.review.followup?.tie?.station ?? '',
    asset_latitude: crossing.review.followup?.tie?.lat ?? '',
    asset_longitude: crossing.review.followup?.tie?.lon ?? '',
    physical_sources: crossing.review.proof.map(([, url]) => url),
    working_method: crossing.method, blocker: crossing.blocker, approval_lead: crossing.lead,
    conditional_approvals: crossing.conditional, submission: crossing.submit,
    fallback: crossing.fallback, latitude: crossing.lat, longitude: crossing.lon,
    flowline_oid: crossing.evidence.layer_objectid, fema_at_point: crossing.evidence.fema_at_point,
    nearby_structure: crossing.evidence.nearby_structure_inventory_leads,
    nearby_nwi: crossing.evidence.nwi_within_100m, source_urls: crossing.sources.map(([, url]) => url),
  })), 'water_crossing_decisions.csv');
});

function focusCrossing() {
  const id = location.hash.slice(1);
  const crossing = waterById.get(id);
  if (crossing) {
    segment = crossing.segment;
    search.value = '';
    setting.value = '';
  }
  render();
  if (crossing) {
    const card = document.getElementById(id);
    card.focus({preventScroll: true});
    card.scrollIntoView({block: 'start'});
  }
}
window.addEventListener('hashchange', focusCrossing);
focusCrossing();
