# translate message into secret message
import random
a=input("Enter your name :")

chars = "abcdefghijklmnopqrstuvwxyz"
start= random.choice(chars)+random.choice(chars)+random.choice(chars)
end= random.choice(chars)+random.choice(chars)+random.choice(chars)
s=list(start)
e=list(end)
l=list(a)
g=len(l)
r=l.pop(0)
l.append(r)
t=s+l+e
for i in range(0,len(t)):
    print(t[i],end="")

