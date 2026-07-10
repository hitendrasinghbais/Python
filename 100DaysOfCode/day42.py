# enumerate function
marks=[23,3,44,56,78,54,78]
 
index=0
for mark in marks:
    print(mark)
    if(index==5):
        print("i am on index 5")
    index+=1    

print("\n")

for index,mark in enumerate(marks,start=2):
    print(mark)
    if(index==5):
        print("i am on index 5")
 
