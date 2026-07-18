# super keyword 
class ParentClass:
    def ParentMethod(self):
        print("Parent Method get called")
        
class ChildClass(ParentClass):
    def ParentMethod(self):
        print("ChildClass ParentMethod get called")
    def ChildMethod(self):
        print("Child Method get called")
        super().ParentMethod()
        
        
g=ChildClass()
g.ChildMethod()
g.ParentMethod()

print("\n")

# -------------------------------------------------------------------
#  Now for constructor
class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id =id 
        
class Programmer(Employee):
    def __init__(self,name,id,lang):
        super().__init__(name,id)
        self.lang=lang
        
e=Employee("Harry",345)
print(e.name,e.id)

p=Programmer("Hitendra",1057,"Python")
print(p.name,p.id,p.lang)
