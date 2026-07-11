x=34
print(f"Value of global is {x}")

def hello():
    global x
    print("Hi from hello function")
    x=99
    print(x)
hello()    
print(f"Value of global is now {x}")
