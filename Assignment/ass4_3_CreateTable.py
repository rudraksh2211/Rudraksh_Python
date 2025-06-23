import sqlite3

conn=sqlite3.connect("ass4.db")
conn.execute('''
             Create table student(
             roll_no integer primary key autoincrement,
             name varchar(100),
             mobile varchar(10),
             age integer)
             ''')
conn.execute('''
             Create table teacher(
             teacher_id integer primary key autoincrement,
             name varchar(100),
             mobile varchar(10),
             salary integer)
             ''')
conn.close()