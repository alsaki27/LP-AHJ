nav('water.html');

const segmentOrder = ['Spurs', 'Segment0', 'Segment1'];
const scope = $('#water-scopes');
const search = $('#water-search');
const register = $('#water-register');
const exportButton = $('#water-export');
let segment = '';
let visible = [];

const indexed = WATER_CROSSINGS.map(crossing => ({
  crossing,
  searchText: Object.values(crossing).filter(value => typeof value === 'string')
    .concat(Object.values(crossing.evidence)).join(' ').toLowerCase(),
}));

function crossingCard(crossing) {
  return `<article class="water-card" id="${esc(crossing.id)}" tabindex="-1">
    <header><div>
      <div class="note">${esc(crossing.id)} · ${esc(crossing.feature)} · ${waterStation(crossing.station)} ft</div>
      <h3>${esc(crossing.name)}</h3>
    </div><span class="water-priority">${esc(crossing.priority)}</span></header>
    ${waterDecision(crossing)}
    ${waterEvidence(crossing)}
    <p class="water-links"><a href="${waterMapLink(crossing.id)}">View crossing on map</a> ·
    <a href="${esc(streetViewLink(crossing.lat, crossing.lon))}" target="_blank" rel="noopener noreferrer">Google Street View</a></p>
  </article>`;
}

function render() {
  const term = search.value.toLowerCase().trim();
  visible = indexed.filter(({crossing, searchText}) =>
    (!segment || crossing.segment === segment) && (!term || searchText.includes(term))
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
$('#water-print').addEventListener('click', () => print());
exportButton.addEventListener('click', () => {
  csv(visible.map(crossing => ({
    id: crossing.id, segment: SEGS[crossing.segment], feature: crossing.feature,
    station_ft: crossing.station, crossing: crossing.name, priority: crossing.priority,
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
