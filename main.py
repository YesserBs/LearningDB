import sqlite3

conn = sqlite3.connect('Base.db')
c = conn.cursor()

#La rowid est la clé primaire, donc le mecanisme est pret. pas besoin de faire un champ ID comme je l'ai deja fait
c.execute("SELECT rowid, * FROM personne")
data = c.fetchone()
print(data)

conn.commit()
conn.close()
