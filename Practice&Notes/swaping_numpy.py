import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9,0])
print(arr)
print(arr[2])
arr[0],arr[2]=arr[2],arr[0]
print(arr)

arr=np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
arr[[0,2],:]=arr[[2,0],:]
print(arr)

arr=np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
arr[1,2],arr[2,1]=arr[2,1],arr[1,2]
print(arr)

arr=np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
arr[:,[0,2]]=arr[:,[2,0]]
print(arr)

arr=np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]],[[13,14,15,16],[17,18,19,20],[21,22,23,24]]])
arr[:,:,[0,2]]=arr[:,:,[2,0]]
print(arr)

arr=np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]],[[13,14,15,16],[17,18,19,20],[21,22,23,24]]])
arr[:,[0,2],:]=arr[:,[2,0],:]
print(arr)

#handling missing data
arr=np.array([1,np.nan,2,np.nan,3])
res=np.isnan(arr)
print(res)

arr1=arr[~np.isnan(arr)]
print(arr1)

print(np.nan_to_num(arr,copy=True,nan=0))
