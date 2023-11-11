# Queues-> Basic-Queues

from queue import Queue
# put() and get()
n  = int(input("Nums: "))
q = Queue()
print('0')
q.put('1')
while n>0:
    f = q.get()
    print(f)
    q.put(f+'0')
    q.put(f+'1')
    n=n-1