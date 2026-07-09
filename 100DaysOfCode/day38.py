# raising custom error 
x=int(input("Enter a value bet 5 to 11 :"))

if(x<5 or x>11):
    raise ValueError("value should be bet 5 and 11")

s=input("Enter a string name quit:")

if not s=="quit":
    raise ValueError("You should write quit")    
