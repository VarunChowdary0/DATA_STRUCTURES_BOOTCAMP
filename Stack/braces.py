# stack->  check for correct braces

s = input("> ")
stack = []
for ch in s :
    if ch in ['(','{','[']:
        stack.append(ch)
    elif ch in [')','}',']']:
        if len(stack)>0:
            if stack[-1] == '[' and ch == ']':
                stack.pop()
            elif stack[-1] == '{' and ch == '}':
                stack.pop()
            elif stack[-1] == '(' and  ch ==')':
                stack.pop()
            else:
                break
if len(stack)==0 and len(s)%2 == 0:
    print("yes")
else:
    print("no")