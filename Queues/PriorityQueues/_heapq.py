# heapq => priority queues
import heapq
arr = [9,20,23,1,3,29]
sorted_ = []
heapq.heapify(arr)
for i in range(len(arr)):
    sorted_.append(heapq.heappop(arr))
print(sorted_)
