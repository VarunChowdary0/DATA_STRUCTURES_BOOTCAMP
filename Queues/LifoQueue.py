# Queues-> LifoQueue
from queue import LifoQueue
# stack == LifoQueue 
LQ = LifoQueue(maxsize=5)
LQ.put('varun0')
LQ.put('varun1')
LQ.put('varun2')
print("isFULL :",LQ.full())
# current length of queue
print("size :",LQ.qsize())
#a  After accessing/getting the item is removed
print(LQ.get())
print(LQ.get())
print(LQ.get())
print(LQ.empty())
