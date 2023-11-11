def f(n):
    if n<=2:
        return
    f(n-2)
    print(n)
    f(n-4)
    print(n)
f(10)