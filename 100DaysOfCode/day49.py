# file handling

# read file
f=open('myfile.txt',"r")
# print(f)
text=f.read()
print(text)
f.close()


# write file
f=open("myfile2.txt","w")
f.write("Hello ji i am writing")
f.close()

# append file
# f=open("myfile2.txt","a")
# f.write("Hello ji i am writing")
# f.close()

with open ("myfile.txt","a") as f:
    f.write("writing by with ")
