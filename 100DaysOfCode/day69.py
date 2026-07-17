# class method
class Employee:
    company="Apple"
    def show(self):
        print(f"The name of Employee {self.name} and working in {self.company}")
    
    @classmethod   
    def ChangeCompany(cls,newcompany):
        cls.company=newcompany
        
e= Employee()
e.name="Hari"
e.show()
e.ChangeCompany("Tesla")
e.show()
print(Employee.company)
