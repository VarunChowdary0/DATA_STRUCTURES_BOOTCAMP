class Node:
    def __init__(self,data) :
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def InsertEnd(self,data):
        if( self.head == None):
            self.head = Node(data)
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = Node(data)

    def PrintList(self):
        if self.head == None:
            print("List is Empty")
        else:
            temp = self.head
            while temp != None:
                print(temp.data,end=' -> ')
                temp = temp.next
            print("None")
            return
        
LL =LinkedList()
LL.InsertEnd('Prashanth')
LL.InsertEnd('varun')
LL.InsertEnd('gay sohail')
LL.PrintList()
