# Basic-> Lexigrapgical
n = int(input("Enter Number of words: "))
MyD = {}
maxes = []
for i in range(n):
    x = input("> ")
    if x in MyD.keys():
        MyD[x]+=1
    else :
        MyD[x]=1
for i in MyD.keys():
    if MyD[i] == max(MyD.values()):
        maxes.append(i)
if(len(maxes)==1):
    print(maxes[0],MyD[maxes[0]])
else:
    print(max(maxes),MyD[max(maxes)])

