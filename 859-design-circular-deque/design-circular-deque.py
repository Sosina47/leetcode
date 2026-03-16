class ListNode:
    def __init__(self, val, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next

class MyCircularDeque(ListNode):

    def __init__(self, k: int):
        self.head = None
        self.tail = None
        self.count = k

    def insertFront(self, value: int) -> bool:
        if self.count == 0:
            return False
        node = ListNode(value, None, self.head)

        if not self.tail:
            self.tail = node

        else:
            self.head.prev = node

        self.head = node
        self.count -= 1

        return True

    def insertLast(self, value: int) -> bool:
        if self.count > 0:
            node = ListNode(value, self.tail)
            
            if not self.head:
                self.head = node
                self.tail = node

            else:
                self.tail.next = node
                self.tail = node
            
            self.count -= 1
            return True

        return False

    def deleteFront(self) -> bool:
        if not self.head:
            return False 

        self.head = self.head.next
        self.count += 1
        if not self.head:
            self.tail = None            
            
        return True

    def deleteLast(self) -> bool:
        if not self.head:
            return False

        self.count += 1
        if not self.head.next:
            self.head = None
            self.tail = None
            return True

        prev = self.tail.prev
        prev.next = None 
        self.tail = prev

        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1

        return self.head.val

    def getRear(self) -> int:
        if self.isEmpty():
            return -1

        return self.tail.val

    def isEmpty(self) -> bool:
        if not self.head:
            return True

        return False

    def isFull(self) -> bool:
        if self.count == 0:
            return True
        
        return False


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()