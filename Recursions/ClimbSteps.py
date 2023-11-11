def Climb(n):
    if n == 1 or n == 2 :
        return n
    return Climb(n-1)+Climb(n-2)
n = int(input(">> "))
print(Climb(n))