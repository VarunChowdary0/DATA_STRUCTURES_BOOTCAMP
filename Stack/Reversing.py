# stack -> reversing
stack =[]
word  = input("> ")
for i in word:
    stack.append(i)
for x in word:
    print(stack[-1],end="")
    stack.pop()