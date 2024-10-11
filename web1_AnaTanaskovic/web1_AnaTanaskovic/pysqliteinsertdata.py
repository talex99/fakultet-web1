import sqlite3
from sqlite3 import Error

def createconnection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

def main():
    database = "plantsdatabase.db"

    conn = createconnection(database)

    sql = "insert into users (username, password, role) values ('admin', '1234', 'admin')"
    cur = conn.cursor()
    cur.execute(sql)
    sql = "insert into users (username, password, role) values ('customer', '1234', 'customer')"
    cur = conn.cursor()
    cur.execute(sql)

    sql = "insert into plants (price, name) values ('255', 'Philodendron')"
    cur = conn.cursor()
    cur.execute(sql)
    sql = "insert into plants (price, name) values ('255', 'Philodendron')"
    cur = conn.cursor()
    cur.execute(sql)
    sql = "insert into plants (price, name) values ('256', 'Philodendron')"
    cur = conn.cursor()
    cur.execute(sql)
    sql = "insert into plants (price, name) values ('285', 'Philodendron')"
    cur = conn.cursor()
    cur.execute(sql)
    sql = "insert into plants (price, name) values ('785', 'Philodendron')"
    cur = conn.cursor()
    cur.execute(sql)
    sql = "insert into plants (price, name) values ('500', 'Philodendron')"
    cur = conn.cursor()
    cur.execute(sql)
    sql = "insert into plants (price, name) values ('350', 'Philodendron')"
    cur = conn.cursor()
    cur.execute(sql)
    sql = "insert into plants (price, name) values ('852', 'Philodendron')"
    cur = conn.cursor()
    cur.execute(sql)
    sql = "insert into plants (price, name) values ('888', 'Philodendron')"
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    
     
	    
if __name__ == '__main__':
    main()
