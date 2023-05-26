import sqlite3

conn = sqlite3.connect('Base.db')
c = conn.cursor()

#Affectation avant suppression
c.execute("SELECT rowid, * FROM personne")
data_1 = c.fetchall()

#Suppression de la personne dont la rowid = 3
c.execute("DELETE from personne WHERE rowid = 3")

#Affectation avant suppression
c.execute("SELECT rowid, * FROM personne")
data_2 = c.fetchall()

#Affichage
print(data_1)
print(data_2)

conn.commit()
conn.close()
