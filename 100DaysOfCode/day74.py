# Method Overriding
class shape:
    def __init__ (self,x):
        self.x=x
    
    def area(self):
        return self.x * self.x

class circle(shape):
    def __init__(self,radius):
        self.radius=radius
        super().__init__(radius)
        
    def area(self):
        return 3.14 * super().area()

t=shape(3)
print(t.area())   
h=circle(2)
print(h.area())    

print("\n")
# -------------------------------------------------------
# Another Example
class animal:
    def sound(self):
        print(f"Animal makes a sound")
    
class dog(animal):
    def sound(self):
        super().sound()
        print(f"Dog barks")
        
# m=animal()
# m.sound()
n=dog()
n.sound()
