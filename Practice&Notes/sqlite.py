import sqlite3

conn=sqlite3.connect("db1.db")

#for create
conn.execute('''
             Create table rudraksh2(
                 usid INTEGER PRIMARY KEY AUTOINCREMENT,
                 username VARCHAR(100),
                 pass VARCHAR(100)
             )
             ''')

#for insert
conn.execute('''
            Insert into rudraksh(username,pass) values("ABC","abc123")
             ''')

#for view
data = conn.execute('''
Select * from rudraksh
             ''')
for x in data:
    print(x)
    
#for delete
d=input("Enter ID which want to delete")
conn.execute("DELETE FROM rudraksh where usid ="+d)
conn.commit()


conn.close()