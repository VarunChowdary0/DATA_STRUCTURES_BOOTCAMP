def ArrCombs(arr):
    if len(arr) == 0:
        return []
    if len(arr) == 1:
        return [arr]
    ans = []
    for i in range(len(arr)):
        fixedEle = arr[i]
        subArr = arr[0:i] + arr[i+1:]
        allPermutation = ArrCombs(subArr)
        for premutation in allPermutation:
            ans.append([fixedEle]+premutation)
    return ans
arr = [1,2,3,4]
print(ArrCombs(arr))

