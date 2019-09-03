from queue import Queue
from threading import Thread

def worker(q, n):
    while True:
        item = q.get()
        if item is None:
            break
        print("process data:", n, item)

q = Queue(13)
th1 = Thread(target=worker, args=(q, 1))
th2 = Thread(target=worker, args=(q, 2))
th3 = Thread(target=worker, args=(q, 3))
th4 = Thread(target=worker, args=(q, 4))
th5 = Thread(target=worker, args=(q, 5))

th1.start(); th2.start(); th3.start(); th4.start(); th5.start()

for i in range(50):
    q.put(i)

q.put(None); q.put(None); q.put(None); q.put(None); q.put(None)
th1.join(); th2.join(); th3.join(); th4.join(); th5.join()