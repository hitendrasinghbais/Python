# Generatorss
def generator():
    for i in range (5):
        yield i
        
gen=generator()
print(next(gen))

print("------")
for j in gen:
    print(j)
