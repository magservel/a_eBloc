function printInfo(e) {
    sidebar = L.DomUtil.get('sidebar');
    sidebar.classList.toggle('collapsed', false);
    tab_info = L.DomUtil.get('tab_info');
    tab_info.classList.toggle('active', true);
    info = L.DomUtil.get('info');
    info.classList.toggle('active', true);
    info.innerHTML = e.target.feature.properties.printInfo;
}

function onEachLine(feature, layer) {
    layer.on({
        click: printInfo,
    });
}

function createCustomIcon (feature, latlng) {

    var colors = ['white', 'green', 'blue', 'red', 'black', 'gold']
    var iconColor = colors[feature.properties.calque];



lineIconOptions = {
    iconShape: 'circle-dot',
    borderColor: 'white',
    backgroundColor: iconColor,
    iconSize: [16,16]
};

  myIcon = L.BeautifyIcon.icon(lineIconOptions)
  return L.marker(latlng, { icon: myIcon })
}

// create an options object that specifies which function will called on each feature
let lineLayerOptions = {
  pointToLayer: createCustomIcon,
  onEachFeature: onEachLine,
}

//$.get(lines_url,
//    function(data) {
//        const geoJson = JSON.parse(data);
//        lines = L.geoJson(geoJson.features, lineLayerOptions).addTo(map);
//    });

