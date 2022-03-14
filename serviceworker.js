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
                "./static/assets/vendor/purecounter/purecounter.js",
                "./static/assets/js/bootstrap.min.js",
                "./static/assets/js/FormValidator.js",
                "./static/assets/js/jquery-3.2.1.min.map",
                "./static/assets/js/scripts.js",
                "./static/assets/js/signup.js",
                "./static/assets/js/UserHome.js",
                "./static/assets/mp4/bg1.mp4",
                "./",

            ]);
        })
    );
});


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

self.addEventListener('activate', function(event) {
  event.waitUntil(
    caches.keys().then(function(cacheNames) {
      return Promise.all(
        cacheNames.filter(function(cacheName) {
          // Return true if you want to remove this cache,
          // but remember that caches are shared across
          // the whole origin
        }).map(function(cacheName) {
          return caches.delete(cacheName);
        })
      );
    })
  );
});


