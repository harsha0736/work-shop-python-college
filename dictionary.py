#dictionary
"""
car={"brand":"ford","model":"mustang","year":1964}
print(car)
a=dict(name="NRI",place="agiripalli")
print(a)
#accessing
print(car["brand"])
#get()
print(car.get("brand","keynotavailable"))
#inserting element
#method1
car["cost"]=300000
print(car)
#method2
car.update({"cost":3000000})
car2={"brand":"ford","model":"mustang","year":1964,"brand":"BMW"}
print(car2)

"""

# Methodes
#copy()
"""
car={"brand":"ford","model":"mustang","year":1964}
a=car.copy()
print(a)
print(a.keys())
print(a.values())
print(a.items())
print(car.get("model"))
b=a.popitem()
print(b)
#b=a.popitem("model")
#print(b)
b=a.pop("model")
print(a)
a.clear()
print(a)
del a
print(a)
"""


#example1

car={"brand":"ford","model":"mustang","year":1964}
car["cost"]="3M"
print(car)

#example2
l=[1,1,2,2,3,3,4,4,5,5]
a=set(l)
print(a)

#example3
print(print("cse"))
