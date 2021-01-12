function openPopup(e) {
    e.target.bindPopup(e.target.feature.properties.name).openPopup();
}

function resetHighlight(e) {
    e.target.closePopup();
}

function zoomToFeature(e) {
    map.fitBounds(e.target.getBounds());
    openPopup(e);
}