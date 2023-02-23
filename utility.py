import Connection
import dbAccessor
from Route import Route 
from Budget import Budget
from Filtre import Filtrable

def getRoutePrioritaire(connect, indentifiantFiltrable, diametre):
    try:
        connectionOpened = False

        if(connect == None):
            connect = Connection.getPgsqlConnection()
            connectionOpened = True
        
        routes = dbAccessor.selectRoute(connect, None)
        routesOrdrePrio = orderRouteByCoeffPrio(routes, indentifiantFiltrable, diametre)

        return routesOrdrePrio[0]

    except (Exception) as error:
        print("getRoutePrioritaire : ",error)

    finally:
        # closing database connection.
        if connect:
            if(connectionOpened == True):
                connect.close()
                print("PostgreSQL connection is closed")

def getAllFiltrables(connect, route,indentifiantFiltrable, diametre):
    latlongD = geomToLatLong(connect, route.id, None, 'geo_pkd', None)
    filtrables1 = dbAccessor.getAllFiltrableAuxEnviron(connect, indentifiantFiltrable, diametre, latlongD[0], latlongD[1])
    #nbFiltrable1 = len(filtrables1)

    latlongF = geomToLatLong(connect, route.id, None, 'geo_pkf', None)
    filtrables2 = dbAccessor.getAllFiltrableAuxEnviron(connect, indentifiantFiltrable, diametre, latlongF[0], latlongF[1])
    #nbFiltrable2 = len(filtrables2)

    arrayFusionFiltrable = filtrables1 + filtrables2

    #elimine les doublons en cas de doublon 
    ################################################################################
    idFiltreSansDoublon = list(set((filtre.id) for filtre in arrayFusionFiltrable))
    
    arrayFusionFiltrableSansDoublon = []

    for idFiltre in idFiltreSansDoublon:
        filtre = dbAccessor.selectFiltrableById(connect, idFiltre)
        arrayFusionFiltrableSansDoublon.append(filtre)
    ################################################################################

    return arrayFusionFiltrableSansDoublon

def orderRouteByCoeffPrio(routes, indentifiantFiltrable, diametre):
    idPrio = 0
    result = []
    for i in range(len(routes)):
        idPrio = getIdPrio(routes, i, indentifiantFiltrable, diametre)
        result.append(routes[idPrio])
    return result

def getIdPrio(routes, idInit, indentifiantFiltrable, diametre):
    idPrio = idInit
    coeffPrio = getCoeffPriorite(routes[idPrio], indentifiantFiltrable, diametre)
    for i in range(len(routes)):
        coeff = getCoeffPriorite(routes[i], indentifiantFiltrable, diametre)
        if(coeff > coeffPrio):
            idPrio = i
    return idPrio

def getCoeffPriorite(route, indentifiantFiltrable, diametre):

    try:
        connect = Connection.getPgsqlConnection()

        budget = calculBudgetRoute(route)

        sommeFiltrables = len(getAllFiltrables(connect, route, indentifiantFiltrable, diametre))

        coeff = sommeFiltrables/(budget.cout * budget.duree)

        return coeff
    
    except (Exception) as error:
        print("getCoeffPriorite : ",error)

    finally:
        # closing database connection.
        if connect:
            connect.close()
            print("PostgreSQL connection is closed")


def geomToLatLong(connect , idroute, table_name, colonne, SRID):
    try:
        connectionOpened = False

        if(connect == None):
            connect = Connection.getPgsqlConnection()
            connectionOpened = True
        
        curseur = connect.cursor()

        if(SRID == None):
            SRID = 32645
        
        if(table_name == None):
            table_name = 'route'

        #sql = """  SELECT UpdateGeometrySRID('{0}', '{1}' ,{2})  """.format(table_name, colonne, SRID)            

        #print(sql)

        #curseur.execute(sql)

        #connect.commit()

        #print("update SRID succes")

        sql = """   SELECT ST_X (ST_Transform ({0}, 32645)) AS lat,
                    ST_Y (ST_Transform ({1}, 32645)) AS long
                    FROM route WHERE id = {2}  """.format(colonne, colonne, idroute)            

        print(sql)

        curseur.execute(sql)

        result = curseur.fetchone()

        return result

    except (Exception) as error:
        print("update SRID echouee ou select echoue ", error)

    finally:
        # closing database connection.
        if connect:
            curseur.close()
            if(connectionOpened == True):
                connect.close()
                print("PostgreSQL connection is closed")

def calculVolumeGoudron(route):

    longueur = (route.pkf - route.pkd) * 1000 #conversion km * 1000 -> m
    profondeur = (route.etat/10) / 100 #conversion (etat/10) -> cm/100 -> m

    return longueur * route.largeur * profondeur #largeur par defaut en m


def calculBudgetRoute(route):

    connect = Connection.getPgsqlConnection()
    
    constr_cout = dbAccessor.getConstruction(connect, 'cout', None)
    constr_duree = dbAccessor.getConstruction(connect, 'duree', None)

    volumeGoudron = calculVolumeGoudron(route)

    budget_cout = constr_cout.valeur * volumeGoudron
    budget_duree = constr_duree.valeur * volumeGoudron

    budget = Budget(budget_cout, budget_duree, volumeGoudron)

    route.setBudget(budget)
    
    connect.close()

    return budget
