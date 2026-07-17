#  static methods
class Math:
    def __init__(self,num):
        self.num = num
    
    def addnum(self,v):
        self.num =self.num +v
        
    @staticmethod
    def add(a,b):
        print(a+b)
        
Math.add(4,6)
e=Math(5)
e.addnum(8)
print(e.num)
