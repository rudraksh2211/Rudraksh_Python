a=int(input("Enter Number"))
x=a
res=0
while x>=1:
    y=x%10
    x=x//10
    res=res*10+y
print(res)
if res==a:
    print("Palindrome")
else:
    print("Not Palindrome")