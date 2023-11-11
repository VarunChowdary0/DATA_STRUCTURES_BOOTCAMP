#array = [int(X) for x in input().split()]
def findMissingNumber(arr , n):
    ans = 0
    for i in range(1,n+1):
        ans = ans ^ i
    for o in arr:
        ans = ans ^ o
    return ans 
Arr = [1,2,3,4,5,6,8]
print(findMissingNumber(Arr,len(Arr)+1))