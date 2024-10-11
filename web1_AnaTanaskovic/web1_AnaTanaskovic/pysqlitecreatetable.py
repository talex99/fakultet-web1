import sqlite3
from sqlite3 import Error


def createconnection(dbfile):
    conn = None
    try:
        conn = sqlite3.connect(dbfile)
        return conn
    except Error as e:
        print(e)

    return conn


def createtable(conn, createtablesql):
    try:
        c = conn.cursor()
        c.execute(createtablesql)
    except Error as e:
        print(e)


def main():
    database = "plantsdatabase.db"

    sqlcreateuserstable = """ CREATE TABLE IF NOT EXISTS users (
                                id integer primary key autoincrement, 
                                username varchar(20),
                                password varchar(20),
                                role varchar(20) default 'admin'
                            ); """
                                    
    sqlcreateplantstable = """ CREATE TABLE IF NOT EXISTS plants (
                                id integer primary key autoincrement,
                                price varchar(20),
                                name varchar(20)
                            ); """

    conn = createconnection(database)

    if conn is not None:  
        createtable(conn, sqlcreateuserstable)
        createtable(conn, sqlcreateplantstable) 
        
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()
