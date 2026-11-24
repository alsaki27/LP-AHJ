window.addStreetViewPicker = function(map) {
  const container = map.getContainer();
  const control = L.control({position: 'topleft'});
  const person = L.marker([0, 0], {
    draggable: true,
    autoPan: true,
    keyboard: false,
    title: 'Drag to a road to open Street View',
    icon: L.divIcon({
      className: 'street-view-person',
      html: '<span aria-hidden="true">🚶</span>',
      iconSize: [32, 32],
      iconAnchor: [16, 30],
    }),
  });

  control.onAdd = () => {
    const panel = L.DomUtil.create('div', 'street-view-control');
    panel.innerHTML = `<button type="button" aria-pressed="false" aria-controls="street-view-instructions">
      <span aria-hidden="true">🚶</span> Street View</button>
      <div id="street-view-instructions" hidden>
        <p>Drag the person or select a road.</p>
        <button type="button" class="street-view-center">Use map center</button>
      </div>
      <a class="street-view-result" target="_blank" rel="noopener noreferrer" hidden>Reopen in Google Maps</a>`;
    const toggle = panel.querySelector('button');
    const instructions = panel.querySelector('#street-view-instructions');
    const result = panel.querySelector('.street-view-result');
    let picking = false;

    function setPicking(active) {
      picking = active;
      toggle.setAttribute('aria-pressed', String(active));
      instructions.hidden = !active;
      container.classList.toggle('street-view-picking', active);
      if (active) person.setLatLng(map.getCenter()).addTo(map);
      else person.remove();
    }

    function openAt({lat, lng}) {
      const url = streetViewLink(lat, lng);
      setPicking(false);
      result.href = url;
      result.hidden = false;
      window.open(url, '_blank', 'noopener,noreferrer');
    }

    L.DomEvent.disableClickPropagation(panel);
    L.DomEvent.disableScrollPropagation(panel);
    toggle.addEventListener('click', () => setPicking(!picking));
    panel.querySelector('.street-view-center').addEventListener('click', () => openAt(map.getCenter()));
    person.on('dragend', () => openAt(person.getLatLng()));

    container.addEventListener('click', event => {
      if (!picking || event.target.closest('.leaflet-control, .street-view-person')) return;
      event.preventDefault();
      event.stopPropagation();
      openAt(map.mouseEventToLatLng(event));
    }, true);

    container.addEventListener('keydown', event => {
      if (picking && event.key === 'Escape') {
        setPicking(false);
        toggle.focus();
      }
    });
    return panel;
  };
  control.addTo(map);
};
