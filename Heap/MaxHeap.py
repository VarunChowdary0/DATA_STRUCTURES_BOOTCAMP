class MaxHeap:
    def __init__(self,size):
        self.arr = [0]*size
        self.lastIndex = 0
    def getParentIndex(self,index):
        return (index-1)//2
    def getLeftChildIndex(self,index):
        return 2*index+1
    def getRightChildIndex(self,index):
        return 2*index+2
    def hasParent(self,index):
        parentIndex = (index-1)//2
        if parentIndex < 0:
            return False
        else:
            return True
    def hasLeftChild(self,index):
        leftChildIndex = 2*index+1
        if leftChildIndex < self.lastIndex:
            return True
        else:
            return False
    def hasRightChild(self,index):
        rightChildIndex = 2*index+2
        if rightChildIndex < self.lastIndex:
            return True
        else:
            return False
    def push(self,ele):
        self.arr[self.lastIndex] = ele
        currentIndex = self.lastIndex
        while self.hasParent(currentIndex) and self.arr[self.getParentIndex(currentIndex)] < self.arr[currentIndex]:
            self.arr[currentIndex],self.arr[self.getParentIndex(currentIndex)] = self.arr[self.getParentIndex(currentIndex)],self.arr[currentIndex]
            currentIndex = self.getParentIndex(currentIndex)
        self.lastIndex = self.lastIndex+1
    def pop(self):
        if self.isEmpty():
            return None
        self.arr[0] = self.arr[self.lastIndex-1]
        currentindex = 0
        popedELE  = self.arr[0]
        while self.hasLeftChild(currentindex):
            maxIndex = currentindex
            if self.hasLeftChild(currentindex) and self.arr[self.getLeftChildIndex(currentindex) > self.arr[self.getLeftChildIndex(currentindex)]] :
                maxIndex = self.getLeftChildIndex(currentindex)
            if self.hasRightChild(currentindex) and self.arr[self.getRightChildIndex(currentindex) > self.arr[self.getRightChildIndex(currentindex)]] :
                maxIndex = self.getRightChildIndex(currentindex)
            if maxIndex == currentindex:
                break
            self.arr[currentindex],self.arr[maxIndex] = self.arr[maxIndex] , self.arr[currentindex]
            currentindex = maxIndex
        self.lastIndex = self.lastIndex - 1
        return popedELE
    def isEmpty(self) :
        return (self.lastIndex == 0)
    def Print(self):
        print(self.arr)
n = int(input("heap Length: "))
max_heap = MaxHeap(n)
for i in range(n):
    x = int(input(">>"))
    max_heap.push(x)
max_heap.Print()
print(max_heap.pop())
max_heap.Print()
print(max_heap.pop())
max_heap.Print()
print(max_heap.pop())
max_heap.Print()
print(max_heap.pop())
max_heap.Print()