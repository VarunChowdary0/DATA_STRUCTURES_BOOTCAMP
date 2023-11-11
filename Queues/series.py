# Queues-> Assignment
from queue import Queue
n = int(input(">"))
q = Queue()
q.put(n)
while n:
    print(q.get())
    if(n%2==0):
        n=n//2
        q.put(n)
    elif(n%3==0):
        n=n//3
        q.put(n)
    else:
        n=n-1
        q.put(n)

