def calculator(a,b,op):
    if op=="+":
        print(f"Sum of {a} and {b} is {a+b}")
    elif op=="-":
        print(f"Diff of {a} and {b} is {a-b}")
    elif op=="*":
        print(f"Mul of {a} and {b} is {a*b}")
    elif op=="/":
        if b==0:
            print("Can not devide by 0")
        else:
            print(f"Div of {a} and {b} is {a/b}")

a=int(input("Enter first number"))
b=int(input("Enter second number"))
op=input("Enter Operator")
calculator(a,b,op)