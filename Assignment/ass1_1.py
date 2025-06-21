name=input("Enter Name")
cls=input("Enter Class")
m1=int(input("Enter the marks of English"))
m2=int(input("Enter the marks of Hindi"))
m3=int(input("Enter the marks of SST"))
m4=int(input("Enter the marks of Maths"))
m5=int(input("Enter the marks of Science"))
per=(m1+m2+m3+m4+m5)/5
if per>90:
    g="Grade A"
elif per>75:
    g="Grade B"
elif per>60:
    g="Grade C"
elif per>45:
    g="Grade D"
else:
    g="Fail"
print(name,cls,per,g,sep=" ")

#print("pre is even") if per %2==0 else print("odd")
