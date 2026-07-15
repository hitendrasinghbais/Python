# Constructor
class Person:
    def __init__(self,n,o):
        print("When Object created then Constructor get called")
        self.name=n
        self.occ=o
    def info(self):
        print(f"{self.name} is a {self.occ}")
        
a=Person("Divya","CA")
a.info()
b=Person("Yash","Businessman")

b.info()

# type of constructor 
# 1. parameterized 
# 2. default
