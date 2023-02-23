import psycopg2

def getPgsqlConnection():
    conn = psycopg2.connect(
        host="localhost",
        database="geo",
        user="postgres",
        password="root"
    )

    return conn

# Connect to the PostgreSQL database
#conn = psycopg2.connect(
#    host="localhost",
#    database="geo",
#    user="postgres",
#    password="root"
#)

# Create a cursor object
#cur = conn.cursor()

# Execute a query
#cur.execute("SELECT * FROM construction")

# Fetch the results
#results = cur.fetchall()
#print(results)

# Close the cursor and connection
#cur.close()
#conn.close()