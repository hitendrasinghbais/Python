a=input("Enter a number:")
b=input("Enter a number:")
print("Choice the following operation you want to perform:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Nothing")
choice=input("Enter your choice:")
if choice=="1": 
    print("The sum is:",int(a)+int(b))
elif choice=="2":
    print("The difference is:",int(a)-int(b))
elif choice=="3":
    print("The product is:",int(a)*int(b))
elif choice=="4":
    print("The quotient is:",int(a)/int(b))
elif choice=="5":
    print("No operation performed.")
