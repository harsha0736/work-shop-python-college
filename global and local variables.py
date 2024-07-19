#Global and Local variables
#global ---->out of the function


x=20
def f2():
    global x
    x=10
    print(x)
f2()
print(x)

