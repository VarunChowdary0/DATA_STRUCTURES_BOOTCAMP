class Node:
    def __init__(self,data):
        self.data = data
        self.left  = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    # def Insert(self,a,temp):
    #     if temp == None:
    #         return Node(a)
    #     if a < temp.data:
    #         temp.left = self.Insert(a,temp.left)
    #     else:
    #         temp.right = self.Insert(a,temp.right)

    def Insert(self,a):
        depth = 0
        if self.root == None:
            self.root = Node(a)
        else:
            temp = self.root
            newNode = Node(a)
            parent = self.root
            while True:
                depth += 1
                if newNode.data < temp.data:
                    temp = temp.left
                    if temp == None:
                        parent.left = newNode
                        break
                    parent = parent.left
                else:
                    temp = temp.right
                    if temp == None:
                        parent.right = newNode
                        break
                    parent.right
            print(f"Current Depth: ",depth)
    def fullBinarytreee(self,temp):
        if temp == None:
            return True
        elif temp.left ==None and temp.right != None:
            return False
        elif temp.left !=None and temp.right == None:
            return False
        else:
            return self.fullBinarytreee(temp.left) and self.fullBinarytreee(temp.right)
    def preOrder(self,temp):
         if temp != None:
            print(temp.data,end=" - ")
            self.preOrder(temp.left)
            self.preOrder(temp.right)
    

# depth of all 

BST = BinarySearchTree()
n = int(input("Enter the number of nodes: "))
for i in range(n):
    a = int(input("Enter value : "))
    BST.Insert(a)
BST.preOrder(BST.root)