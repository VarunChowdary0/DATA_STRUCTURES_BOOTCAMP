arr = [int(x) for x in input().split(" ")]
sorted_= sorted(arr)
if len(sorted_)%2==0:
    print((sorted_[(len(sorted_)//2)-1]+sorted_[len(sorted_)//2])/2)
else:
    print(sorted_[(len(sorted_))//2])