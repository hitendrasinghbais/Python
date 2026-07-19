# single inheritance
class  Person:
    def __init__(self,name,age):
        self.name=name 
        self.age=age
        
class Student(Person):
    def __init__ (self,name,age,rollno):
        super().__init__(name,age)
        self.rollno=rollno
        
    def study(self):
        print("Stundent do study")
        
class Teacher(Person):
    def __init__(self,name,age,salary):
        super().__init__(name,age)
        self.salary=salary
    def teach(self):
        print("Teacher teach")
    
h=Person("kanna",34)

print(h.name,h.age)
      
l=Student("Hitend",23,1057)
print(l.name,l.age,l.rollno)
l.study()


