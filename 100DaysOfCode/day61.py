# Inheritance in python
class Employee:
    def __init__(self,name,id):
        self.name= name
        self.id= id
    
    def info(self):
        print(f"The information of Employee : {self.id} is {self.name}")
    
class Programmer(Employee):
    def ShowLanguage(self):
        print("Default language is Python")    
e1=Employee("Rohan Das",234)
e1.info()
e2=Programmer("Jay Dubey",567)
e2.info()
e2.ShowLanguage()
