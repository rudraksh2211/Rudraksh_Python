try: 
    ni=int(input("Enter number"))
    x=10/ni
    print(x)
except ZeroDivisionError:
    print("Can not devide by zero")
except ValueError:
    print("Number Required")
except SyntaxError:
    print("Syntext error")