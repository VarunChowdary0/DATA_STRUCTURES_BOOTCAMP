# Basic-> Pangram
import datetime
alps = [chr(v) for v in range(ord('a'), ord('a') + 26)]
String = input("Enter The Sentence: ")
a = datetime.datetime.now()
String.lower()
isPangram= True
for x in alps:
    if x in String:
        continue
    else:
        isPangram = False
        break
b = datetime.datetime.now()
if(isPangram):
    print("Pangram")
else:
    print("Not a pangram")
print(b-a,"sec")
#https://chat.whatsapp.com/IZ2FsKBa88dekd8gfYwRyh