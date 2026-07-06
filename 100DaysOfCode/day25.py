#  operation on tuple
cars=("tata","kia","mahindra","maruti")
lcars=list(cars)
lcars.append("toyota")
lcars.pop(1)
print(lcars)
print(cars)
cars=tuple(lcars)
print(cars)

indiancars=("tata","mahindra","maruti")
outercars=("vw","vinfast","kia","huyndai")
topcars=indiancars +outercars
print(topcars)

tup1=(0,1,2,3,4,4,3,2,1,2,3,4,4,32,4)
cnt=tup1.count(4)
print("4 come ",cnt,"times in tup1")
print(len(topcars))
