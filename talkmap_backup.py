

# # Leaflet cluster map of talk locations
#
# (c) 2016-2017 R. Stuart Geiger, released under the MIT license
#
# Run this from the _talks/ directory (go to terminal and cd _talks . 
# At the end, within the terminal, write cd ..), which contains .md files of all your talks. 
# This scrapes the location YAML field from each .md file, geolocates it with
# geopy/Nominatim, and uses the getorg library to output data, HTML,
# and Javascript for a standalone cluster map.
#
# Requires: glob, getorg, geopy

import glob
import getorg
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
from time import sleep
from collections import defaultdict

# Load markdown files
g = glob.glob("*.md")

# Setup geocoder with a user agent
geocoder = Nominatim(user_agent="my-app")
location_dict = defaultdict(lambda: None)  # Store geocoded results

# Function to handle geocoding with retries
def geocode_location(location):
    try:
        return geocoder.geocode(location, timeout=10)  # Increase timeout to 10 sec
    except GeocoderTimedOut:
        print(f"Timeout error for location: {location}. Retrying...")
        sleep(2)  # Wait 2 seconds before retrying
        return geocode_location(location)  # Recursive retry

# Extract locations from markdown files
for file in g:
    with open(file, 'r', encoding="utf-8") as f:
        lines = f.read()
        if 'location: "' in lines:
            loc_start = lines.find('location: "') + 11
            loc_end = lines.find('"', loc_start)
            location = lines[loc_start:loc_end]
            
            if location and location not in location_dict:  # Avoid duplicate requests
                print(f"Geocoding: {location}")
                location_dict[location] = geocode_location(location)
                sleep(1.5)  # Respect Nominatim rate limits

# Create map using getorg
m = getorg.orgmap.create_map_obj()
getorg.orgmap.output_html_cluster_map(location_dict, folder_name="../talkmap", hashed_usernames=False)




