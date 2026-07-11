# OS module
import os

if (not os.path.exists("data ")):
    os.mkdir("data")

for i in range (0,5):
    os.rename(f"Prog {i+1}" ,  f"Prog{i+1}")
    
# folders=os.listdir("100days challenge")

# print(folders)

# for folder in folders:
#     print(folder)
