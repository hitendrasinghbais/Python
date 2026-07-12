# lambda function

def fun(fx,value):
    return 1000+fx(value)

m=lambda x: x*2

print(m(5))
print(fun(lambda h:h*h*h,5))

