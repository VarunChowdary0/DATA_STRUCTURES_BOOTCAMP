# Forward and Backward steps
def getNumberOfUniqueSteps(forward,back,String):
    x = 0
    list_of_all_steps_taken = []
    for i in String:
        list_of_all_steps_taken.append(x)
        if i == forward:
            x+=2
        elif i == back:
            x-=1
        else :
            return "String contains other characters !! "
    return len(set(list_of_all_steps_taken))

myString = input("Enter a string: ")
print("Enter forward and backward character in above string: ",end=" ") 
f,b = input().split()
print(getNumberOfUniqueSteps(f,b,myString))