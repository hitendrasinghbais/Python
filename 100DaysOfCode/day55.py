import random
l=[
    ["Draw","Lose","Win"],
    ["Win","Draw","Lose"],
    ["Lose","Win","Draw"]]

print("Select One Option from below:")
print("1.Stone" ,   "2.Paper" , "3.Scissor")

g=["Stone","Paper","Scissor"]
a=int(input("Enter option no. :"))
a-=1
print("\n")
print("User choice :",g[a] )


r=[0,1,2]
b=random.choice(r)

print("CPU Choice :",g[b])

print("\n")
print("You",l[a][b],"the Game")

