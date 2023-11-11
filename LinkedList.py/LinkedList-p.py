class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.previous = None

class Doubly_Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def Insert_End(self,data):
        if self.head == None : 
            self.head = Node(data)
            self.tail = self.head
        else : 
            new_node = Node(data)
            self.tail.next = new_node
            self.tail.previous = self.tail
            self.tail = new_node
    def Insert_Start(self,data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            new_node.previous = None
    def Delete_End(self):
        if self.head != None:
            pass
    def Print_List(self):
        temp = self.head
        if temp == None:
            print("List is Empty")
            return
        while temp != None:
            print(temp.data,end=" <--> ")
            temp = temp.next
        print("None")
        return
DL = Doubly_Linked_List()
DL.Insert_End(200)
DL.Insert_End(300)
DL.Insert_End(400)
DL.Insert_Start(0)
DL.Print_List()