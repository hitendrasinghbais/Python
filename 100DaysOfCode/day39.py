# exercise
questions = [
    [
        "What is the capital of India?",
        "Mumbai",
        "New Delhi",
        "Chennai",
        "Kolkata",
        2
    ],
    [
        "Which planet is known as the Red Planet?",
        "Earth",
        "Venus",
        "Mars",
        "Jupiter",
        3
    ],
    [
        "Who is known as the Father of Computers?",
        "Charles Babbage",
        "Alan Turing",
        "Bill Gates",
        "Steve Jobs",
        1
    ],
    [
        "Which language is used for Python programming?",
        "HTML",
        "Python",
        "Java",
        "C++",
        2
    ],
    [
        "How many days are there in a leap year?",
        "364",
        "365",
        "366",
        "367",
        3
    ]
]

levels=[1000,2000,3000,5000,10000,30000,120000]
money=0
for i in range (0,len(questions)):
    question=questions[i]
    print(f"Question for Rs.{levels[i]} ")
    print(f"{question[0]}")
    print(f"1.{question[1]}       2.{question[2]}")
    print(f"3.{question[3]}       4.{question[4]}")
    reply=int(input("Enter your option (1-4) or Enter 0 to quit :"))
    if(reply==0):
        print(f"You take home money is Rs.{levels[i-1]}")
        break
    if (reply==question[5]):
        print(f"correct answer ,you won Rs.{levels[i]}\n")
        if(i==4):
            money=10000
        elif(i==6):
            money=120000
    else:
        print(f"wrong answer, you take home money Rs.{money}")
        break
        
