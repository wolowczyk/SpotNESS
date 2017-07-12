document.addEventListener("DOMContentLoaded", function() {
    document.getElementById('id_location').parentNode.style.display = 'none';
});

function initMap() {
var map = new google.maps.Map(document.getElementById('map'), {
  center: {lat: 53.577626, lng: 23.105803},
  zoom: 4
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

map.addListener('rightclick', function(e) {
    placeMarkerAndPanTo(e.latLng, map);
  });


function placeMarkerAndPanTo(latLng, map) {
  var marker = new google.maps.Marker({
    position: latLng,
    map: map,
  });
  map.panTo(latLng);
  var showPosition = document.querySelector("#id_location");
    id_location.value = '{lat: ' + latLng.lat() + ', lng: ' + latLng.lng() + '}'
}
}