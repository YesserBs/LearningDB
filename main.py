import sqlite3

conn = sqlite3.connect('Base.db')
c = conn.cursor()

#Insertion de données (1, "Yesser") dans Personne
c.execute("""INSERT INTO Personne VALUES 
    (1, "Yesser")
""")

conn.commit()
conn.close()
