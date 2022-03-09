var serviceWorkerPath = "/serviceworker.js";
 var edhaServiceWorker = registerServiceWorker(serviceWorkerPath);
 function registerServiceWorker(serviceWorkerPath){
    if('serviceWorker' in navigator){
      navigator.serviceWorker
        .register(serviceWorkerPath)
          .then(
            function(reg){
              console.log('edha service worker registered');
            }
          ).catch(function(error){
            console.log(error)
          });
    }
 }
var staticCacheName = 'edharulesandbiz-v1'
self.addEventListener('install', function(event){
    event.waitUntil(
        caches.open(staticCacheName).then(function(cache){
            return cache.addAll([
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

