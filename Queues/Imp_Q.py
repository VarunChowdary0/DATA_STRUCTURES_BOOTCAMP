# Queues-> Enqueue and Dequeue
from queue import Queue
Q = Queue()

n = int(input("n: "))
for i in range(n):
    ui = input("IN:> ")
    if(ui == "Dequeue"):
        print(Q.get())
    else:
        a,b=ui.split(" ")
        if a=="Enqueue":
            Q.put(b)
            print("OUT :> +",b)
        else:
            print("Invalied")
