#!/usr/bin/python3 

import sqlite3 
from sqlite3 import Error
import http.cookies
import cgi
import os
import datetime

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

form = cgi.FieldStorage()
username = form.getvalue("username")
password = form.getvalue("password")
remember = form.getvalue("remember")

if username and password and remember:
	cookie = http.cookies.SimpleCookie()
	cookie['username'] = username
	cookie['password'] = password
	cookie['username']['expires'] = 30 * 24 * 60 * 60
	cookie['password']['expires'] = 30 * 24 * 60 * 60
	username_cookie = cookie['username'].value
	password_cookie = cookie['password'].value
else:
	try:
		cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
		username_cookie = cookie['username'].value
		password_cookie = cookie['password'].value
	except (KeyError, TypeError):
		username_cookie = ""
		password_cookie = ""

def validate_login(username, password):
	sql = "select * from users where username=? and password=?"
	curs.execute(sql, (username, password))
	res = curs.fetchall()
	if res:
		return True
	else:
		return False

is_login_valid = False
if username and password:
	is_login_valid = validate_login(username, password)

print("Content-Type: text/html")
print()
print("""
<html>
	<head>
		<title>Login Page</title> """)
if username and password and is_login_valid:
	print("<meta http-equiv='refresh' content='0; url=index.py?username={0}'/>".format(username))
print("""
		<link rel="stylesheet" type="text/css" href="/login.css">
	</head>
	<body>
		<h1>Login Page</h1>
		<form action='/cgi-bin/login.py' method='get'>
			<input type='text' name='username' placeholder='Username' value={0}>
			<input type='password' name='password' placeholder='Password' value={1}>
			<div class='remember-me'>
				<input type='checkbox' id='remember-me' name='remember'>
				<label for='remember-me'>Remember me</label>
			</div>
			<input type='submit' value='Login'>
		</form>
	</body>
</html>
""".format(username_cookie, password_cookie))

if username and password and not is_login_valid:
	print("""
	<div class="error-message show-error">
		<p>Incorrect username or password. Please try again.</p>
	</div>
	""")