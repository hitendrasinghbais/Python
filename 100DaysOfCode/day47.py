# translate message into secret message and then decode it also
import random
l=input("Enter your name :").split()
coding=False
if(coding):
    chars = "abcdefghijklmnopqrstuvwxyz"
    start= random.choice(chars)+random.choice(chars)+random.choice(chars)
    end= random.choice(chars)+random.choice(chars)+random.choice(chars)
    s=list(start)
    e=list(end)
    g=len(l)
    for word in l:
        word=list(word)
        if len(word)>=3:
            r=word.pop(0)
            word.append(r)
            t=s+word+e
            for i in range(0,len(t)):
                print(t[i],end="")
            print(end=" ")
        else:
            word.reverse()
            for i in range(0,len(word)):
                print(word[i],end="")
else:           
    for word in l:
        word=list(word)
        if len(word)>=9:
            word=word[3:]
            word=word[:-3]
            r=word.pop()
            word.insert(0,r)
            for i in range(0,len(word)):
                print(word[i],end="")
            print(end=" ")
        else:
            word.reverse()
            for i in range(0,len(word)):
                print(word[i],end="")
        

        
