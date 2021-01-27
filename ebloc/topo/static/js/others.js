function onEachInfo(feature, layer) {
    layer.on({
        //click: printInfo,
    });
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

let otherLayerOptions = {
  pointToLayer: createCustomIcon,
  onEachFeature: onEachInfo,
}


