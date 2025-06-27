import numpy as np

arr=np.random.rand(4,2)
print(arr)

arr=np.empty((4,2))
print(arr)

arr=np.full((4,2),4)
print(arr)

arr=np.zeros((3,5))
print(arr)

arr=np.ones((4,3,2))
print(arr)

arr=np.arange(2,11)
arr1=arr.reshape((3,3))
print(arr1)

arr=np.empty(10)
print(arr)
arr[5]=11
print(arr)

arr=np.array([1,2,3,4,5,6,7,8,9,0])
arr1=arr[::-1]
print(arr1)

arr=np.array([1,2,3,4])
print(arr,arr.dtype)
arr=arr.astype('f')
print(arr,arr.dtype)