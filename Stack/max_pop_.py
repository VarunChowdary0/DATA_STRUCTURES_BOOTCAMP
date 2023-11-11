# max-pop 

stack = []
n=int(input("num: "))
for i in range(n):
    s = (input("> "))
    if len(stack) == 0 :
        stack.append((int(s),int(s)))
    elif s == 'd':
        stack.pop()
    else:
        stack.append((int(s),max(int(s),stack[-1][1])))
print(stack)