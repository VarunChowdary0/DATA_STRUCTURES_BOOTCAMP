a = [int(x) for x in input().split(" ")]
n = len(a)
for i in range(0,n):
    ans = -1
    for j in range(i+1,n):
        if a[j]>a[i]:
            ans = a[j]
            break
    print(ans)
