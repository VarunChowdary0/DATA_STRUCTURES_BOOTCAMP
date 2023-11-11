def mergeSortTwoArrays(arr1,arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    sortedArr = [ 0  for i in range(n1+n2)]
    i,j,k = 0,0,0
    while i<n1 or j<n2:
        if i>=n1:
            while j<n2:
                sortedArr[k] = arr2[j]
                k+=1
                j+=1
        elif j<=n2:
            while i<n1:
                sortedArr[k] = arr1[i]
                i+=1
                k+=1
        else:
            if arr1[i] < arr2[i] : 
                sortedArr[k] = arr1[i]
                i+=1
                k+=1
            else:
                sortedArr[k] = arr2[j]
                j+=1
                k+=1
    return sortedArr

def getMergedSortedLists(Arr):
    ans = []
    if len(Arr)== 1:
        return Arr[0]
    else:
        ans = mergeSortTwoArrays(Arr[0],Arr[1])
    
    i=2
    while i<len(Arr):
        ans = mergeSortTwoArrays(ans,Arr[i])
        i+=1
    print(ans)


Arr = [[2,8,9,12],[15,17],[-1,3,15,19],[6,7,9,11]]

getMergedSortedLists(Arr)