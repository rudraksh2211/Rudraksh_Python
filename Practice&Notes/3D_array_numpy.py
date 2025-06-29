import numpy as np
arr=np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]],[[13,14,15,16],[17,18,19,20],[21,22,23,24]]])
print(arr)
print(arr.shape)
print(arr[1,2,3])

arr=np.zeros((2,3,4))
print(arr)

arr=np.ones((2,3,4))
print(arr)

arr=np.empty((2,3,4))
print(arr)

arr=np.array([1,2,3,4,5])
x=arr.copy()
arr[0]=4
print(arr)
print(x)

arr=np.array([1,2,3,4,5])
x=arr.view()
arr[0]=4
print(arr)
print(x)

print(x.base)
print(arr.base)

arr=np.array([1,2,3,4,5],ndmin=5)
print(arr)

arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
arr=arr.reshape(4,5)
print(arr)
print(arr.reshape(2,2,5))

arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(arr.reshape(2,3,2))

print(arr.reshape(-1))

#iterating
arr=np.array([1,2,3,4,5])
for x in arr:
    print(x,end="")
print()
arr=np.array([[1,2,3,4,5],[6,7,8,9,10]])
for row in arr:
    for x in row:
        print(x,end="")
print()
arr=np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]],[[13,14,15,16],[17,18,19,20],[21,22,23,24]]])
for block in arr:
    for row in block:
        for x in row:
            print(x,end="")
print()
for x in np.nditer(arr):
    print(x)
    
print(arr.ravel())
print(np.unique(arr))
print(arr.min(),arr.max())
print(arr.sum(0))
print(arr.sum(1))
print(arr.sum(2))

print(np.sqrt(arr))

arr=np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]],[[13,14,15,16],[17,18,19,20],[21,22,23,24]]])
arr1=np.array([[[10,20,30,40],[50,60,70,80],[90,100,110,120]],[[130,140,150,160],[170,180,190,200],[210,220,230,240]]])
print(arr+arr1)
print(arr-arr1)
print(arr*arr1)
print(arr/arr1)
print(arr**arr1)
print(arr%arr1)
print(arr//arr1)

arr=np.array([[1,2,3],[6,7,8]])
arr1=np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
x=arr.dot(arr1)
print(x)

print(np.transpose(arr))

arr=np.array([1,2,3,4,5])
arr1=np.array([6,7,8,9,0])
res=np.concatenate((arr,arr1))
print(res)

arr=np.array([[1,2,3],[6,7,8]])
arr1=np.array([[1,2,3],[6,7,8]])
res=np.concatenate((arr,arr1))
print(res)

#spliting
arr=np.array([1,2,3,4,5,6])
print(np.split(arr,3))

#resize
arr=np.array([[1,2,3],[6,7,8]])
arr1=np.resize(arr,(2,4))
print(arr1)

#append
arr=np.array([[1,2,3],[6,7,8]])
arr1=np.append(arr,[7,8,9])
print(arr1)

arr=np.array([[1,2,3],[6,7,8]])
arr1=np.append(arr,[[7,8,9],[1,2,3]],axis=1)
print(arr1)

#insert
arr=np.array([[1,2,3],[6,7,8]])
arr1=np.insert(arr,2,[7,8,9])
print(arr1)

#delete
arr=np.arange(12).reshape(3,4)
print(arr)
print(np.delete(arr,5))

#rearranging
arr=np.array([1,2,3,4,5,6])
result=np.flip(arr)
print(result)

#sort
print(np.sort(result))

max_index=np.argmax(arr)
min_index=np.argmin(arr)

