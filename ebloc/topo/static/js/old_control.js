
var info = L.control();

info.onAdd = function (map) {
    this._div = L.DomUtil.get('info');
    this.update();
    return this._div;
};

// method that we will use to update the control based on feature properties passed
info.update = function (props) {
var innerHTML_top = '', innerHTML_bottom = '', card_content = '', card_infos = '';

    if (props){
        innerHTML_top = `
            <div class="card" style="width: 18rem;">
              <div class="card-body">
                <h5 class="card-title">` + props.name + `</h5>`;

        innerHTML_bottom = `</div>
            </div>`;
    }
    if (props && props.cota) {
        var inc = (props.incontournable) ? '<i class="fa fa-star"></i> - ' : '';
        card_content = '<h4 class="card-title">'+ inc  + props.cota + '</h4> \n';
        card_infos += '<p>Expo: ' + props.expo + '/3</p>' ;

        if (props.da) {
            card_infos = '<p>Départ assis ' + props.da_cota + '</p>' ;
        }
        if (props.compression) {
            card_infos += '<p>Compression</p>' ;
        }
        if (props.elim) {
            card_infos += '<p>Elim</p>' ;
        }
        if (props.hauteur) {
            card_infos += '<p>Hauteur: ' + props.hauteur + 'm </p>' ;
        }
        if (props.inclin) {
            card_infos += '<p>Inclinaison: ' + props.inclin + '/5</p>' ;
        }
        if (props.jette) {
            card_infos += '<p>Jetté</p>' ;
        }
        if (props.morfo) {
            card_infos += '<p>Morpho</p>' ;
        }
        card_infos += '<p> Orientation: ' + props.orientation.toUpperCase() + '</p>' ;
        if (props.physique) {
            card_infos += '<p>Physique</p>' ;
        }
        if (props.plans) {
            card_infos += '<p>Plans</p>' ;
        }
        if (props.reglette) {
            card_infos += '<p>Reglette</p>' ;
        }
        if (props.reta) {
            card_infos += '<p>Retablissement</p>' ;
        }
        if (props.top) {
            card_infos += '<p>Top</p>' ;
        }
        if (props.touche) {
            card_infos += '<p>Touché</p>' ;
        }
        if (card_infos) {
            card_content = card_content + '<h6>Infos</h6>' + card_infos;
        }

    }

        this._div.innerHTML = innerHTML_top + card_content + innerHTML_bottom;
};

info.addTo(map);