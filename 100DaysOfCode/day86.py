#  walrus operator

numbers=[1,2,3,4,5,6,7,8]

while (n:=len(numbers))>0:
    print(numbers.pop())
    
# ----------------------------

happy=False
print(happy)

print(h:=True)
# --------------------------------------

foods =list()

while True:
    food=input("What food you like ? or Enter 'quit' to quit : ")
    if (food=="quit"):
        break
    foods.append(food)
print(foods)    
# ---------------------------------------
foods=list()

while(food:=input("Enter fav Car brand or Enter 'quit' to quit : ")) !="quit" :
    foods.append(food)
    
print(foods)
