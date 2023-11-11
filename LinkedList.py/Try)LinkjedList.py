class Node:
    def __init__ (self,data):
        self.data = data
        self.next = None
class LinkedList :
    def __init__(self):
        self.head = None
        self.tail = None
    def insertEnd(self,data):
        if self.head == None : 
            self.head = Node(data)
            self.tail = self.head
        else:
            currentTail = self.tail
            new_Tail = Node(data)
            # don't change the head create new tail
            currentTail.next = new_Tail
            self.tail = new_Tail
    def insertStart(self,data):
        if self.head == None:
            self.head =Node(data)
            self.tail =self.head
        else :
            currentHead = self.head
            # create new head 
            newHead = Node(data)
            # newHead has its next value None ->
            # and self.head gives the current head -> 
            # so set newHead.next = self.head
            newHead.next = currentHead 
            # change the current head to newhead
            self.head = newHead
    def printLinkedList(self):
        temp = self.head
        if temp == self.tail :
            print(f"| {self.head.data} |")
            return
        while temp != None:
            print('|',temp.data,end=' | ----->')
            temp = temp.next
        print(" None")
        return
    
    def deleteEnd(self):
        if self.head == self.tail: # only one node exists
            self.head = None
            self.tail =None
            return
        temp = self.head
        while temp.next != self.tail: # itterate to go to last
            temp = temp.next
        self.tail = temp # set tail to the last but one 'Node'
        self.tail.next = None # and set its next value to 'None'
        print("Last Node Deleted")

    def deleteStart(self):
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        self.head = self.head.next # just change the head of the current to next
        print("First Node Deleted")
    
    def searchKey(self,key):
        if self.head == None:
            print("List is Empty")
            return
        temp = self.head
        while temp != None:
            if key == temp.data:
                print("Found")
                return
            temp = temp.next
        print("Not Fonud")
        return

            
LL = LinkedList()
Tx = 8
while True:
    if Tx%4 == 0:
        print('''
            1 -> Insert At End [ push ]
            2 -> Insert At Start 
            3 -> Delete End [ pop ]
            4 -> Print List
            5 -> Delete Start 
            6 -> Search
            0 -> Exit
        ''')
    x  = int(input(">> "))
    Tx += 1
    match (x):
        case 1:
            a = int(input("insert end: "))
            LL.insertEnd(a)
        case 2:
            a = int(input("insert start: "))
            LL.insertStart(a)
        case 3:
            LL.deleteEnd()
        case 4:
            LL.printLinkedList()
        case 5:
            LL.deleteStart()
        case 6:
            k = int(input("Key : "))
            LL.searchKey(k)
        case 0:
            break
