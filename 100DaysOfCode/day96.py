import time 
import asyncio
import requests

# url=""
# response=requests.get(url)
# with open ("trick1","wb").write(response.content)


async def func1():
    url="https://images.pexels.com/photos/30299053/pexels-photo-30299053.jpeg"
    response=requests.get(url)
    open ("trick1.jpg","wb").write(response.content)
    # time.sleep(3)
    await asyncio.sleep(3)
    print("func1")
    
async def func2():
    url="https://images.pexels.com/photos/534164/pexels-photo-534164.jpeg"
    response=requests.get(url)
    open ("trick2.png","wb").write(response.content)
    # time.sleep(3)
    await asyncio.sleep(14)
    print("func2")
    
async def func3():
    url="https://images.pexels.com/photos/12421204/pexels-photo-12421204.jpeg"
    response=requests.get(url)
    open ("trick3.jpg","wb").write(response.content)
    # time.sleep(3)
    await asyncio.sleep(9)
    print("func3")
    
print("program is started")
async def main():
    # task=asyncio.create_task(func1())
    # # await func1()
    # await func2()
    # await func3()
    L = await asyncio.gather(func1(),func2(),func3())
    print(L)
asyncio.run(main())
