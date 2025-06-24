import pandas

lis=[["Batting Position","Player"],
     [1,"Y Jaiswal"],
     [2,"KL Rahul"],
     [3,"S Sudarshan"],
     [4,"S Gill"],
     [5,"R Pant"],
     [6,"K Nair"],
     [7,"R Jadeja"],
     [8,"S Thakur"],
     [9,"J Bhumara"],
     [10,"M Siraj"],
     [11,"P Krishina"]]
l=pandas.DataFrame(lis)
print(l)

dic={"Batting Order":[1,2,3,4,5,6,7,8,9,10,11],"Player":["Y Jaiswal","KL Rahul","S Sudarshan","S Gill","R Pant","K Nair","R Jadeja","S Thakur","J Bhumara","M Siraj","P Krishina"]}
d=pandas.DataFrame(dic)
print(d)