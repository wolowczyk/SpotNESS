document.addEventListener("DOMContentLoaded", function(event) {
lat = document.querySelector('#point_lat');
lng = document.querySelector('#point_lng');
lat.style.display = "none";
lng.style.display = "none";

initMap = function() {
var pos = {
          lat: parseFloat(lat.innerHTML),
          lng: parseFloat(lng.innerHTML),
        };
var map = new google.maps.Map(document.getElementById('map-detail'), {
  center: pos,
  zoom: 15
});
var marker = new google.maps.Marker({
  position: pos,
  map: map
});
};
});

