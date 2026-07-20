# Multi Interitance
class Father:
    def __init__(self,father_name):
        self.fathername=father_name
        
    def work(self):
        print(f"I am Empolyee")

class Mother:
    def __init__(self,mother):
        self.mothername=mother
        
    def work(self):
        print(f"I do cooking")
        
class Child(Mother,Father):
    def __init__(self,child):
        self.child=child
        
    def play(self):
        print(f"I love to play!!")
        
h=Child("deva")
print(h.child)
h.work()
