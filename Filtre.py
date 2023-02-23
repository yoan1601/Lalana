import Connection

class Filtrable:
    def __init__(self ,id, identifiant,description,latitude,longitude):
        self.id = id
        self.identifiant = identifiant
        self.description = description
        self.latitude = latitude
        self.longitude = longitude
    
    def detail(self):
        print('identifiant ', self.identifiant)
        print('description ', self.description)
        print('latitude ', self.latitude)
        print('longitude ', self.longitude)
    
    def insert(self, connect):
        try:
            connectionOpened = False
    
            if(connect == None):
                connect = Connection.getPgsqlConnection()
                connectionOpened = True
            
            curseur = connect.cursor()

            seq = 'batiment_seq'

            if(self.identifiant.__contains__('O') == True):
                seq = 'homme_seq'

            sql = """ INSERT INTO filtrable (identifiant, description, latitude, longitude) VALUES ( concat(%s , nextval(%s)) , %s, %s , %s) """            
            param = (self.identifiant, seq, self.description, self.latitude, self.longitude)

            print(sql)

            curseur.execute(sql, param)

            connect.commit()
            count = curseur.rowcount
            print(count, "insertion filtrable succes")

        except (Exception) as error:
            print("Insertion filtrable echouee", error)

        finally:
            # closing database connection.
            if connect:
                curseur.close()
                if(connectionOpened == True):
                    connect.close()
                    print("PostgreSQL connection is closed")

