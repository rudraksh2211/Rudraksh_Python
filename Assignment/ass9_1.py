import numpy as np

arr=np.array([[1,2,3],[4,5,6]])
arr1=[7,8,9]
arr2=np.append(arr,arr1)
print(arr2)

arr=np.array([[1,2,3],[4,5,6]])
print(arr.flatten())

arr=np.array([1,2,3,4,5,6])
result=np.flip(arr)
print(result)

arr=np.array([[1,2,3],[4,5,6]])
print(arr.min())
print(arr.max())
print(arr.shape)

arr=np.array([[1,2,3],[4,5,6]])
for row in arr:
    for x in row:
        print(x)
print(arr[1,1])

sum=0
arr=np.array([[1,2,3],[4,5,6]])
for row in arr:
    for x in row:
        sum+=x
print(sum)

arr=np.array([[1,2,3],[4,5,6]])
arr1=np.array([[7,8,9],[10,11,12]])
print(arr+arr1)
print(arr-arr1)
print(arr*arr1)
print(arr/arr1)