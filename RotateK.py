# rotate the list k times
# input 2 5 9 8 14 132
# K = 3
# out 8 14 132 2 5 9
#              - - -
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def Insert(self,data):
        if self.head == None : 
            self.head = Node(data)
            self.tail = self.head
        else : 
            current_node = Node(data)
            self.tail.next = current_node
            self.tail = current_node
        print("Inseted at End")
    def Insert_Begining(self,data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else :
            current_node = Node(data)
            current_node.next = self.head
            self.head =  current_node
        print("Inseted at start")


    def Delete_End(self):
        if self.head != None:
            if self.head == self.tail:
                self.head =None
                self.tail =None
            else:
                temp = self.head
                while temp.next != self.tail:
                    temp = temp.next
                self.tail =temp
                self.tail.next = None
                print("Deleted at End")

    def Delete_Start(self):
        if self.head != None:
            if self.head == self.tail:
                self.head =None
                self.tail =None
            else:
                self.head = self.head.next
        print("Deleted at start")


    def PrintList_Detail(self):
        temp = self.head
        while temp != None:
            if temp.next != None:
                print('|',temp.data,'|',temp.next,'|-> val |',temp.next.data,end="|| --------> ")
            else:
                print('|',temp.data,'|',temp.next,'|-> val |',temp.next,end=" || ----------> ")
            temp = temp.next
        print("None")
    def PrintList(self):
        temp = self.head
        while temp != None:
            print(temp.data,end="|-----> |")
            temp = temp.next
        print("None")
    def RotateAndSave(self,k,length):
        count = 0
        if self.head == None:
            print("Empty")
        elif self.head == self.tail:
            print(self.head.data)
        else:
            Q = []
            Stack = []
            temp = self.head
            while temp != None:
                if count < k :
                    Q.append(temp.data)
                    temp = temp.next
                else :
                    Stack.append(temp.data)
                    temp = temp.next
                count+=1
        for i in range(length):
            if i < length - k :
                print(Stack.pop(),end="  ")
            else:
                print(Q.pop(0),end=" ")
    def getLengthOfList(self):
        length = 0
        temp = self.head
        while temp.next != None:
            length += 1
            temp = temp.next
        return length  
    
    def FindMedian(self):

LL = LinkedList()
length = 0
print('''
    1 -> push
    2 -> pop
    3 -> get
    4 -> rotate
    0 -> Exit
    ''')
while True:
    ch = int(input(">>> "))
    match ch:
        case 1:
            a = input("--->> ")
            length+=1
            LL.Insert(a)
        case 2:
            a = input("--->> ")
            LL.Delete_End()
        case 3:
            a = input("--->> ")
            LL.Delete_Start()
        case 4:
            a = int(input("k ->> "))
            LL.RotateAndSave(a,length)
        case 0:
            break
