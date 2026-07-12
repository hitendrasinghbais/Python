# file handing seek() tell() 
with open ("myfile.txt","r") as f:
    # move to 10th byte in the file
    f.seek(10)
    
    # read the next 5 bytes
    print(f.tell())
    data=f.read(5)
    print(data) 
    
with open("myfile3.txt","w") as f:
    f.write("Hello World Ji ")
    f.truncate(5)
    
with open ("myfile3.txt","r")as f:
    print(f.read())
