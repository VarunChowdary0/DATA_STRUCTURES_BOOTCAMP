def getMergedSortedArr(arr1,arr2):
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
arr1 = [1,3]
arr2 = [4,2]
print(getMergedSortedArr(arr1,arr2))
        
