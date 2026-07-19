#  Magic/Dunder
from emp import Employee 
       
r=Employee("hitendra")
print(r.name)
print(len(r))
r()
print(str(r))
print(repr(r))


----------------------------------------------------------------------
# emp.py

class Employee:
    def __init__(self,name):
        self.name=name
    
    def __len__(self):
        i=0
        for y in self.name:
            i=i+1
        return i
    
    def __str__(self):
        return f"The name of employee is {self.name}"

    def __repr__(self):
        return f"Employee {self.name }"
    
    def __call__(self):
        print(f"The call function has been called")
