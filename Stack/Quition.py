# stack ->perform push and pop

n = int(input("> "))
stack =[]
def push(y):
    stack.append(y)

res = []
for i in range(n):
    x = input()
    if(x=='pop'):
        if(len(stack)==0):
            res.append('Empty')
        else:
            res.append(f'pop-{stack[-1]}')
            stack.pop()
    else:
        a,b = x.split(" " or "\n")
        if(a=='push'):
            push(b)
            res.append(f'push-{b}')
        else:
            print("Invalied")
for y in res:
    print(y)