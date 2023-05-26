import sqlite3

conn = sqlite3.connect('Base.db')
c = conn.cursor()

#Creation de table pour y stocker des informations plus tard
c.execute("""CREATE TABLE Personne (
    ID int,
    Name str
)""")

conn.commit()
conn.close()
