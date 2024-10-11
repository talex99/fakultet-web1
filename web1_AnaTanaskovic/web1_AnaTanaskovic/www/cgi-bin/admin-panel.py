#!/usr/bin/python

import sqlite3 
from sqlite3 import Error
import http.cookies
import cgi
import os
import datetime

form = cgi.FieldStorage()
username = form.getvalue("username")

def createconnection(dbfile):
	conn = None
	try:
		conn = sqlite3.connect(dbfile)
	except Error as e:
		print(e)
	return conn

def get_plants():
    curs.execute("SELECT * FROM plants")
    plants = curs.fetchall()
    return plants

def is_admin():
    sql = "SELECT role from users where username=? and role='admin'"
    curs.execute(sql, (username,))
    found_admin = curs.fetchone()
    return True if found_admin else False

dbfile = "plantsdatabase.db"
conn = createconnection(dbfile)	
curs = conn.cursor() 

plants = get_plants()
isAdmin = is_admin()

print("Content-Type: text/html")
print()
print("""
<html>
	<head>
    """)
if not username or not isAdmin:
    print("<meta http-equiv='refresh' content='0; url=login.py'>")
print("""
		<title>Main Page</title>
        <link rel="stylesheet" type="text/css" href="/index.css">
        <link rel="stylesheet" type="text/css" href="/admin-panel.css">
        <script src="/admin-panel.js"></script>
	</head>
	<body>
        <div class="container">
            <div class="header">
                <h1>House of plants</h1>
            </div>
            <div class="menu">
                <div>
""")
print("<a href='index.py?username={}'>Home</a>".format(username))
print("""
                    <a href=''>Admin panel</a>

                </div>
                <a href="login.py" class="logout-button">Logout</a>
            </div>

            <div id='content-container' class='flexRow'>
                <div class="table-container">
                    <a onclick='showAddplantForm()' class='btn add-btn'>Add</a>
                    <table id='plantsTable'>
                        <tr>
                            <th>ID</th>
                            <th>price</th>
                            <th>Name</th>
                            <th>Action</th>
                        </tr>
""")
for plant in plants:
    plant_id = plant[0]
    price = plant[1]
    name = plant[2]

    print("""
                        <tr>
                            <td>{0}</td>
                            <td>{1}</td>
                            <td>{2}</td>
                            <td>
                                <a id='edit-plant-btn' onclick="showEditplantForm({0}, '{1}', '{2}')" class='btn'>Edit</a>
                                <a id='remove-plant-btn' onclick='deleteplant({0})' class='btn'>Delete</a>
                            </td>
                        </tr>
    """.format(plant_id, price, name, username))
print("""
                    </table>
                </div>
                <div id='form-container' class='flexColumn'></div>
            </div>
        </div>
	</body>
</html>
""")

