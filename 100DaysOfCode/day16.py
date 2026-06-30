# match case staements

day = input("Enter day name: ")

match day:
    case "Monday":
        print("Start of the work week")
    case "Saturday" | "Sunday":
        print("It's the weekend!")
    case "Friday":
        print("Almost weekend")
    case _:
        print("Just a regular day")
