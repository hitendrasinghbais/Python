# operator overloading
class vector :
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    
    def __add__(self,a):
        return vector(self.x + a.x ,self.y +a.y, self.z +a.z)
    
    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}k"
    
s1=vector(2,3,4)
print(s1)
s2=vector(4,6,8)
print(s2)
print(s1+s2)
