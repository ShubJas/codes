class ListNode:
    def __init__(self, value=0,next=None):
        self.val = value
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None
        

        

    def get(self, index: int) -> int:
        
        cur = self.head
        while cur and index:
            cur = cur.next
            index-=1

        
        return cur.val if cur else -1


        

    def addAtHead(self, val: int) -> None:
        
        new = ListNode(val,self.head)
        self.head = new

        
        

        

    def addAtTail(self, val: int) -> None:
        if not self.head:
            self.head = ListNode(val)
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = ListNode(val)
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index==0:
            self.addAtHead(val)
        cur = self.head
        while cur and index-1:
            cur = cur.next
            index-=1
        if cur:
            new = ListNode(val)
            new.next = cur.next
            cur.next= new




        

    def deleteAtIndex(self, index: int) -> None:
        if index == 0 and self.head:
            self.head=self.head.next
        cur = self.head
        while cur and index-1:
            cur = cur.next
            index-=1
        if cur and cur.next:
            cur.next = cur.next.next
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)