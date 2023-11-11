# Basic-> Find Winner
# race of A,B,C,D four tie -> none else winner name
Speeds = {}
names =['A','B','C','D']
count=0
WinnerName=''
for i in names : 
    Speeds[i]=int(input(f"Enter Speed of {i}: "))
winner = max(Speeds.values())
for key in Speeds:
    if(Speeds[key]==winner):
        count+=1
        WinnerName=key
if(count==1):
    print(WinnerName)
else:
    print('None')