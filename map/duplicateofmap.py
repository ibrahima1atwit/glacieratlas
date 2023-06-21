import geopy
import pandas as pd
import folium
import matplotlib.pyplot as plt
from geopy.geocoders import Nominatim
from folium.vector_layers import Rectangle
from folium.plugins import MarkerCluster


# Read excel file with just coordinates
df1 = pd.read_csv('Map_python.csv')

# Read csv file with names
df2 = pd.read_csv('Map_names.csv')

subset_size = 100 
subset1 = df1.head(subset_size)
subset2 = df2.head(subset_size)

# Creates a map centered on the first location
center_lat = subset1['LAT'].iloc[0]
center_long = subset1['LONG'].iloc[0]
my_map = folium.Map(location=[center_lat, center_long], zoom_start = 10)

geolocator = Nominatim(user_agent="email@email.com", timeout=20)
locations = []

marker_cluster = MarkerCluster().add_to(my_map)

for index, row in subset2.iterrows():
    latitude = row['LAT']
    longitude = row['LONG']
    name = row['NAMES']
   
    folium.Marker([latitude, longitude], popup = name, icon=folium.Icon(color='red')).add_to(marker_cluster)

    # Add markers for points in csv file with just coordinates
for index, row in subset1.iterrows():
    # Get the longitude and latitude values
    twila_latitude = row['LAT']
    twila_longitude = row['LONG']
    popup_text = f"LAT: {twila_latitude}<br>LONG: {twila_longitude}"
    folium.Marker([twila_latitude, twila_longitude], popup = popup_text, icon=folium.Icon(color='blue')).add_to(marker_cluster)
    box_size = 0.1
    box = bounds = [(twila_latitude - box_size/2, twila_longitude - box_size/2), (twila_latitude + box_size/2, twila_longitude + box_size/2), (twila_latitude - box_size/2, twila_longitude + box_size), (twila_latitude + box_size/2, twila_longitude - box_size/2)]
    for index1, row1 in subset2.iterrows():
          # Create a loop that checks the points in the bounds of the named glacier points
          # If the twila point is within a bound of a named point then that twila point is a part of that specific glacier
          



    
try:
        location = geolocator.reverse((latitude, longitude))    
    except geopy.exc.GeocoderTimedOut:
    # Handle timeout error
        print("Geocoding service timed out. Try again later.")
    except geopy.exc.GeocoderUnavailable:
    # Handle unavailable service
        print("Geocoding service is currently unavailable. Try again later.")
    except Exception as e:
    # Handle other exceptions
        print("An error occurred during geocoding:", str(e))
    locations.append(location)

# Place a box around each individual named coordinate
for index, row in subset2.iterrows():
    twila_latitude = row['LAT']
    long = row['LONG']
    box_size = 0.1
    box = Rectangle(bounds=[(twila_latitude - box_size/2, long - box_size/2),
                            (twila_latitude + box_size/2, long + box_size/2)],
                    color='lightgray', fill=True, fill_opacity=0.3)
    my_map.add_child(box)

# for loop to find points within area
# 


# for index, row in subset1.iterrows():
#     lat = row['LAT']
#     long = row['LONG']
#     location_name = locations[index]
#     popup_text = f"LAT: {lat}<br>LONG: {long}"
#     folium.Marker([lat,long], popup = popup_text).add_to(my_map) 

# satellite_layer = folium.TileLayer('Google Satellite').add_to(my_map)
# satellite_layer.layer_name = 'Satellite'


# Add a satellite tile layer with attribution
satellite_layer = folium.TileLayer(
    tiles='https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}',
    attr='Google Satellite',
    name='Satellite'
).add_to(my_map)

# Add layer control to toggle between map and satellite layers
folium.LayerControl().add_to(my_map)

my_map  
