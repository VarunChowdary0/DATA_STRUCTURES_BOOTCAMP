# heapq => priority queues
import heapq
arr = [int(x) for x in input().split()]
sorted_ = []
heapq.heapify(arr)
for i in range(len(arr)):
    sorted_.append(heapq.heappop(arr))
print(sorted_)
