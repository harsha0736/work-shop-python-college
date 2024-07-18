#String Operations


'''
a='NRI CSE'
print(len(a))
print(a[3])
print(a[6])
print(a[-1])
print(a[:-1])
print(a[0:7])
'''


"""
h='hello'
print(h[0:3])
print(h[::-1])
"""

#help(str)
#string methods
"""
a="Hello NRI CSE"
print(a.count('e'))
print(a.replace('CSE','cse-A'))
print(a.find("NRI"))
print(a.lower())
print(a.upper())
print(a.capitalize())
print(a.title())
print(a.isupper())
print(a.isdigit())
print("12".isdigit())
print('abc'.isdigit())
print("abc".isalpha())
print("abcd".startswith("abcd"))
print("abcd".endswith("s"))
print("acbd".split("b"))
print('-'.join(['a','b','c','d','e']))
print("  abc d  ".strip())
print("  abc d  ".lstrip())
print("  abc d  ".rstrip())
"""


#String Formating
a="abc"
b="xyz"
print("hello",a,b)
print("hello",a)
print(a+""+b)
print("Hello,{}{}".format(a,b))
print(f"Hello{a}{b}")
