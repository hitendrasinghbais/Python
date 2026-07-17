#  Instance variable vs class variable
class Employee:
    CompanyName="Apple"
    EmployeeNo=0
    def __init__(self,name):
        self.name= name
        self.salary=1000
        Employee.EmployeeNo+=1
        
    def show(self):
        print(f"The name of Employee is {self.name}sized {Employee.EmployeeNo} working in {self.CompanyName} and its salary is {self.salary}")
  
# Employee.show(e)        
e1=Employee("Ram")
e1.CompanyName="Samsung"
e1.show()

Employee.CompanyName="Microsoft"
print(Employee.CompanyName)

e2=Employee("Shaym")
e2.salary=1200
e2.show()
