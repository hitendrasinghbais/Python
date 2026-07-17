# Access Modifier  
class Employee:
    def __init__(self):
        self.__name="Harry"
        
obj=Employee()
# print(obj.__name) It cannot access directly
print(obj._Employee__name) # It can access indirectly
