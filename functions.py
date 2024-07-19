#FUNCTIONS:

#example1:
'''
def f1():
    print("HELLO WORLD")
    return 0
f1()
print(f1())
'''

#example2:
'''
def add(a,b):
    return a+b

a=int(input("enter value1:"))
b=int(input("enter value2:"))
print("result",add(a,b))
 '''

#types of functions
#1.positional argument
#2.keyword

def f1(a,b):
    return a+b

print(f1(10,20))


#3. default
def f1(a,b=30):
    return a+b

print(f1(10))


#4.variable lengthe argument
def f1(*args):
    print(args)
    return sum(args)
print(f1(10,20,30,40,50))
    
#5.keyword variable length:
def f1(**kargs):
    print(kargs)
    return 0
print(f1(name="NRI",branch="cse"))


#example:
def f2():
    pass





















