var staticCacheName = 'edharulesandbiz-v1'
self.addEventListener('install', function(event){
    event.waitUntil(
        caches.open(staticCacheName).then(function(cache){
            return cache.addAll([
                "./static/assets/css/style.css",
                "./static/assets/css/styles.css",
                "./static/assets/vendor/aos/aos.css",
                "./static/assets/vendor/aos/aos.js",
                "./static/assets/css/floating-menu/style.css",
                "./static/assets/css/floating-search/style.css",
                "./static/assets/vendor/css/bootstrap.min.css",
                "./static/assets/js/bootstrap.min.js",
                "./static/assets/js/FormValidator.js",
                "./static/assets/js/jquery-3.2.1.min.map",
                "./static/assets/js/main.js",
                "./static/assets/js/scripts.js",
                "./static/assets/js/signup.js",
                "./static/assets/js/UserHome.js",
                "./static/assets/mp4/bg1.mp4",
                "./static/assets/mp4/bg1.mp4",
                "./404.html",
                "./500.html",
                "./base_landing.html",
                "./authenticate/base.html",
                "./edharules/base.html",

            ]);
        })
    );
});

var networkDataReceived = false;

startSpinner();

// fetch fresh data
var networkUpdate = fetch('/data.json').then(function(response) {
  return response.json();
}).then(function(data) {
  networkDataReceived = true;
  updatePage(data);
});

// fetch cached data
caches.match('/data.json').then(function(response) {
  if (!response) throw Error("No data");
  return response.json();
}).then(function(data) {
  // don't overwrite newer network data
  if (!networkDataReceived) {
    updatePage(data);
  }
}).catch(function() {
  // we didn't get cached data, the network is our last hope:
  return networkUpdate;
}).catch(showErrorMessage).then(stopSpinner());

self.addEventListener('fetch', function(event){
    var requestURL = new URL(event.request.url);
        if (requestURL.origin === location.origin){
            if((requestURL.pathname === "./")){
                event.respondWith(caches.match("./"));
                return;
            }
        }
        event.respondWith(
            caches.match(event.request).then(function(response){
                return response || fetch(event.request);
            })
        );
    });


