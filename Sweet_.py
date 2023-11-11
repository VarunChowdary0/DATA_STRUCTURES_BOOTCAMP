n = int(input("N: "))
k = int(input("K: "))
MyList = [int(x) for x in input().split(" ")]
Sorted_ = sorted(MyList)
c = 0
def Check(Arr):
    for o in Arr:
        if(k>=o):
            return 1
        else:
            return 0

while Check(Sorted_):
    c+=1
    x = Sorted_[0] + Sorted_[1]*2
    Sorted_.append(x)
    for o in range(2):
        Sorted_.remove(Sorted_[0])
    Sorted_ = sorted(Sorted_)
print(c)
