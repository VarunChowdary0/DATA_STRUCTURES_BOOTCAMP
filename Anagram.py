# Basic-> Anagram
str1 = input("Enter string 1: ")
str2 = input("Enter string 2: ")
l1= len(str1)
l2= len(str2)
D1 = {}
D2 = {}
if(l1==l2):
    for i in range(l1):
        if str1[i] in D1.keys():
            D1[str1[i]]+=1
        else:
            D1[str1[i]]=1

        if str2[i] in D2.keys():
            D2[str2[i]]+=1
        else:
            D2[str2[i]]=1
    if(D1==D2):
        print("Anagram")
    else:
        print("Not a Anagram")
else:
    print("Not a Anagram")