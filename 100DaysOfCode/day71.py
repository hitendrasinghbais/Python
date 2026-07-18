# dir, __dict__ and help() method 

# dir()
# dir() func returns a list of all 
# attributes and method available 
# for an object
l=[1,2,3,4]
print(dir(l))
print(l.__add__)

# dict
# __dict__ attribute retuens a 
# dictionary representation of an
# object's attributes.
class Person :
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.value=5
        
p=Person("Rama",23)
print(p.name,p.age)
print(p.__dict__)


# help
# help() function is used to get help
# documentation for an object,including
# a description of its attributes and methods.
print(help(Person))
