# classes and object 
class Person:
    name="Hitendra"
    occupation="Software Developer"
    age="22"
    def info(self):
        print(f"{self.name} is a {self.occupation}" )

a=Person()
b=Person()

a.name="Devansh"
a.occupation="CA"

a.info()
b.info()
