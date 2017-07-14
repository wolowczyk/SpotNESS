function initMap() {
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

var spots = {{ spots_list | safe }};

for ( i = 0; i < spots.length; i++ ) {
var marker = new google.maps.Marker({
    position: new google.maps.LatLng(spots[i][1], spots[i][2]),
    map: map,
    url: spots[i][3],
  });
  google.maps.event.addListener(marker, 'click', function() {
    window.location.href = this.url;
});

  }
}