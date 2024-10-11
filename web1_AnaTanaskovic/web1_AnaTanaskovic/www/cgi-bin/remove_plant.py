#!/usr/bin/python3 

import cgi
import sqlite3
import os
from sqlite3 import Error
import json

form = cgi.FieldStorage()
plant_id = form.getvalue('plant_id')

def createconnection(dbfile):
	conn = None
	try:
		conn = sqlite3.connect(dbfile)
	except Error as e:
		print(e)
	return conn

dbfile = "plantsdatabase.db"
conn = createconnection(dbfile)	
curs = conn.cursor() 

sql = "DELETE FROM plants WHERE id=?"
curs.execute(sql, (plant_id,))
conn.commit()

sql = "SELECT id, price, name FROM plants"
curs.execute(sql)
plants = curs.fetchall()
conn.commit()

conn.close()

print("Content-Type: application/json")
print("")
print(json.dumps(plants))
