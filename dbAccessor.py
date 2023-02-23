import Connection
from Construction import Construction
from Filtre import Filtrable
from Route import Route

def selectFiltrableById(connect, id):
    try:
        connectionOpened = False

        if(connect == None):
            connect = Connection.getPgsqlConnection()
            connectionOpened = True
        
        curseur = connect.cursor()

        if(id == None):
            sql = """ SELECT * FROM filtrable """

            print(sql)

            curseur.execute(sql)

            results = curseur.fetchall()

            print("Select all filtrables succes")

            filtrables = []

            for result in results:
                filtre = Filtrable(result[0], result[1], result[2], result[3], result[4])
                filtrables.append(filtre)

            return filtrables
        
        else:
            sql = """ SELECT * FROM filtrable WHERE id = {0} """.format(id)

            print(sql)

            curseur.execute(sql)

            result = curseur.fetchone()

            print("Select filtrable succes avec id {0}".format(id))

            filtre = Filtrable(result[0], result[1], result[2], result[3], result[4])

            return filtre

    except (Exception) as error:
        print("Select route echouee", error)

    finally:
        # closing database connection.
        if connect:
            curseur.close()
            if(connectionOpened == True):
                connect.close()
                print("PostgreSQL connection is closed")


def selectFiltrable(connect, identifiant):
    try:
        connectionOpened = False

        if(connect == None):
            connect = Connection.getPgsqlConnection()
            connectionOpened = True
        
        curseur = connect.cursor()

        if(identifiant == None):
            sql = """ SELECT * FROM filtrable """

            print(sql)

            curseur.execute(sql)

            results = curseur.fetchall()

            print("Select all filtrables succes")

            filtrables = []

            for result in results:
                filtre = Filtrable(result[0], result[1], result[2], result[3], result[4])
                filtrables.append(filtre)

            return filtrables
        
        else:
            sql = """ SELECT * FROM filtrable WHERE identifiant like '%{0}%' """.format(identifiant)

            print(sql)

            curseur.execute(sql)

            results = curseur.fetchall()

            print("Select all filtrables succes avec identifiant {0}".format(identifiant))

            filtrables = []

            for result in results:
                filtre = Filtrable(result[0], result[1], result[2], result[3], result[4])
                filtrables.append(filtre)

            return filtrables

    except (Exception) as error:
        print("Select route echouee", error)

    finally:
        # closing database connection.
        if connect:
            curseur.close()
            if(connectionOpened == True):
                connect.close()
                print("PostgreSQL connection is closed")

def getAllFiltrableAuxEnviron(connect, identifiant, diametre, latitude, longitude):

    #diametre en metre

    connectionOpened = False
    
    if(connect == None):
        connect = Connection.getPgsqlConnection()
        connectionOpened = True
    
    curseur = connect.cursor()

    if(identifiant != None):
        sql = """ 
                SELECT * 
                FROM filtrable
                WHERE ST_DISTANCE(ST_GeographyFromText('point('||latitude||' '||longitude||')'), ST_GeographyFromText('point({0} {1})')) < {2} AND identifiant like '%{3}%'
            """ .format(latitude, longitude, diametre, identifiant)
    
    else:
        sql = """ 
                SELECT * 
                FROM filtrable
                WHERE ST_DISTANCE(ST_GeographyFromText('point('||latitude||' '||longitude||')'), ST_GeographyFromText('point({0} {1})')) < {2}
            """ .format(latitude, longitude, diametre)

    print(sql)

    curseur.execute(sql)

    results = curseur.fetchall()

    curseur.close()
    if(connectionOpened == True):
       connect.close() 

    #print("id  >>> {0}".format(result[0]))

    filtres = []

    for result in results:
        filtre = Filtrable(result[0], result[1], result[2], result[3], result[4])
        filtres.append(filtre)
    
    return filtres    

def selectRoute(connect, id):
    try:
        connectionOpened = False

        if(connect == None):
            connect = Connection.getPgsqlConnection()
            connectionOpened = True
        
        curseur = connect.cursor()

        if(id == None):
            sql = """ SELECT * FROM route """

            print(sql)

            curseur.execute(sql)

            results = curseur.fetchall()

            print("Select all routes succes")

            routes = []

            for result in results:
                route = Route(result[0], result[1], result[2], result[3], result[4], result[5], None)
                routes.append(route)

            return routes
        
        else:
            sql = """ SELECT * FROM route WHERE id = {0} """.format(id)

            print(sql)

            curseur.execute(sql)

            result = curseur.fetchone()

            route = Route(result[0], result[1], result[2], result[3], result[4], result[5], None)

            print("Select route succes")

            return route

    except (Exception) as error:
        print("Select route echouee", error)

    finally:
        # closing database connection.
        if connect:
            curseur.close()
            if(connectionOpened == True):
                connect.close()
                print("PostgreSQL connection is closed")

def getConstruction(connect ,descri, date):
    
    connectionOpened = False
    
    if(connect == None):
        connect = Connection.getPgsqlConnection()
        connectionOpened = True
    
    curseur = connect.cursor()

    if(date == None):
        date = "(SELECT max(date) FROM construction WHERE description = '"+descri+"')"
    else:
        date = "'"+date+"'"

    sql = "SELECT * FROM construction WHERE description = '{0}' AND date = {1}".format(descri, date)

    curseur.execute(sql)

    result = curseur.fetchone()

    curseur.close()
    if(connectionOpened == True):
       connect.close() 

    #print("id  >>> {0}".format(result[0]))

    constr = Construction(result[0], result[1], result[2], result[3], result[4])
    
    return constr
