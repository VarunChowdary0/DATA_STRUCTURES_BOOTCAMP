
# Queues-> queue simulation using a list.

q  =[]
def put(x):
    q.append(x)
def get():
    if(len(q)==0):
        return "Empty"
    else:
        temp = q[0]
        q.remove(q[0])
        return temp
n = int(input("n: "))
for i in range(n):
    ui = input("IN:> ")
    if(ui == "get"):
        print(get())
    else:
        a,b=ui.split(" ")
        if a=="put":
            put(b)
            print("OUT :> +",b)
        else:
            print("Invalied")

