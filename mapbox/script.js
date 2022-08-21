mapboxgl.accessToken =
  "pk.eyJ1IjoiYXJhdmluZGthbm5hbjAxIiwiYSI6ImNsNzJ5dHp4NTExaXkzb3NiYXhraXYwdnQifQ.XHZ07PcTPU6ff2qxg8bcRQ";

navigator.geolocation.getCurrentPosition(
  (position) => {
    console.log(position);
    setupMap([position.coords.longitude, position.coords.latitude]);
  },
  () => {},
  {
    enableHighAccuracy: true,
  }
);


let map = "";
function setupMap(center) {
  map = new mapboxgl.Map({
    container: "map",
    style: "mapbox://styles/mapbox/streets-v11",
    center: center,
    zoom: 10,
  });

  const nav = new mapboxgl.NavigationControl();
  map.addControl(nav, "top-right");

  let coord = [61.1022, 2.2406, 91.813, 22.1423];

  map.on("load", () => {
    map.addSource("radar", {
      type: "image",
      url: `https://api.mapbox.com/styles/v1/mapbox/satellite-v9/static/[${coord}]/300x200@2x?access_token=pk.eyJ1IjoiYXJhdmluZGthbm5hbjAxIiwiYSI6ImNsNzJ5dHp4NTExaXkzb3NiYXhraXYwdnQifQ.XHZ07PcTPU6ff2qxg8bcRQ`,
      coordinates: [
        [coord[0], coord[3]],
        [coord[2], coord[3]],
        [coord[2], coord[1]],
        [coord[0], coord[1]],
      ],
    });
    map.addLayer({
      id: "radar-layer",
      type: "raster",
      source: "radar",
      paint: {
        "raster-fade-duration": 0,
      },
    });
  });
}

let cities = {
  chennai: [80.2707, 13.0827],
  mumbai: [72.8777, 19.076],
  kolkata: [88.3639, 22.5726],
};

function moveTo(city) {
  console.log(city);
  map.flyTo({
    center: cities[city],
    essential: true,
  });
}

document
  .getElementById("chennai")
  .addEventListener("click", () => moveTo("chennai"));
document
  .getElementById("mumbai")
  .addEventListener("click", () => moveTo("mumbai"));
document
  .getElementById("kolkata")
  .addEventListener("click", () => moveTo("kolkata"));
