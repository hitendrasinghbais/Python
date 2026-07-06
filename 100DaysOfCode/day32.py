# sets methods in python
s1={2,4,6,8,10}
s2={4,8,12}
print(s1.union(s2))
print(s1,s2)
# s1.update(s2)
print(s1)

print(s1.intersection(s2))

print(s1.symmetric_difference(s2))
 
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print(cities.isdisjoint(cities2))

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul"}
print(cities.issuperset(cities2))
cities3 = {"Seoul", "Madrid","Kabul"}
print(cities.issuperset(cities3))
