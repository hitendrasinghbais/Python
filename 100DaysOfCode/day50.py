# read() readline() and other method
# f=open("myfile.txt","r")
# while True:
#     line =f.readline()
#     if not line:
#         break
#     print(line)


# f=open("myfile2.txt","r")
# i=0
# while True:
#     i=i+1
   
#     line=f.readline()
#     if not line:
#         break
    
#     m1=line.split(",")[0]
#     m2=line.split(",")[1]
#     m3=line.split(",")[2]
#     print(f"Marks of student {i} in Maths is {m1}")
#     print(f"Marks of student {i} in Hindi is {m2}")
#     print(f"Marks of student {i} in SST is {m3}")
   
f=open("myfile3.txt","w")
lines=["line1","line2","line3"]
for line in lines:
    f.write(line + "\n")
f.close()
