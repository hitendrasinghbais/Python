# finally keyword
def funct():
    try:
        l=[1,2,3,4,5]
        i=int(input("Enter a number:"))
        print(l[i])
        return 1
    except:
        print("Some error occur")
        return 0
    finally:
        print("finally always run either try or except")
    
x=funct()
print(x)
