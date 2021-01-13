function onEachInfo(feature, layer) {
    layer.on({
        mouseover: openPopup,
        mouseout: resetHighlight,
    });
    others_layer.addLayer( layer );
}

parkingIconOptions = {
    icon: 'parking',
    prefix: 'fa',
    iconShape: 'marker',
    borderColor: 'blue',
    textColor: 'blue',
};

campingIconOptions = {
    icon: 'campground',
    prefix: 'fa',
    iconShape: 'marker',
    borderColor: 'green',
    textColor: 'green',
};

function createCustomIcon (feature, latlng) {
    if (feature.properties.type == 1) {
        infoIcon = L.BeautifyIcon.icon(parkingIconOptions)
    } else {
        infoIcon = L.BeautifyIcon.icon(campingIconOptions)
    }

  return L.marker(latlng, { icon: infoIcon })
}

// create an options object that specifies which function will called on each feature
let infoLayerOptions = {
  pointToLayer: createCustomIcon,
  onEachFeature: onEachInfo,
}

//$.get(others_url,
//    function(data) {
//        const geoJson = JSON.parse(data);
//        others = L.geoJson(geoJson.features, infoLayerOptions).addTo(map);
//    });

