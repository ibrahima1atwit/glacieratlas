import folium
folium.Map(location = [71.706936, -42.604303], zoom_start = 2.5)

m = folium.Map(location=[65.0731, -40.1955], zoom_start=3.5)

tooltip = "Click Here For More Info"

marker = folium.Marker(
    location=[65.0731, -40.1955],
    popup="<stong>Apuseeq</stong>",
    tooltip=tooltip)
marker.add_to(m)

m