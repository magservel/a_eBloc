var map = L.map('map').setView([42.4959, 1.9826], 15);

            L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
            }).addTo(map);

            var locate = L.control.locate().addTo(map);
            var sidebar = L.control.sidebar('sidebar').addTo(map);

            var lines = {{ lines|safe }};
//            var others = {{ others|safe }};
//            var sectors = {{ sectors|safe }};

            var lines_geom = L.geoJson(lines.features, lineLayerOptions).addTo(map);
//            var others_geom = L.geoJson(others.features, infoLayerOptions).addTo(map);
//            var sectors_geom = L.geoJson(sectors.features, {
//                style: function (feature) {
//                    return {color: feature.properties.color};
//                },
//            }).addTo(map);