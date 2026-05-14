# Leaflet cluster map of talk locations
#
# Run from the repo root:
#   venv\Scripts\python.exe talkmap.py
#
# Scrapes the location YAML field from each _talks/*.md file, geolocates it
# with geopy/Nominatim (caching results to talkmap/geocode_cache.json so
# already-processed locations are never re-fetched), and builds a Folium
# cluster map saved to talkmap/map.html.

import json
import os
import frontmatter
import glob
from geopy import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderRateLimited
from geopy.extra.rate_limiter import RateLimiter
import folium
from folium.plugins import MarkerCluster

TIMEOUT = 5
CACHE_FILE = "talkmap/geocode_cache.json"

# Load geocode cache: location string -> {"latitude": ..., "longitude": ...}
if os.path.exists(CACHE_FILE):
    with open(CACHE_FILE) as f:
        geo_cache = json.load(f)
else:
    geo_cache = {}

geocoder = Nominatim(user_agent="jimegon-talkmap")
geocode = RateLimiter(geocoder.geocode, min_delay_seconds=1, error_wait_seconds=5)

location_dict = {}  # description -> {"latitude": ..., "longitude": ...}

for file in glob.glob("_talks/*.md"):
    data = frontmatter.load(file).to_dict()

    location = (data.get('location') or '').strip()
    if not location:
        print(f"Skipped (no location): {file}")
        continue

    title = (data.get('title') or '').strip()
    venue = (data.get('venue') or '').strip()
    description = f"{title}<br />{venue}; {location}"

    if location in geo_cache:
        print(f"Cached:   {location}")
        location_dict[description] = geo_cache[location]
        continue

    try:
        geo = geocode(location, timeout=TIMEOUT)
        if geo:
            coords = {"latitude": geo.latitude, "longitude": geo.longitude}
            geo_cache[location] = coords
            location_dict[description] = coords
            print(f"Geocoded: {location} -> {geo.latitude:.4f}, {geo.longitude:.4f}")
        else:
            print(f"No result: {location}")
    except GeocoderTimedOut as ex:
        print(f"Timed out: {location} — {ex}")
    except GeocoderRateLimited as ex:
        print(f"Rate limited: {location} — {ex}")
    except Exception as ex:
        print(f"Error: {location} — {ex}")

# Persist updated cache
os.makedirs("talkmap", exist_ok=True)
with open(CACHE_FILE, 'w') as f:
    json.dump(geo_cache, f, indent=2)

# Build map
m = folium.Map(location=[39.5, -60], zoom_start=2)
marker_cluster = MarkerCluster().add_to(m)

for description, coords in location_dict.items():
    folium.Marker(
        location=[coords["latitude"], coords["longitude"]],
        popup=description,
    ).add_to(m)

m.save("talkmap/map.html")
print(f"\nMap saved to talkmap/map.html ({len(location_dict)} markers)")
