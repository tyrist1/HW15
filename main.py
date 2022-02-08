import sqlite3

con = sqlite3.connect("animal.db")
cur = con.cursor()
sqlite_query = "SELECT * " \
               "FROM animals " \
               "WHERE  name " \

cur.execute(sqlite_query)
cur.fetchall()
con.close()



