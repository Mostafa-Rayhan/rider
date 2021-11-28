// function initMap() {
//         	var location = {lat: 23.777176, lng: 90.399452
//         	};
//         	var map = new google.maps.Map(document.getElementById("map"), {
//         		zoom: 4,
//         		Center: location
//         	});
        
        	
//                 var marker = new google.maps.Marker({
// 			position: location,
// 			map: map,
// 			});
// 		};


function initMap() {
	var options = {
		zoom: 4,
		lat: 23.777176, lng: 90.399452
	}

	var map = new 
	google.maps.Map(document.getElementById("map"), options);


        
	var marker = new google.maps.Marker({
		position: {lat: 23.746466,lng: 90.376015},
		map: map,
		});

		var infoWindow = new google.maps.infoWindow({
			content: '<h1>Dhanmondi</h1>'
		});
	}

	// var marker = new mapboxgl.Marker()
	// 	.setLngLat([23.746466, 90.376015])
	// 	.addTo(map);