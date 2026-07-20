# Hierarchical  and Hybrid Inheritance

# Hierarchical Inheritance

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")


class Student(Person):
    def __init__(self, name, age, rollno):
        super().__init__(name, age)
        self.rollno = rollno

    def study(self):
        super().introduce()
        print(f"Roll No : {self.rollno}")
        print("Student is studying")


class Teacher(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def teach(self):
        super().introduce()
        print(f"Salary : {self.salary}")
        print("Teacher is teaching")


class Doctor(Person):
    def __init__(self, name, age, specialization):
        super().__init__(name, age)
        self.specialization = specialization

    def treat(self):
        super().introduce()
        print(f"Specialization : {self.specialization}")
        print("Doctor is treating patients")


s = Student("Hitendra", 22, 1057)
s.study()

print("----------------")

t = Teacher("Rahul", 40, 50000)
t.teach()

print("----------------")

d = Doctor("Amit", 45, "Cardiologist")
d.treat()
 
print("\n") 
print("----------------------------------------------------------------------------------------------------------------")
# Hybrid Inheritance

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_vehicle(self):
        print(f"Brand : {self.brand}")
        print(f"Model : {self.model}")


class Car(Vehicle):
    def __init__(self, brand, model, fuel_type):
        super().__init__(brand, model)
        self.fuel_type = fuel_type

    def drive(self):
        self.display_vehicle()
        print(f"Fuel Type : {self.fuel_type}")


class Electric:
    def __init__(self, battery):
        self.battery = battery

    def charge(self):
        print(f"Battery Capacity : {self.battery} kWh")


class ElectricSportsCar(Car, Electric):
    def __init__(self, brand, model, fuel_type, battery, top_speed):
        Car.__init__(self, brand, model, fuel_type)
        Electric.__init__(self, battery)
        self.top_speed = top_speed

    def race(self):
        self.drive()
        self.charge()
        print(f"Top Speed : {self.top_speed} km/h")
        print("Electric Sports Car is racing")


e = ElectricSportsCar("Tesla", "Roadster", "Electric", 100, 400)
e.race()
