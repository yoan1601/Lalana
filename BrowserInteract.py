import folium
import webbrowser

# Fonction pour afficher les coordonnées d'un point au survol du curseur
def afficher_coordonnees(lat, lon):
    popup_text = "Latitude={}, Longitude={}".format(lat, lon)
    return folium.Popup(popup_text, max_width=300)

# Création de la carte centrée sur les coordonnées données
carte = folium.Map(location=[48.8534, 2.3488], zoom_start=13)

# Ajout de marqueurs pour des emplacements donnés
emplacement1 = folium.Marker(location=[48.8534, 2.3488], tooltip='Paris (48.8534, 2.3488)', popup="Paris",icon=folium.Icon(color='green'))
emplacement2 = folium.Marker(location=[48.8434, 2.3388], tooltip='Paris2 (48.8000, 2.3476)', popup="Londres",color="blue")
emplacement3 = folium.Marker(location=[48.8634, 2.3588], tooltip='Londres (48.8100, 2.3490)', popup="PK9")
emplacement1.add_to(carte)
emplacement2.add_to(carte)
emplacement3.add_to(carte)

# Configuration de l'affichage des coordonnées au survol du curseur
folium.LatLngPopup().add_to(carte)

# Affichage de la carte
carte.save('map/Carte2.html')
webbrowser.open('map/Carte2.html')