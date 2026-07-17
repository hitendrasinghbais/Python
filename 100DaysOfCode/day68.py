# Exercise -Clear the clutter
import os
print(os.getcwd())
os.chdir(r"D:\Code\100days challenge\data")
print(os.getcwd())

l=os.listdir()

g=len(os.listdir())
r=1
for i in range(0,g):
    os.rename(l[i],f"{r}.png")
    r+=1
print(os.listdir())
