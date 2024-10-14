import folium
import pandas 

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color(height):
    if height <= 1000:
        return 'green'
    elif height <= 2000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[39.763078,-104.952148], zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name = "My Map")

for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.CircleMarker(location = [lt, ln], popup=str(el)+ " m",radius=6, fill_color = color(el),color='blue', fill_opacity=0.8))

fg.add_child(folium.GeoJson(data=(open('world.json', 'r', encoding='UTF-8-sig').read())))

map.add_child(fg)
map.save("1st map.html")
