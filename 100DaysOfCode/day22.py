#  List
l=[2,3,4,"marks",45,12,"malloc","array","samsung"]
print(l)
print(type(l))
print(l[1])
print(l[-3])

if 7 in l:
    print("Yes")
else:
    print("No")
    
if "ark" in "marks":
    print("Yes")
    
print(l)
print(l[:])
print(l[2:])
print(l[1:8:2])

# list comprehension
lst=[i for i in range(7)]
print(lst)
