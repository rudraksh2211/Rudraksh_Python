import sqlite3

conn=sqlite3.connect("ass4.db")
conn.execute('''insert into student(name,mobile,age) values ("Rudraksh Dusad","999999999","20")''')
conn.execute('''insert into student(name,mobile,age) values ("Sachin Choudhary","999999999","21")''')
conn.execute('''insert into student(name,mobile,age) values ("Sahil Dhingra","999999999","19")''')
conn.execute('''insert into student(name,mobile,age) values ("Samyak Jain","999999999","20")''')
             
conn.execute('''insert into teacher(name,mobile,salary) values ("Rudraksh Dusad","999999999","200000")''')
conn.execute('''insert into teacher(name,mobile,salary) values ("Sachin Choudhary","999999999","210000")''')
conn.execute('''insert into teacher(name,mobile,salary) values ("Sahil Dhingra","999999999","190000")''')
conn.execute('''insert into teacher(name,mobile,salary) values ("Samyak Jain","999999999","200000")''')
             
conn.commit()
conn.close()