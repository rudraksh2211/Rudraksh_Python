import sqlite3

conn=sqlite3.connect("ass4.db")
conn.execute(''' 
             update teeacher where name="Rudraksh Dusad" set salary="300000
             ''')