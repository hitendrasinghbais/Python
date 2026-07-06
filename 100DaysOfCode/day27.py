# Exercise 3

question=[
    ["Q1. What is the capital of India?","A. Mumbai","B. New Delhi","C. Chennai","D. Kolkata","B"],
 ["Q2. Which planet is known as the Red Planet?","A. Earth","B. Venus","C. Mars","D. Jupiter","C"]
]
print(question[0][0])
print(question[0][1])
print(question[0][2])
print(question[0][3])
print(question[0][4])

a=input("Enter your option :")
if(a=="B"):
    print("correct answer","Win Rs1100")
    print(question[1][0])
    print(question[1][1])
    print(question[1][2])
    print(question[1][3])
    print(question[1][4])
    
    a=input("Enter your option :")
    if(a=="C"):
        print("correct answer win Rs2100")
    else:
        print("wrong answer but win Rs1100")
else:
    print("wrong answer")

