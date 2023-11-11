# Basic-> Fearful 
# Number is Fearful if K it is divisible by K and between LOW and HIGH else : CUTE
Num = int(input("Enter Number: "))
k = int(input("Enter K: "))
low = int(input("Enter LOW: "))
high = int(input("Enter HIGH: "))
if (Num%k==0 and low<Num<high) :
    print("FEARFUL")
else:
    print("CUTE")