function onEachSector(feature, layer) {
    layer.on({
        click: zoomToFeature, openPopup,
    });
}

let sectorLayerOptions = {
  style: function (feature) {
                return {color: feature.properties.color};
            },
  onEachFeature: onEachSector,
}

