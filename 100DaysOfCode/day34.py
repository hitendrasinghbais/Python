# dictionaries methods
s1={1:90,2:67,23:56,78:56}
s2={45:89,67:23,89:23,56:12}
s1.update(s2)
print(s1)

s1.clear()
print(s1)

empty={}
print(empty)

print(s2.pop(67))
print(s2)

s2.popitem()
print(s2)
