# error handling
a=input("Enter a number :")
try:
    for i in range (2,11):
        print(f"{a}x{i}={int(a)*i}")
except :
    print("Invalid Input")  
    
print("Program ends")      
        
