import geocoder
import folium
class gps:
    g = geocoder.ip("me")
    myAddress = g.latlng
    my_map1 = folium.Map(location=myAddress,
    zoom_start=8,
    zoom_control=False,
    scrollWheelZoom=False)
    folium.CircleMarker(location=myAddress,radius=100,popup="Yorkshire").add_to(my_map1)
    my_map1.save("map.html  ")