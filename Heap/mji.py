class MaxHeap:
    def _init_(self):
        self.lastIndex = 0
        self.arr = [0] * 10

    def push(self, ele):
        self.arr[self.lastIndex] = ele
        currentIndex = self.lastIndex
        while self.hasParent(currentIndex) and self.arr[currentIndex] > self.arr[self.getParentIndex(currentIndex)]:
            self.arr[currentIndex], self.arr[self.getParentIndex(currentIndex)] = self.arr[self.getParentIndex(currentIndex)], self.arr[currentIndex]
            currentIndex = self.getParentIndex(currentIndex)
        self.lastIndex = self.lastIndex + 1

    def pop(self):
        if self.isEmpty():
            return None

        poppedElement = self.arr[0]
        self.arr[0] = self.arr[self.lastIndex - 1]
        currentIndex = 0

        while self.hasLeftChild(currentIndex):
            maxChildIndex = currentIndex
            leftChildIndex = self.getLeftChildIndex(currentIndex)
            rightChildIndex = self.getRightChildIndex(currentIndex)

            if leftChildIndex < self.lastIndex and self.arr[leftChildIndex] > self.arr[maxChildIndex]:
                maxChildIndex = leftChildIndex
            if rightChildIndex < self.lastIndex and self.arr[rightChildIndex] > self.arr[maxChildIndex]:
                maxChildIndex = rightChildIndex

            if maxChildIndex == currentIndex:
                break

            self.arr[maxChildIndex], self.arr[currentIndex] = self.arr[currentIndex], self.arr[maxChildIndex]
            currentIndex = maxChildIndex

        self.lastIndex = self.lastIndex - 1
        return poppedElement

    def getParentIndex(self, index):
        return (index - 1) // 2

    def getLeftChildIndex(self, index):
        return 2 * index + 1

    def getRightChildIndex(self, index):
        return 2 * index + 2

    def hasParent(self, index):
        return (index - 1) // 2 >= 0

    def hasLeftChild(self, index):
        return 2 * index + 1 < self.lastIndex

    def hasRightChild(self, index):
        return 2 * index + 2 < self.lastIndex

    def isEmpty(self):
        return self.lastIndex == 0

mh = MaxHeap()
mh.push(20)
mh.push(10)
mh.push(30)
mh.push(40)
mh.push(60)
mh.push(50)
mh.push(100)
mh.push(70)
mh.push(90)
mh.push(80)
while not mh.isEmpty():
    print(mh.pop())
