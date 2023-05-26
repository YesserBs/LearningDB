import sqlite3

conn = sqlite3.connect('Base.db')
c = conn.cursor()

#Insertion de plusieurs elements en une seule fois
Personnes = [(2, "Personne_B"), (3, "Personne_C")]
c.executemany("INSERT INTO Personne VALUES (?,?)", Personnes)

conn.commit()
conn.close()
