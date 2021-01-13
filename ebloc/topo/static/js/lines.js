function onEachLine(feature, layer) {
    layer.on({
        mouseover: openPopup,
        mouseout: resetHighlight,
    });
        switch (feature.properties.calque) {
          case 1:
                f_layer.addLayer( layer );
            break;
            case 2:
                ad_layer.addLayer( layer );
            break;
            case 3:
                d_layer.addLayer( layer );
            break;
            case 4:
                td_layer.addLayer( layer );
            break;
            case 5:
                ed_layer.addLayer( layer );
            break;

        }
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

