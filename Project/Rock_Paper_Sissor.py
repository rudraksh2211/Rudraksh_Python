import random
ucount=0
ccount=0
x=1
list=["Rock","Paper","Sissor"]
while x==1:
    x=int(input("Enter Number of turns [5,10,15]"))
    for y in range(x):
        print('''
          Enter Choice Number
        1. Rock
        2. Paper
        3. Sissor
          ''')
        a=int(input("Enter Choice"))
        if a==1:
            user=list[0]
        elif a==2:
            user=list[1]
        elif a==3:
            user=list[2]
        elif a==4:
            break
        else:
            print("Invalid Choice")
        comp=random.choice(list)
        print("Computer choose", comp)
        if user==comp:
            print("Draw")
            ucount+=1
            ccount+=1
            print("Your Point =", ucount,"Computer Point =", ccount, sep="        ")
        elif user=="Rock" and comp=="Sissor" or user=="Paper" and comp=="Rock" or user=="Sissor" and comp=="Paper":
            print("You Won")
            ucount+=2
            print("Your Point =", ucount,"Computer Point =", ccount, sep="        ")
        else:
            print("Computer Won")
            ccount+=2
            print("Your Point =", ucount,"Computer Point =", ccount, sep="        ")

print("")
print("End of Game")
if ucount==ccount:
    print("Match Draw")
    print("Your Point =", ucount,"Computer Point =", ccount, sep="        ")
elif ucount>ccount:
    print("You Won")
    print("Your Point = ", ucount ,"Computer Point = ",ccount, sep="        ")
else:
    print("Computer Won")
    print("Your Point =", ucount,"Computer Point =", ccount , sep="        ")