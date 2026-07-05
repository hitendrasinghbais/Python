# Tuple is unchangable with()bracket 
tp=(23,56,34,76,54,"blue","king",45,12)
print(type(tp),tp)
print(tp[4])

if 36 in tp:
    print("Yes 34 present")
else:
    print("No present")

tp2= tp[2:9:2]
print(tp2)
