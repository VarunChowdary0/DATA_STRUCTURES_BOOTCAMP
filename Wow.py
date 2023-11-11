# if num is divisor of k => print Wow else => Not So Wow
num = int(input("Enter num: "))
k = int(input("Enter k: "))
if(k%num==0):
    print("WoW")
else:
    print("Not So WoW")