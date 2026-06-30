# if ,elif ,else and nested if statement 
a=int(input("Enter a number: "))
if(a<0):
    print("Its negative number")
elif(a>0):
    print("Its is positive number")
    if(a<100):
        print(a,"is smaller than 100")
    elif(a>100):
        print(a,"is greater than 100")
    else:
        print(a,"is equal to 100")
else:
    print(a,"is number is zero")      
