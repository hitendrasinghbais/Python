# regular expressions
import re

pattern="programming"
text='''
Python is a high-level, 
general-purpose programming
language that emphasizes code
readability, simplicity, and ease-of-writing
with the use of significant indentation,[38] 
an extensive ("batteries-included") standard library,
and garbage collection. Python supports multiple 
programming paradigms but with an emphasis on object
-oriented programming and dynamic 
typing.
'''
# only for first occurance
# match=re.search(pattern,text)
# print(match)

matches=re.finditer(pattern,text)
for match in matches:
    print(match)

# type of match is tuple
