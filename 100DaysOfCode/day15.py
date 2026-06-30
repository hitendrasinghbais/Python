#  exercise 2 : Good morning Sir
import time
wtime=int(time.strftime("%H"))
print(wtime)


if(wtime>=4 and wtime<=12 ):
    print("Good Morning Sir")
    
elif(wtime>=13 and wtime<=16):
    print("Good Afternoon Sir")
    
elif(wtime>=17 and wtime<=19):
    print("Good Evening Sir")
else:
    print("Good Night Sir")
    
