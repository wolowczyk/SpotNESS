initMap = function() {
    var map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: 0, lng: 0},
        zoom: 2
    });

    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function(position) {
            var pos = {
                lat: position.coords.latitude,
                lng: position.coords.longitude
            };
            map.setCenter(pos);
            map.setZoom(11);
        });
    }
    document.getElementById("spots_list").style.display = "none";
    var spots = document.getElementsByClassName('spot_spot');
    var lat_list = document.getElementsByClassName("spot_lat");
    var lng_list = document.getElementsByClassName("spot_lng");
    var url_list = document.getElementsByClassName("spot_url");

    for ( i = 0; i < spots.length; i++ ) {
        var marker = new google.maps.Marker({
            position: new google.maps.LatLng(parseFloat(lat_list[i].innerHTML), parseFloat(lng_list[i].innerHTML)),
            map: map,
            url: url_list[i].innerHTML,
        });
        google.maps.event.addListener(marker, 'click', function() {
            window.location.href = this.url;
        });
    }
}