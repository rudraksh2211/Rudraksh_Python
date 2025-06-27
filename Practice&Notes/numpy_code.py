#data analysis,ml & ai , finance & economic, image & signal processing daya visualization
import numpy as np

print(np.__version__)
a=np.array([1,2,3])
print(a)
a=np.array([[1,2],[3,4]])
print(a)
print(a.dtype)
a=np.array(['A','B','C'],dtype='S')
print(a)
print(a.dtype)
a=np.array([1,2,3,4],dtype='i4')
print(a)
print(a.dtype)

#function
x=np.zeros(10)
print(x)
x=np.ones(5)
print(x)
x=np.ones([5,4],order='F')
print(x)

#list to numpy
lis=[1,2,3,4]
y=np.array(lis)
print(y)

#arrange
arr=np.arange(10)
print(arr)
arr=np.arange(1,10,2)
print(arr)

#linspace
arr=np.linspace(1,10,num=6,endpoint=False,retstep=True)
print(arr)

arr=np.random.rand(5)
print(arr)

n=np.empty((2,3))
print(n)

n=np.full((2,3),'A')
print(n)
a=np.array([1,2,3,4,5])
print(a[0])
print(a[3]+a[4])

a=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(a[0,3])
print(a[-1,-3])

#slicing
a=np.array([1,2,3,4,5])
print(a[1:4])
print(a[::2])

a=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(a[0:2,1:4:2])