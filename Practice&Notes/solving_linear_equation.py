import numpy as np
arr1=np.array([[3,2],[1,2]])
arr2=np.array([5,5])
res=np.linalg.solve(arr1,arr2)
print(res)

arr1=np.array([[3,-2],[2,1]])
arr2=np.array([5,5])
res=np.linalg.solve(arr1,arr2)
print(res)

arr1=np.array([[3,2],[1,2]])
arr2=np.array([5,5])
res=np.linalg.inv(arr1)
print(res)
res=np.dot(res,arr2)
print(res)