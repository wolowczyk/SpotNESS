document.addEventListener("DOMContentLoaded", function() {
    document.getElementById('id_lat').parentNode.style.display = 'none';
    document.getElementById('id_lng').parentNode.style.display = 'none';
});

function initMap() {
var map = new google.maps.Map(document.getElementById('map'), {
  center: {lat: 53.577626, lng: 23.105803},
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
      }, function() {
        handleLocationError(true, infoWindow, map.getCenter());
      });
    } else {
      handleLocationError(false, infoWindow, map.getCenter());
    }

var marker;

function placeMarkerAndPanTo(latLng, map) {
  if ( marker ) {
    marker.setPosition(latLng);
  } else {
    marker = new google.maps.Marker({
      position: latLng,
      map: map,
      draggable: true,
    });
    map.panTo(latLng);
    id_lat.value = latLng.lat();
    id_lng.value = latLng.lng();
  }
}

map.addListener('rightclick', function(e) {
    placeMarkerAndPanTo(e.latLng, map);
});
}
