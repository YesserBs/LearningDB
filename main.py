import sqlite3

conn = sqlite3.connect('Base.db') #Crée Base.db si elle n'existe pas
c = conn.cursor()


conn.commit()
conn.close()

"""
Dans ce code j'ai crée la BD Base en executant le code: le code 
crée une connxion a la bd :)"""