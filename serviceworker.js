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


self.addEventListener('fetch', function(event) {
  event.respondWith(
    fetch(event.request).catch(function() {
      return caches.match(event.request);
    })
  );
});
    });


