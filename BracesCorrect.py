def RemoveOtherCharacters(String):
    myS = ''
    for ch in String:
        if ch in ('{','[','(',')',']','}'):
            myS+=ch
    return myS

def isTheStringHasCorrectBraces(String):
    String = RemoveOtherCharacters(String)
    MyStack = []
    count = 0
    for Br in String:
        if Br in ('(' , '[' , '{'):
            MyStack.append(Br)
            count+=1
        elif Br in (')','}',']'):
            if len(MyStack) != 0:
                count+=1
                if Br == ')' and MyStack[-1] =='(':
                    MyStack.pop()
                if Br == ']' and MyStack[-1] =='[':
                    MyStack.pop()
                if Br == '}' and MyStack[-1] =='{':
                    MyStack.pop()
        else : 
            break
    if len(MyStack) == 0 and len(String) == count:
        return True
    else:
        return False
myString = input("Enter a string: ")
print(isTheStringHasCorrectBraces(myString))

                