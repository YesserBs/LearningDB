import sqlite3

conn = sqlite3.connect('Base.db')
c = conn.cursor()

#Selection de toutes les infos d'une table
c.execute("SELECT * FROM personne")
data = c.fetchall()
print(data)

conn.commit()
conn.close()
