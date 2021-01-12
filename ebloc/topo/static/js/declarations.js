var sectors_url = "{% url 'get_all_sectors' %}";
var others_url = "{% url 'get_all_others' %}";
var lines_url = "{% url 'get_all_lines' %}";
var line_url = "{% url 'get_line' %}";

var map = L.map('map').setView([42.4959, 1.9826], 15);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

L.control.locate().addTo(map);


 var others, others_layer = L.layerGroup().addTo(map);
 var sectors, sectors_layer = L.layerGroup().addTo(map);
 var lines;
 var f_layer = L.layerGroup().addTo(map);
 var ad_layer = L.layerGroup().addTo(map);
 var d_layer = L.layerGroup().addTo(map);
 var td_layer = L.layerGroup().addTo(map);
 var ed_layer = L.layerGroup().addTo(map);