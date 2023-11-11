from queue import PriorityQueue

Customers = PriorityQueue()
n = int(input("N: "))
for i in range(n):
    key = int(input("Key: "))
    value = input("Name: ")
    myD = (key,value)
    Customers.put(myD)
while Customers:
    print(Customers.get())