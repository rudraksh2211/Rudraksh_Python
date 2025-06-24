import pandas as pd

dic={1:"Y Jaiswal",2:"KL Rahul",3:"S Sudarshan",4:"S Gill",5:"R Pant",6:"K Nair",7:"R Jadeja",8:"S Thakur",9:"J Bhumara",10:"M Siraj",10:"P Krishina"}
d=pd.Series(dic)
print(d)

lis=["Y Jaiswal","KL Rahul","S Sudarshan","S Gill","R Pant","K Nair","R Jadeja","S Thakur","J Bhumara","M Siraj","P Krishina"]
l=pd.Series(lis)
print(l)

print(l[3])
print(d[3])