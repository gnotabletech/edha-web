var staticCacheName = 'edharulesandbiz-v1'
self.addEventListener('install', function(event){
    event.waitUntil(
        caches.open(staticCacheName).then(function(cache){
            return cache.addAll([
                "./templates/base_landing.html",
                "./static/assets/css/style.css",
                "./static/assets/css/styles.css",
                "./static/assets/css/signup.css",
                "./static/assets/js/bootstrap.min.js",
                "./static/assets/js/FormValidator.js",
                "./static/assets/js/jquery-3.2.1.min.map",
                "./static/assets/js/main.js",
                "./static/assets/js/scripts.js",
                "./static/assets/js/signup.js",
                "./static/assets/js/UserHome.js",
                "./static/assets/mp4/bg1.mp4",

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


