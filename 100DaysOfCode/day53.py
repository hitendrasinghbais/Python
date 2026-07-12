# map, filter and reduce 
l=[1,2,3,4,5,6,7]

def sq(x):
    return x*x

newl=list(map(sq,l))
print(newl)

def nwfilter(x):
    return x>4
newnew=list(filter(nwfilter,l))
print(newnew)


# reduce function
from functools import reduce
ll=[1,2,4,8,16,32,64,128,256]
p=reduce(lambda m,n: m+n ,ll)
print(p)
