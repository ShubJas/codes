class ListNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class MyCircularDeque:

    def __init__(self, k: int):
        # Initialize deque with a dummy head and dummy tail that point to each other
        self.front = ListNode(0)
        self.last = ListNode(0)
        self.front.next = self.last
        self.last.prev = self.front
        self.k = k
        self.count = 0

    def insertFront(self, value: int) -> bool:
        if self.count < self.k:
            newnode = ListNode(value)
            newnode.next = self.front.next
            newnode.prev = self.front
            self.front.next.prev = newnode
            self.front.next = newnode
            self.count += 1
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if self.count < self.k:
            newnode = ListNode(value)
            newnode.prev = self.last.prev
            newnode.next = self.last
            self.last.prev.next = newnode
            self.last.prev = newnode
            self.count += 1
            return True
        return False

    def deleteFront(self) -> bool:
        if self.count > 0:
            delete_node = self.front.next
            self.front.next = delete_node.next
            delete_node.next.prev = self.front
            self.count -= 1
            return True
        return False

    def deleteLast(self) -> bool:
        if self.count > 0:
            delete_node = self.last.prev
            self.last.prev = delete_node.prev
            delete_node.prev.next = self.last
            self.count -= 1
            return True
        return False

    def getFront(self) -> int:
        if self.count != 0:
            return self.front.next.val
        return -1

    def getRear(self) -> int:
        if self.count != 0:
            return self.last.prev.val
        return -1

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.k
