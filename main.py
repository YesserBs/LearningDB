import sqlite3

conn = sqlite3.connect('Base.db')
c = conn.cursor()

#Affectation avant le changment
c.execute("SELECT rowid, * FROM personne")
data_1 = c.fetchall()

#Affectation apres changment et affichage
c.execute("""UPDATE personne SET Name = 'Personne_A'
WHERE Name = 'Personne_C'""")
c.execute("SELECT rowid, * FROM personne")
data_2 = c.fetchall()

print(data_1)
print(data_2)

conn.commit()
conn.close()
