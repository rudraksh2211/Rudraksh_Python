def my_fun(a):
    print("Hello",a)
my_fun("Python")    

def sum(a=0,b=0):
    print(a+b)
    return a+b
c=sum(3)
print(c)

def sum1(*a):
    sum=0
    for x in a:
        sum=sum+x
    print(sum)
sum1(1,2,3,4)

def city(city3,city1,city2):   
    print(city1,city2,city3)
city(city1="a",city2="b",city3="c")


def city1(**city):
    print(city["city1"],city["city2"],city["city3"])
city1(city1="a",city2="b",city3="c")