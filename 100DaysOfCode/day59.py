# decorator
def greet(fx):
    def mfx(*args,**kwargs):
        print("Function start")
        fx(*args,**kwargs)
        print("Function ends")
    return mfx

@greet
def hello():
    print("Hello World!")
     
def add(a,b):
    print(a+b)
    
hello()

greet(add)(2,4)
add(4,9)
