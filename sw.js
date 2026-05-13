// Bump this when shipping changes to force clients to refresh the cache.
const CACHE = 'applied-inversion-v4';
const ASSETS = [
  './',
  './index.html',
  './manifest.webmanifest',
  './icons/icon.svg',
  './icons/icon-192.png',
  './icons/icon-512.png',
  './icons/icon-maskable-512.png',
  './icons/favicon-32.png',
];

// Cross-origin URL prefixes we are willing to cache (muxer libs loaded at runtime).
const EXTERNAL_ALLOWED = [
  'https://cdn.jsdelivr.net/npm/mp4-muxer@',
  'https://cdn.jsdelivr.net/npm/webm-muxer@',
  'https://cdn.jsdelivr.net/npm/gifenc@',
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE).then((cache) => cache.addAll(ASSETS))
  );
  self.skipWaiting();
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(keys.filter((k) => k !== CACHE).map((k) => caches.delete(k)))
    ).then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (event) => {
  const req = event.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);
  const sameOrigin = url.origin === self.location.origin;
  const externalAllowed = EXTERNAL_ALLOWED.some((p) => req.url.startsWith(p));
  if (!sameOrigin && !externalAllowed) return;

  event.respondWith((async () => {
    const cache = await caches.open(CACHE);
    const cached = await cache.match(req, { ignoreSearch: true });
    const fetchPromise = fetch(req).then((res) => {
      if (res && res.ok && (res.type === 'basic' || res.type === 'cors' || res.type === 'opaque')) {
        cache.put(req, res.clone()).catch(() => {});
      }
      return res;
    }).catch(() => cached);
    return cached || fetchPromise;
  })());
});
