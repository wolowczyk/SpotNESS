function initMap() {
var pos = {
          lat: {{ point.lat }},
          lng: {{ point.lng }}
        };
var map = new google.maps.Map(document.getElementById('map'), {
  center: {lat: 52.26916667, lng: 20.90722222},
  zoom: 4
});
var marker = new google.maps.Marker({
  position: {lat: 52.26916667, lng: 20.90722222},
  map: map
});
}