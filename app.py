
from flask import Flask, send_file, request, redirect, url_for, render_template
import dbAccessor
import map
from Route import Route
from Filtre import Filtrable

app = Flask(__name__)

@app.route('/')
def index():
    routes = dbAccessor.selectRoute(None, None)
    return render_template('menu.html', routes = routes)

@app.route('/menu')
def menu():
    return index()

@app.route('/insertFiltrable', methods=['POST'])
def insertFiltrable():
    identifiants = ['B', 'O']
    
    idcategorie = int(request.form['idcategorie'])
    ident = identifiants[idcategorie]
    description = request.form['description']
    lat = request.form['lat']
    long = request.form['long']

    filtre = Filtrable(None, ident, description, lat, long)
    filtre.insert(None)

    return goToInsertFiltrable()

@app.route('/goToInsertFiltrable', methods=['GET'])
def goToInsertFiltrable():
    categories = ['batiment', 'humain']
    return render_template('nouveauFiltrable.html', categories = categories, lenCat = len(categories))

@app.route('/insertRoute', methods=['POST'])
def insertRoute():
    description = request.form['description']
    largeur = request.form['largeur']
    pkd = request.form['pkd']
    pkf = request.form['pkf']
    etat = request.form['etat']
    latD = request.form['latD']
    longD = request.form['longD']
    latF = request.form['latF']
    longF = request.form['longF']

    route = Route(None, description, largeur, pkd, pkf, etat, None)
    route.insertWithGeoPos(None, latD, longD, latF, longF)

    return index()

@app.route('/goToInsertRoute', methods=['GET'])
def goToInsertRoute():
    return render_template('nouvelleRoute.html')

@app.route('/buildMap', methods=['POST'])
def buildMap():
    idroute = request.form['idroute']
    m = map.getMap(None, idroute, 'route', 'geo_pkd', 'geo_pkf', 32645, 15)
    m.save("templates/map/carte.html")
    map.showMap(m, "templates/map/carte.html")
    routes = dbAccessor.selectRoute(None, None)
    return render_template('menu.html', routes = routes)


if __name__ == '__main__':
    app.run()