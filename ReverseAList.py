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
        return self.tail

    def deleteStart(self):
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        self.head = self.head.next # just change the head of the current to next
        print("First Node Deleted")

    def RevList(head):
        temp = head
        st =[]
        while temp:
            st.append(temp.data)
            temp = temp.next
        temp = head
        while temp:
            temp.data = st.pop()
            temp = temp.next

List = LinkedList()
Stack = LinkedList()

List.insertEnd(2)
List.insertEnd('g')
List.insertEnd(15)
List.insertEnd(8)
List.insertEnd(7)
List.RevList()


# url = 'src="https://lh3.googleusercontent.com/u/0/d/<code>=w2000-h4180-iv1"'
# Arr  = ['1BPwCIspHAMmnLItKD890QcMBViuwclLS',
#         '1CUUx_U1LluTAZ7DCdVGQ-v303H4MwSK8',
#         '1SStGoycMtNl-zwlFS3BL390ACr-vQBtT',
#         '11yz5L3wlIoGPWYtL6mBpzxNIoufpMj0S',
#         '1gFPwuX8xvm52z6145UbjZdeuPykQ3R5N',
#         '1BW8OxeF3qvwuR-YTB_5QVgd7kgJ2VCLw']