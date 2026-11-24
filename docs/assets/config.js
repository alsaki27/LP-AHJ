// Basemap configuration. Drop downloaded tiles into ./tiles/{z}/{x}/{y}.jpg (or .png) and set enabled:true.
window.BASEMAP = {
  enabled: true,                       // the app falls back to the plain vector background if tiles are missing
  imagery: { url: 'tiles/{z}/{x}/{y}.jpg', minZoom: 8, maxZoom: 18, attribution: 'Imagery: USGS / USDA FSA NAIP (public domain)' },
  // optional second basemap (e.g. roads/labels), same format
  streets: { url: 'tiles_streets/{z}/{x}/{y}.png', minZoom: 8, maxZoom: 18, attribution: '' }
};
