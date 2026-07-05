# list method
lst=[98,27,2,4,8,8,45,23,45]
print(lst)
lst.append(99)
print(lst)

lst.sort()
print(lst)
lst.sort(reverse=True)
print(lst)
# reverse for reverse the original lst
lst.reverse()
print(lst)
# () for to find the element in list at what index
print(lst.index(45))
# [] is to find what element at index no. 
print(lst[3])
print(lst.count(8))

lst.insert(4,1998)
e=[56,34,67,78,98]
r=e+lst
print(r)
r.sort()
print(r)
