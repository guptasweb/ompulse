// 🧘 OmPulse Service Worker - Spiritual Offline Experience
// Ensuring your conscious investing journey continues even without connection

const CACHE_NAME = 'ompulse-v1.0.0';
const OFFLINE_URL = '/offline.html';

// Resources to cache for offline spiritual guidance
const CACHE_URLS = [
  '/',
  '/static/manifest.json',
  '/offline.html',
  // Add critical CSS and JS files here when they exist
];

// Spiritual messages for different states
const ZEN_MESSAGES = {
  installing: '🌱 Installing OmPulse consciousness...',
  activated: '✨ OmPulse spirit awakened and ready',
  offline: '🧘 Connection lost, but inner wisdom remains strong',
  online: '🌊 Sacred connection restored to market stream'
};

// Install event - Cache essential resources
self.addEventListener('install', event => {
  console.log(ZEN_MESSAGES.installing);
  
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => {
        console.log('🌸 Caching essential spiritual resources');
        return cache.addAll(CACHE_URLS);
      })
      .then(() => {
        console.log('💫 Essential wisdom cached for offline access');
        return self.skipWaiting();
      })
      .catch(error => {
        console.error('🌫️ Error caching resources:', error);
      })
  );
});

// Activate event - Clean up old caches
self.addEventListener('activate', event => {
  console.log(ZEN_MESSAGES.activated);
  
  event.waitUntil(
    caches.keys()
      .then(cacheNames => {
        return Promise.all(
          cacheNames.map(cacheName => {
            if (cacheName !== CACHE_NAME) {
              console.log('🍃 Releasing old cache:', cacheName);
              return caches.delete(cacheName);
            }
          })
        );
      })
      .then(() => {
        console.log('🌟 OmPulse consciousness fully activated');
        return self.clients.claim();
      })
  );
});

// Fetch event - Serve cached content when offline
self.addEventListener('fetch', event => {
  // Only handle GET requests
  if (event.request.method !== 'GET') return;
  
  // Handle API requests differently
  if (event.request.url.includes('/api/')) {
    event.respondWith(handleApiRequest(event.request));
    return;
  }
  
  // Handle navigation requests
  if (event.request.mode === 'navigate') {
    event.respondWith(handleNavigationRequest(event.request));
    return;
  }
  
  // Handle other requests with cache-first strategy
  event.respondWith(
    caches.match(event.request)
      .then(response => {
        if (response) {
          return response;
        }
        return fetch(event.request);
      })
      .catch(() => {
        // Return offline page for navigation requests
        if (event.request.mode === 'navigate') {
          return caches.match(OFFLINE_URL);
        }
      })
  );
});

// Handle API requests with network-first, then offline wisdom
async function handleApiRequest(request) {
  try {
    const response = await fetch(request);
    return response;
  } catch (error) {
    console.log('🌫️ API connection clouded, serving offline wisdom');
    
    // Return spiritual offline responses for different endpoints
    if (request.url.includes('/meditation/daily')) {
      return new Response(JSON.stringify({
        success: true,
        meditation: {
          date: new Date().toISOString().split('T')[0],
          market_affirmation: "🧘 Even without connection, I trust my inner wisdom to guide my financial decisions",
          breathing_exercise: "🌬️ Breathe in peace and abundance, breathe out fear and doubt",
          financial_wisdom: "💫 True wealth comes from within and flows naturally when we are aligned",
          chakra_focus: "💚 Heart Chakra - Making money decisions from love, not fear",
          mantra: "I am connected to infinite abundance 🌟"
        },
        zen_moment: "🌸 In silence, the deepest truths are heard",
        offline_note: "🌫️ Channeling offline spiritual guidance"
      }), {
        headers: { 'Content-Type': 'application/json' }
      });
    }
    
    if (request.url.includes('/astro/daily-forecast')) {
      return new Response(JSON.stringify({
        success: true,
        forecast: {
          overall_energy: "serene offline consciousness 🧘",
          market_prediction: "🌌 The stars remind us that all cycles are temporary, including disconnection",
          cosmic_advice: "💫 Use this quiet moment to reflect on your investment intentions",
          lunar_phase: "🌙 In all phases, the moon teaches patience"
        },
        offline_wisdom: "🔮 The universe speaks loudest in the silence"
      }), {
        headers: { 'Content-Type': 'application/json' }
      });
    }
    
    // Generic offline response
    return new Response(JSON.stringify({
      success: false,
      error: "🌫️ Connection to market stream temporarily clouded",
      offline_wisdom: "🧘 In disconnection, we find deeper connection to our inner guidance",
      suggestion: "💫 Use this time for reflection and intention setting"
    }), {
      status: 503,
      headers: { 'Content-Type': 'application/json' }
    });
  }
}

// Handle navigation requests
async function handleNavigationRequest(request) {
  try {
    const response = await fetch(request);
    return response;
  } catch (error) {
    console.log(ZEN_MESSAGES.offline);
    const cache = await caches.open(CACHE_NAME);
    return await cache.match(OFFLINE_URL) || await cache.match('/');
  }
}

// Listen for messages from the app
self.addEventListener('message', event => {
  if (event.data && event.data.type === 'SKIP_WAITING') {
    console.log('🌟 Immediately activating new OmPulse consciousness');
    self.skipWaiting();
  }
});

// Background sync for when connection is restored
self.addEventListener('sync', event => {
  if (event.tag === 'market-data-sync') {
    console.log('🌊 Sacred connection restored - syncing market consciousness');
    event.waitUntil(syncMarketData());
  }
});

async function syncMarketData() {
  try {
    // Notify all clients that connection is restored
    const clients = await self.clients.matchAll();
    clients.forEach(client => {
      client.postMessage({
        type: 'CONNECTION_RESTORED',
        message: ZEN_MESSAGES.online
      });
    });
  } catch (error) {
    console.error('🌫️ Error syncing market data:', error);
  }
}

console.log('🧘 OmPulse Service Worker loaded - Ready to serve conscious investing wisdom'); 