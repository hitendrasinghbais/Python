# class method as alternative constructors
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    @classmethod
    def fromstr(cls,string):
        return cls(string.split("-")[0],(string.split("-")[1]))
    

e=Employee("Suren",4500)
print(e.name, e.salary)

string=("Ganesh-1390")
e2=Employee.fromstr(string)
print(e2.name)
print(e2.salary)
