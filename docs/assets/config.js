window.BASEMAPS = {
  hosted: [
    {
      name: 'Streets (OpenStreetMap)',
      url: 'https://tile.openstreetmap.org/{z}/{x}/{y}.png',
      maxNativeZoom: 19,
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap contributors</a>',
    },
    {
      name: 'Aerial (USGS)',
      url: 'https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}',
      maxNativeZoom: 16,
      attribution: '<a href="https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer">USDA, USGS The National Map: Orthoimagery</a>',
    },
  ],
  offline: [
    {
      name: 'Local aerial tiles',
      url: 'tiles/{z}/{x}/{y}.jpg',
      minZoom: 8,
      maxNativeZoom: 18,
      attribution: 'Imagery: USGS / USDA FSA NAIP',
    },
    {
      name: 'Local street tiles',
      url: 'tiles_streets/{z}/{x}/{y}.png',
      minZoom: 8,
      maxNativeZoom: 18,
    },
  ],
};
