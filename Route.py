import Connection

class Route:
    def __init__(self, id, description, largeur ,pkd, pkf, etat, budget):
        self.id = id
        self.description = description
        self.largeur = largeur
        self.pkd = pkd
        self.pkf = pkf
        self.etat = etat
        self.budget = budget

    def detail(self):
        print('id ', self.id)
        print('description ', self.description)
        print('largeur ', self.largeur)
        print('pkd ', self.pkd)
        print('pkf ', self.pkf)
        print('etat ', self.etat)
        print('budget volume goudron', self.budget.volume)
        print('budget cout', self.budget.cout)
        print('budget duree', self.budget.duree)
    
    def getLongueur(self):
        return self.pkf - self.pkd
    
    def insertWithGeoPos(self, connect,latPkd, longPkd,latPkf,longPkf):
        try:
            connectionOpened = False
    
            if(connect == None):
                connect = Connection.getPgsqlConnection()
                connectionOpened = True
            
            curseur = connect.cursor()

            geoDebut = "ST_GeomFromText('point({0} {1})', 32645)".format(latPkd,longPkd )
            geoFin = "ST_GeomFromText('point({0} {1})', 32645)".format(latPkf, longPkf)

            sql = """ INSERT INTO route (description, largeur, pkd, pkf, etat, geo_pkd, geo_pkf) VALUES ('{0}',{1},{2},{3},{4},{5},{6}) """.format(self.description, self.largeur, self.pkd, self.pkf, self.etat, geoDebut, geoFin)

            print("sql "+ sql)

            curseur.execute(sql)

            connect.commit()
            count = curseur.rowcount
            print(count, "insertion route succes")

        except (Exception) as error:
            print("Insertion route echouee ", error)

        finally:
            # closing database connection.
            if connect:
                curseur.close()
                if(connectionOpened == True):
                    connect.close()
                    print("PostgreSQL connection is closed")
    
    def insert(self, connect):
        try:
            connectionOpened = False
    
            if(connect == None):
                connect = Connection.getPgsqlConnection()
                connectionOpened = True
            
            curseur = connect.cursor()


            sql = """ INSERT INTO route (description, largeur, pkd, pkf, etat) VALUES (%s,%s,%s,%s,%s)"""            
            param = (self.description, self.largeur, self.pkd, self.pkf, self.etat)

            print(sql)

            curseur.execute(sql, param)

            connect.commit()
            count = curseur.rowcount
            print(count, "insertion route succes")

        except (Exception) as error:
            print("Insertion route echouee", error)

        finally:
            # closing database connection.
            if connect:
                curseur.close()
                if(connectionOpened == True):
                    connect.close()
                    print("PostgreSQL connection is closed")

    
    def setBudget(self, b):
        self.budget = b
    
        