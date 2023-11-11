Str_ = "axmadamxyz"
# for i in range(len(Str_)):
#     for j in range(i,len(Str_)):
#         o = (Str_[i:j])
#         if(o == o[::-1]):
#             #print(o)
n = len(Str_)
arr = [[0 for i in range(n)] for j in range(n)]
j = 0
while j < n:
    i = 0
    jflag = j
    while jflag < n:
        if j==0:
            arr[i][jflag] = 1
        else :
            if Str_[i] != Str_[jflag]:
                arr[i][jflag] = 0
            else : 
                arr[i][jflag] = arr[i+1][jflag-1]
        jflag+=1
        i+=1
    j+=1
for i in arr:
    for j in i:
        print(j,end=" ")
    print()