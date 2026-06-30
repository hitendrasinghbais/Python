# string method 

# String are immutable 
a="HiTen"
print(a.upper())
print(a.lower())

# srtip used for remove white spaces
b="Jay Shree  Ram !!!! "
print(b.strip())

# rstrip(right side) used to remove trailing character like ??!! 
print(b.rstrip("! "))

# lsrtrip left side
print(b.lstrip(" !"))

# replace change words from all places
print(b.replace("Ram","Krishna"))

# split is method to return seperated strings as list items
print(b.split(" "))

#capitalize is method turn the string first character into upper case and rest of other in lower case , if string is first character is upper case then no effect 
print(a.capitalize()) 

# center() method align the string to center as per user given parameter
print(b.center(40))

# count() method return the number of times given value has occured within the given string
print(a.count("HiTen"))

# endswith() method checks if the string ends with a given value. if yes then true return , sles return false
print(b.endswith(" "))
print(b.endswith("Shree",4,11))

print(b.find("Shree"))

print(b.index("Shree"))

# isalnum() method return true when only cosist of A-Z,a-z,0-9
m="Welcometojungle01"
print(m.isalnum())

# isalpha ()method return true when only consist if A-Z,a-z
print(m.isalpha())

# islower() method return true when all character in string in lower case, else return false
mm="hello master ji"
print(mm.islower())

# isprintable() return true if all value given string are printable. else return false
print(m.isprintable())

# isspace() return true only if string contain white spaces
print(b.isspace())

# istitle()return true only if first letter of each word of string is capitalised else return false
print(m.istitle()) 

# startswith() check if the string start with given value is true 
print(b.startswith("Jay"))

#swapcase() lower to upper and upper to lower 
print(m.swapcase())

# title() method capitalise each letter of word 
print(mm.title()) 

# day13 imp for strings methods
