print("Running operator.py")

a=int(input("Enter value"))
b=int(input("Enter value"))
c=int(input("Enter value"))
d=int(input("Enter value"))
e=int(input("Enter value"))
#arithmatic
add=a+b
print(add)
sub=a-b
print(sub)
mul=a*b
print(mul)
div=(a/b)
print(div)
exp=a**b
print(exp)
flo=a//b
print(flo)
mod=a%b
print(mod)
bodmas=(a+b-c*d/e)
print(bodmas)

#assignement
#-> =,+=,-+ ..........

#comparision
#-> ==,!=,>,<,<=,>= ...........

#logical
print(a and b)
print(a or b)

#conditional
if  a>10 :
    print(5)
    if a % 2 ==0: 
      print("even")
    else:
      print("Odd") 
               
#convert into boolean
print(bin(a))    

#loop
for a in range(1,10,2):
  print(a)
for a in range(9,0,-1):
  print(a)

while (a<10):
  print("Hello")
  a+=1


#continue and break

#nested loop
for x in range(1,6):
    for y in range(1,x):
        print(x,end="")
    print()
    