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


    def PrintMiddle(self):
        temp = self.head
        x = 0
        mid = count//2 +1
        while temp != None:
            x +=1
            if x == mid:
                print("Middle Node data",temp.data)
                print("Middle Node next object Address",temp.next)
                break
            temp = temp.next
    
    def PrintMiddle_2(self):
        if self.head == None:
            print("Empty List")
            return
        t1 = self.head
        t2 = self.head
        while t2 !=None and t2.next !=None:
            t1=t1.next
            t2=t2.next.next
        print(t1.data)
    
    def ReverseTheList(self):
        if self.head != None :
            prev = None
            current = self.head
            temp = self.head
            while current != None:
                next = current.next
                current.next = prev
                prev = current
                current = next
            self.head = prev
            self.tail = temp
        self.PrintList()
    
    def Rotate_List(self,k,length):
        if self.head != None:
            k = k % length
            while k != 0 :
                temp1 = self.head
                while temp1.next != self.tail:
                    temp1  = temp1.next
                temp2 = self.tail
                self.tail = temp1
                self.tail.next = None
                temp2.next = self.head
                self.head = temp2

    def deleteLastOccurance(self,a):
        if self.head != None:
            temp1 = self.head
            while temp1 != None : 
                pass


LL = LinkedList()
count = 0
while True:
    print("------------------------------")
    print('''
            1 -> Insert
            2 -> Insert at start
            3 -> Print Linked list
            4 -> Delete at end [ pop ]
            5 -> Delete at Start 
            6 -> Print Middle
            7 -> Prind List Detailed
            8 -> Reverse the List
            9 -> Rotate List
            0 -> EXIT
          ''')
    a = int(input("Choice: "))
    match (a):
        case 0:
            break
        case 1:
            x = int(input("Insert : "))
            print("------------------------------")
            LL.Insert(x)
            count+=1
        case 2:
            x = int(input("Insert Start: "))
            print("------------------------------")
            LL.Insert_Begining(x)
            count+=1
        case 3:
            print("------------------------------")
            LL.PrintList()
        case 4:
            print("------------------------------")
            LL.Delete_End()
        case 5:
            print("------------------------------")
            LL.Delete_Start()
        case 6:
            print("--------------------------------")
            LL.PrintMiddle_2()
        case 7:
            print("----------------------------------")
            LL.PrintList_Detail()
        case 8:
            print("----------------------------------")
            LL.ReverseTheList()
        case 9:
            print("----------------------------------")
            k = 2
            l=count
            LL.Rotate_List(k,l)
'''
    1 -> Stack using Linked List  ? [ insert at end and pop (delete) at end  ]
    2 -> Queue using Linked list  ? [ inseet at end and pop (delete) at start]
'''

# delete all occurences form a given node
