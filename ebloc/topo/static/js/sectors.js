function onEachSector(feature, layer) {
    layer.on({
        click: zoomToFeature, openPopup,
    });
    sectors_layer.addLayer( layer );
}

//$.get(sectors_url,
//    function(data) {
//        const geoJson = JSON.parse(data);
//        sectors = L.geoJson(geoJson.features, {
//            style: function (feature) {
//                return {color: feature.properties.color};
//            },
//            onEachFeature: onEachSector
//        }).addTo(map);
//    });

