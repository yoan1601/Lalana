from Budget import Budget
import dbAccessor
from Route import Route
import utility
import map
from Filtre import Filtrable

routePrio = utility.getRoutePrioritaire(None, 'B', 2000)
routePrio.detail()
allFiltre = utility.getAllFiltrables(None, routePrio, 'B', 2000)
for f in allFiltre:
    print(f.description)
print('nombre de batiment aux alentours : {0}'.format(len(allFiltre)))

#filtres = dbAccessor.selectFiltrable(None, 'B')
#for f in filtres:
#    f.detail()

#filtre = Filtrable(None, 'B', 'Hopital 1', -18.97945, 47.53259)
#filtre.insert(None)

# identifiant : O -> olona
# identifiant : B -> batiment
# identifiant : None -> ALL
#rn7 = dbAccessor.selectRoute(None, 1)
#latLong7 = utility.geomToLatLong(None, rn7.id, None, 'geo_pkd', None)
#filtres = dbAccessor.getAllFiltrableAuxEnviron(None, 'B', 2000, latLong7[0], latLong7[1])
#for f in filtres:
#    f.detail()

#map.tuto()
#m = map.getMap(None, 4, 'route', 'geo_pkd', 'geo_pkf', 32645, 15)
#map.showMap(m, "templates/map/carte.html")

#b1 = Budget(4000, 3)
#b1.detail()

#constr = dbAccessor.getConstruction(None, 'cout', None)
#constr.detail()

#route = Route(None, 'RN2', 5, 1004, 1042, 40, None)
#route = Route(None, 'RN7', 5, 980, 1000, 69, None)

#route.insertWithGeoPos(None, -18.984463421810585, 47.53333843669796, -18.99308231550269, 47.5337518563659)
#route.insert(None)

#budget = utility.calculBudgetRoute(route) 

#budget = route.budget

#print("cout de construction {0} Ar ; duree de construction {1} jours".format(round(budget.cout), round(budget.duree)))
#budget.detail()

#routes = dbAccessor.selectRoute(None, 4)
#print(routes)
