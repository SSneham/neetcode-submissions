class MyCircularQueue:

    def __init__(self, k: int):
        self.arr = [-1]*k
        self.front, self.rear = -1, -1
        self.k = k

    def enQueue(self, value: int) -> bool:
        if (self.rear + 1)%self.k == self.front:
            return False
        if self.front == -1 and self.rear == -1:
            self.front += 1
            self.rear += 1
            self.arr[self.rear] = value
        else:
            self.rear = (self.rear + 1)%self.k
            self.arr[self.rear] = value
        return True

    def deQueue(self) -> bool:
        if self.front == -1 and self.rear == -1:
            return False
        if self.front == self.rear:
            self.front, self.rear = -1, -1
        else:
            self.front = (self.front+1)%self.k
        return True


    def Front(self) -> int:
        if self.front == -1 and self.rear == -1:
            return -1
        return self.arr[self.front]

    def Rear(self) -> int:
        if self.front == -1 and self.rear == -1:
            return -1
        else:
            return self.arr[self.rear]

    def isEmpty(self) -> bool:
        if self.front == -1 and self.rear == -1:
            return True
        return False

    def isFull(self) -> bool:
        if (self.rear + 1)%self.k == self.front:
            return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()