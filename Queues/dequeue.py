# Queues-> deque
from collections import deque
dq = deque()
'''
dq.pop()
dq.popleft()
dq.apppend()
dq.appendleft()

'''
dq.append('varun')
dq.append(2004)
for i in range(5):
    dq.append(i)
print(dq)
for i in range(3):
    if i%2==0:
        dq.pop()
    else:
        dq.popleft()
print(dq)
dq.clear()
print(dq)