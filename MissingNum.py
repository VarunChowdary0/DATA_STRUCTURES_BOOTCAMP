#array = [int(X) for x in input().split()]
def FindMissingNumber(arr , n):
    c = n+1
    ActualSum = c*(c+1)/2
    arrSum = 0
    for x in arr:
        arrSum += x
    return int(ActualSum-arrSum)
Arr = [6,1,5,8,3,2,4]
print(FindMissingNumber(Arr,len(Arr)))