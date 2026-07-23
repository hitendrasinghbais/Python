# multi processing
import multiprocessing
import requests
import concurrent.futures

def filedownload(url,name):
    print(f"filedownload is started {name}")
    response=requests.get(url)
    open(f"files/big1{name}.jpg","wb").write(response.content)
    print(f"filedownload is finished {name}")
    
if __name__ == "__main__" :
    url="https://picsum.photos/4000/3000"

    # pros=[]

    # for i in range(50):
    #     # filedownload(url,i)
    #     p=multiprocessing.Process(target=filedownload,args=[url,i])
    #     p.start()
    #     pros.append(p)
        
        
    # for p in pros:
    #     p.join()
        
    with concurrent.futures.ProcessPoolExecutor( )as executor:
        l1=[url for i in range(50)]
        l2=[i for i in range (50)]
        results=executor.map(filedownload, l1,l2)
        for r in results:
            print(r)
