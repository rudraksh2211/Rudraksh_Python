a=int(input("Enter Number"))
for x in range(1,11,2):
      print(f"{a}*{x}={a*x}")
fact=1
for x in range(1,a+1):
    fact=fact*x
print(fact)

for x in range(2,10):
    for y in range(1,11):
        print(f"{x}*{y}={x*y}")
    print()
    
