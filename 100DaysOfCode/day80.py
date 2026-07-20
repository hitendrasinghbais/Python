# Multi level inheritance
class vechile:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def display_vechile(self):
        print(f"Brand : {self.brand}")
        print(f"Model : {self.model}")
        
class car(vechile):
    def __init__(self,brand, model,fuel_type,seat):
        super().__init__(brand,model)
        self.fuel=fuel_type
        self.seat=seat
        
    def drive(self):
        super().display_vechile()
        print(f"Fuel : {self.fuel}")
        print(f"Seat : {self.seat}")

class sportscar(car):
    
    def __init__(self,brand, model,fuel_type,seat,color):
        super().__init__(brand,model,fuel_type,seat)
        self.color=color
           
    def turbo_model (self):
        super().drive()
        print(f"Color : {self.color}")
            
s=sportscar("BMW","X5","Petrol","2","black")
s.turbo_model()
print(sportscar.mro)
