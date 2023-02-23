import psycopg2
import PK
import folium
import dbAccessor
import utility 
import webbrowser

def ajoutFiltrableInMap(map, filtrable, couleur):
    latLong = [filtrable.latitude, filtrable.longitude]
    position = folium.Marker(
        latLong, 
        popup="latitude {0} --- longitude {1}".format(filtrable.latitude, filtrable.longitude),
        tooltip="{0} --- {1}".format(filtrable.description, filtrable.identifiant),
        icon=folium.Icon(color=couleur)
    )
    
    position.add_to(map)

def showMap(map, mapPath):
    map.save(mapPath)
    webbrowser.open(mapPath)

def getMap(connect,idRoute,table_name,colPkd_name,colPkf_name,SRID,zoom):

    if(zoom == None):
        zoom = 15

    route = dbAccessor.selectRoute(connect, idRoute)

    budget = utility.calculBudgetRoute(route)

    LatlongDebut = utility.geomToLatLong(connect, idRoute, table_name, colPkd_name, SRID)
    LatlongFin = utility.geomToLatLong(connect, idRoute, table_name, colPkf_name, SRID)

    pkd = [LatlongDebut[0], LatlongDebut[1]]
    pkf = [LatlongFin[0], LatlongFin[1]]
    
    m=folium.Map(location=pkd, zoom_start=zoom)

    position1 = folium.Marker(
        pkd, 
        popup="latitude {0} --- longitude {1}--- longeur {2}--- largeur {3}--- degat {4}---cout(Ar) {5}--- duree(Jours) {6}".format(LatlongDebut[0],LatlongDebut[1],route.getLongueur(),route.largeur,route.etat,budget.cout, budget.duree),
        tooltip="PkD {0}".format(route.description),
        icon=folium.Icon(color='green')
    )
    
    position1.add_to(m)

    
    position2 = folium.Marker(
        pkf,
        popup="latitude {0} --- longitude {1}--- longeur {2}--- largeur {3}--- degat {4}---cout(Ar) {5}--- duree(Jours) {6}".format(LatlongFin[0],LatlongFin[1],route.getLongueur(),route.largeur,route.etat,budget.cout, budget.duree),
        tooltip="PkF {0}".format(route.description),
        icon=folium.Icon(color='blue')
    )
    
    position2.add_to(m)

    #layer -- couche
    ###################################################################################
    tile_layer = folium.TileLayer(
        tiles="https://{s}.basemaps.cartocdn.com/rastertiles/dark_all/{z}/{x}/{y}.png",
        attr='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
        max_zoom=19,
        name='hopital',
        control=True,
        opacity=1
    )
    tile_layer.add_to(m)
    ##################################################################################

    m.add_child(folium.LayerControl())
    folium.LatLngPopup().add_to(m)

    return m

