import numpy as np
arr=np.array([[1,2,3],[4,5,6]])
np.save("rd.npy",arr)
res=np.load("rd.npy")
print(res)
print()
arr1=np.array([1,2,3])
arr2=np.array([[10,20,30],[40,50,60]])
arr3=np.array([[11,21,31],[41,51,61]])
np.savez("rd.npz",arr1,arr2,arr3)
res=np.load("rd.npz")
print(res['arr_0'])
print(res['arr_1'])
print(res['arr_2'])

with open('data.txt','w') as f:
    f.write("1 2 3\n4 5 6\n7 8 9")
res=np.loadtxt('data.txt')
print(res)

data=np.array([[1,2,3],[4,5,6],[7,8,9]])
np.savetxt('output.txt', data, delimiter=" ",fmt='%1.1f')

res=np.loadtxt('output.txt')
print(res)