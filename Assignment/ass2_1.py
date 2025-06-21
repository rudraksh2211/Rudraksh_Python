l=[]
price=0
total=0
print('''   1. New Bill
            2. Create Bill
            3. Display Item Price and total bill amount
            4. Display Total
            5. Exit''')
while True:
    
    x=int(input("Enter Choice"))
    if x==1:
        total=0
        l=[]
    elif x==2:
        while True:
            price=int(input("Enter Price (Press -1 for exit)"))
            if price==-1:
                break
            else:
                l.append(price)
                total+=price
    elif x==3:
        print(l)
        print(f"Total={total}")
    elif x==4:
        print(f"Total={total}")
    elif x==5:
        print("Exit")
        break
    else:
        print("Invalid Input")