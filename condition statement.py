#Condition Statement
"""
#if-syntax:
if(condition):
    code
    code
else(condiction):
code
    """
#example
"""
i=int(input())
if(i>0):
    print("number is +ve")
    if(i>10):
        print("number is above 10")
    else:
        print("number is below 10")
elif i<0:
    print("number is -ve")
else:
    print("number is zero")
    """
    
    
#example2
"""
h=int(input("enter the number:"))
if h%2==0:
    print("given number is even")
else:
    print("given number is odd")
    """

#looping statements:
#1.for-syntax
"""for i in list_name:
          code
          for i in range(start:end:step):
          code"""

#example:
'''
fruit=['apple','banana','cherry']
for i in fruit:
    print(i)
#range function
for i in range(10):
    print(i)
    
for i in range(0,10,2):
    print(i)

    
#2.while
    """
while(condition):
      block of code"""
'''

'''    
i=0
while(i<10):
    print(i)
    i=i+1
    '''

#Jumping Statements:    
#1.continue
#2.break
#3.pass    

for i in range(10):
    if(i==3):
        continue
    if(i==5):
        pass
    if(i==8):
        break
    print(i)
    
    

    
    
    
