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
    curs.execute("SELECT id, price, name FROM plants")
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
if not username:
    print("<meta http-equiv='refresh' content='0; url=login.py'>")
print("""
		<title>Main Page</title>
        <link rel="stylesheet" type="text/css" href="/index.css">
        <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
        <script src="/index.js"></script>
	</head>
	<body>
        <div class="container">
            <div class="header">
                <h1>Kuca cveca</h1>
            </div>
            <div class="menu">
                <div>
                    <a href="">Home</a>
""")
if isAdmin:
    print("<a href='admin-panel.py?username={}'>Admin panel</a>".format(username))
print("""
                </div>
                <a href="login.py" class="logout-button">Logout</a>
            </div>
            <div class="content">
                <div class="title">Vaznost sobnog cveca</div>
                    <div class="text">
                       Sobno cvece prisutno je vekovima i oduvek je imalo znacajnu ulogu u ulepsavanju prostora i poboljsanju kvaliteta zivota. Cvece ne samo da doprinosi estetici doma, vec i pozitivno utice na zdravlje, raspolozenje i kvalitet vazduha u zatvorenim prostorijama.
      <br><br>
                        Svaka biljka unosi jedinstven sarm i karakter u prostor, a mnoge od njih imaju sposobnost da preciscavaju vazduh od toksina i osveze atmosferu. Sobno cvece moze biti kljucni dekorativni element, ali i simbol brige o sebi i prirodi. U razlicitim stilovima i vrstama, biljke se mogu prilagoditi svakom domu, bilo da volite jednostavne sukulente ili bujno zelenilo velikih biljaka.
    <br><br>
                         Pored estetskog doprinosa, sobno cvece ima dug vek trajanja ako se pravilno neguje, a mnoge biljke se mogu odrzavati godinama, pa cak i prenositi iz generacije u generaciju. Bez obzira na budzet, postoji biljka za svakoga, od pristupacnih i jednostavnih za održavanje biljaka, do egzoticnijih vrsta koje zahtevaju vise paznje.
    <br><br>
                         U danasnjem brzom i stresnom nacinu zivota, sobno cvece moze uneti mir i ravnotezu u nas svakodnevni prostor. Biljke nas podsecaju na prirodu, smanjuju stres i pomazu u stvaranju prijatnog i zdravijeg okruzenja u domu ili kancelariji.
   </div>
                </div>
""")
print("<div id='plantsGrid' style='display: flex; flex-wrap: wrap; justify-content: center; padding-bottom: 40px;'>")
for plant in plants:
    print("""
    <div class='plant-card' id="plant-{0}">
        <div class='plant-price'>{1}</div>
        <div class='plant-name'>{2}</div>
        <div class="card-image">
				<img src="/plant.jpeg" alt="{1} {2}">
        </div>
        <button onclick='purchaseplant({0})' class="purchase-btn" id="{0}">Kupi</button>
    </div>
    """.format(plant[0], plant[1], plant[2]))
print("""
</div>

            <div class='modal-overlay'>
                <div class='modal-dialog'>
                    <div class="modal-header">
                        Kupovina je uspesna!
                    </div>
                    <div class="modal-body">
                        Hvala Vam na poverenju!
                    </div>
                    <div class="modal-footer">
                        <button class="modal-close-btn">Zatvori</button>
                    </div>
                </div>
            </div>
	</body>
</html>
""")

