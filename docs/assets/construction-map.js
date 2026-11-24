// Public project limits matched to ODOT road centerlines.
const constructionLocations = {
  'SEG0C-03': {
    points: [[-82.992817, 40.087758], [-82.981104, 40.087361]],
    source: 'https://engage.columbus.gov/161safetyimprovements',
  },
  'SEG1U-04': {
    points: [[-83.356633, 40.235836]],
    source: 'https://www.marysvilleohio.org/Archive/ViewFile/Item/6268',
  },
};

function constructionView(project) {
  const locations = constructionLocations[project.id];
  if (locations) return {...locations, label: 'Published location matched to road GIS'};
  if (project.type === 'moratorium') {
    const routes = LP.route_lines.filter(route => project.features?.includes(route.f));
    if (routes.length) return {routes, label: 'Route features flagged for pavement restrictions'};
  }
  return project.ll ? {points: [project.ll], label: 'Route reference point · see card for project limits'} : null;
}

function constructionMapLink(id) {
  return 'map.html#construction=' + encodeURIComponent(id);
}
