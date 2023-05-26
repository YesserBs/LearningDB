import sqlite3

conn = sqlite3.connect('Base.db')
c = conn.cursor()

#Selection specifique (ID > 1)
c.execute("SELECT rowid, * FROM personne WHERE Name LIKE 'Personne%'")
data = c.fetchall()
print(data)

conn.commit()
conn.close()
