# Basic-> Frequating
import datetime
print("Enter Items: ",end=" ")
MyList = [x for x in input().split(" ")]
TheDict = {}
a = datetime.datetime.now()
for i in MyList:
    if i in TheDict.keys():
        TheDict[i]+=1
    else:
        TheDict[i]=1
b = datetime.datetime.now()
print(TheDict)
print(b-a,"sec")