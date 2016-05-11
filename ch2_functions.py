#A simple script demonstrating usage of functions in Python

#A simple function
def func1():
    print "This is function 1"

func1()
print func1()
print func1

#A function accepting arguments
def func2(arg1,arg2):
    print arg1," ",arg2

func2("a",1)

#A function returning a value
def cube(x):
    return x*x*x

print cube(3)

#A function with default value for an argument
def power(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result

print power(2)
print power(2,3)
print power(x=2,num=3)

#function with variable number of arguments
def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result

print multi_add(4,5,10,4)
