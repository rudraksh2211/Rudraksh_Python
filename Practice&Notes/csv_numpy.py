import numpy as np
with open('data.csv','w') as f:
    f.write("1,2,3\n4,5,6\n7,8,9")
res=np.genfromtxt('data.csv',delimiter=",")
print(res)