from multiprocessing import Process,Queue
import random
def getRandomNumber(q):
    q.put(random.randint(0,10))

def writeRandomNumber(q):
    while not q.empty():
        print(q.get());

if __name__ == "__main__":
    q = Queue()
    p1 = Process(target = getRandomNumber,args=(q,))
    p2 = Process(target = writeRandomNumber,args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()