l=[]
while True:
    a=int(input("Enter Number (-1 For Exit)"))
    if a==-1:
        break
    else:
        l.append(a)
#smallest
x=len(l)
min=l[0]
for y in l:
    if min>y:
        min=y
print(min,"Smallest")

#largest
max=l[0]
for y in l:
    if max<y:
        max=y 
print(max,"Greatest")

#second smallest
l1=l
l1.remove(min)
min1=l1[0]
for y in l1:
    if min1>y:
        min1=y
print(min1,"Second Smallest")

#second greatest
l2=l
l2.remove(max)
max1=l2[0]
for y in l2:
    if max1<y:
        max1=y 
print(max1,"Second Greatest")
