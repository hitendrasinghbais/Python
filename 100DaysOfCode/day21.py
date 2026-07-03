#  Function Arguments

def average(a=9,b=5):
    c=(a+b)/2
    return c



r=int(input("Enter a number:"))
s=int(input("Enter a number:"))
c=average(r,s)
print("Input avg",c)


# keyword arguments

def avg(*numbers):
    sum=0
    for i in numbers:
        sum = sum + i
    print("The avg is :",sum/len(numbers))
        
avg(45,45)
