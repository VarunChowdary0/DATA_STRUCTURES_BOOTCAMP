arr= [3,8,-1,4,12,16]
#     0 1 2  3  4  5
Qs = [[1,3],[2,5],[4,5],[1,5]]
allSum = 0
for i in arr:
    allSum+=i
for x in Qs:
    mySum = 0
    if (x[1]-x[0]+1) > len(arr)//2:
        for  f in arr[0:x[0]+1]:
            mySum+=f
            print(arr[0:x[0]+1])
        for  j in arr[x[1]:]:
            mySum+=j
           # print(j,end=", ")
        
    else:
        for g in arr[x[0]:x[1]+1]:
            mySum+=g
    #print(mySum,end=" ")
# def getQueriesSum(arr,queries):
#     n = len(arr)
#     ps = [0  for i in range(n)]
#     for i in range(n):
#         if i ==0 : 
#             ps[i] == arr[i]
#         else  :
#             ps[i] = ps[i-1]  + arr[i]
#     for x in queries:
#         si , ei = x[0] , x[1]
#         if si ==0 :
#             print(ps[ei],end= " ")
#         else:
#             print(ps[ei]-ps[si-1],end=" ")

# arr= [3,8,-1,4,12,16]
# # #     0 1 2  3  4  5
# Qs = [[1,3],[2,5],[4,5],[1,5]]

# getQueriesSum(arr,Qs)