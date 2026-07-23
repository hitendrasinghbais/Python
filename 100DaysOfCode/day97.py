# multi threading

import time
import threading
from concurrent.futures import ThreadPoolExecutor
def func(seconds):
    time.sleep(seconds)
    print(f"the function goes to sleep for {seconds} seconds")
    return seconds
# normal code 
# func(2)
# func(4)
# func(3)
def main():
    time1=time.perf_counter()

    #  multi threading
    t1=threading.Thread(target=func,args=[7])
    t2=threading.Thread(target=func,args=[3])
    t3=threading.Thread(target=func,args=[4])

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()


    time2=time.perf_counter()
    print(time2-time1)

def poolingDemo():
    with ThreadPoolExecutor() as executor:
        # future1 =executor.submit(func,8)
        # future2=executor.submit(func,2)
        # future3=executor.submit(func,9)
        # print(future1.result())
        # print(future2.result())
        # print(future3.result())
        l=[1,3,2,5,1]
        results=executor.map(func,l)
        for result in results:
            print(result)
poolingDemo()
