import sqlite3

conn=sqlite3.connect("ass4.db")
conn.execute(''' 
             update teacher set salary="400000" where name="Rudraksh Dusad"
             ''')
d=input("Enter ID which want to delete")
conn.execute("DELETE FROM teacher where teacher_id ="+d)
conn.commit()
conn.close()