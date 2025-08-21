# Leaflet cluster map of talk locations
#
# Run this from the _talks/ directory (go to terminal and cd _talks . 
# At the end, within the terminal, write cd ..), which contains .md files of all your
# talks. This scrapes the location YAML field from each .md file, geolocates it
# with geopy/Nominatim, and uses the getorg library to output data, HTML, and
# Javascript for a standalone cluster map. This is functionally the same as the
# #talkmap Jupyter notebook.

# Alternatively: run venv\Scripts\python.exe talkmap.py 
# in cd C:\Users\jimeg\source\repos\jimegon.github.io
import frontmatter
import glob
import getorg
from geopy import Nominatim
from geopy.exc import GeocoderTimedOut

# Set the default timeout, in seconds
TIMEOUT = 5

# Collect the Markdown files
g = glob.glob("_talks/*.md")

# Prepare to geolocate
geocoder = Nominatim(user_agent="academicpages.github.io")
location_dict = {}
location = ""
permalink = ""
title = ""



# Perform geolocation
for file in g:
    # Read the file
    data = frontmatter.load(file)
    data = data.to_dict()

    # Press on if the location is not present
    if 'location' not in data:
        continue

    # Prepare the description
    #title = data['title'].strip()
    #venue = data['venue'].strip()
    #location = data['location'].strip()
    #description = f"{title}<br />{venue}; {location}"

    # Prepare the description (from ChatGPT to avoid errors with unknonw to replace above code
    title = (data.get('title') or "").strip()
    venue = (data.get('venue') or "").strip()
    location = (data.get('location') or "").strip()

    # Only include location if it exists
    if location:
        description = f"{title}<br />{venue}; {location}"
    else:
        description = f"{title}<br />{venue}"


    # Geocode the location and report the status
    try:
        location_dict[description] = geocoder.geocode(location, timeout=TIMEOUT)
        print(description, location_dict[description])
    except ValueError as ex:
        print(f"Error: geocode failed on input {location} with message {ex}")
    except GeocoderTimedOut as ex:
        print(f"Error: geocode timed out on input {location} with message {ex}")
    except Exception as ex:
        print(f"An unhandled exception occurred while processing input {location} with message {ex}")

# From ChatGPT: Instead of storing just the geocoded location object, 
# store both the description and coordinates.
geo = geocoder.geocode(location, timeout=TIMEOUT)
if geo:
    location_dict[description] = (geo.latitude, geo.longitude)
    print(description, geo.latitude, geo.longitude)

# Save the map
#m = getorg.orgmap.create_map_obj()
#getorg.orgmap.output_html_cluster_map(location_dict, folder_name="talkmap", hashed_usernames=False)

# From ChatGPT to manually build the map so that the popup text is your description 
# and replace 2 lines above
import folium
from folium.plugins import MarkerCluster

# Create a map centered roughly at the US
# Zoom determines the default zoom level of the map (=4 only shows the US)
#m = folium.Map(location=[39.5, -98.35], zoom_start=2.5) 
m = folium.Map(location=[39.5, -60], zoom_start=2) 

# Create a marker cluster
marker_cluster = MarkerCluster().add_to(m)

for description, geo in location_dict.items():
    if geo:  # Only add if geocoding worked
        folium.Marker(
            location=[geo.latitude, geo.longitude],
            popup=description,
        ).add_to(m)

# Save map
m.save("talkmap/map.html")