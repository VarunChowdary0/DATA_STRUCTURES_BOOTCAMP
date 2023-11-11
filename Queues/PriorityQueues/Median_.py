# heapq => priority queues Median
import heapq
arr = [int(x) for x in input().split(" ")]
sorted_ = []
heapq.heapify(arr)
for i in range(len(arr)):
    sorted_.append(heapq.heappop(arr))
if len(sorted_)%2==0:
    print((sorted_[(len(sorted_)//2)-1]+sorted_[len(sorted_)//2])/2)
else:
    print(sorted_)
    print(sorted_[(len(sorted_))//2])