
mapboxgl.accessToken =
  "pk.eyJ1IjoicmF5aGFuNTciLCJhIjoiY2tyMTc2bDhyMXpleDJ2dDk5cjlkdWwzNyJ9.wdlQcx9--Q-Mldi_9mPj1g"

navigator.geolocation.getCurrentPosition(successLocation, errorLocation, {
  enableHighAccuracy: true
})

function successLocation(position) {
  setupMap([position.coords.longitude, position.coords.latitude])
}

function errorLocation() { 
  setupMap([23.777176, 90.399452])
}

function setupMap(center) {
  const map = new mapboxgl.Map({
    container: "map",
    style: "mapbox://styles/mapbox/streets-v11",
    center: center,
    zoom: 15
  })

  const nav = new mapboxgl.NavigationControl()
  map.addControl(nav)

  var directions = new MapboxDirections({
    accessToken: mapboxgl.accessToken
  })

  map.addControl(directions, "top-left")

  map.addControl(new mapboxgl.GeolocateControl({
    positionOptions: {
        enableHighAccuracy: true
    },
    trackUserLocation: true,
    showUserHeading: true
  }));

  const marker = new mapboxgl.Marker()
      .setLngLat([23.746466, 90.376015])
      .addTo(map);
  //
  // // Set marker options.
  // const marker = new mapboxgl.Marker({
  //     color: "#ffffff",
  //     draggable: true
  // }).setLngLat([23.746466, 90.376015])
  //     .addTo(map);
}