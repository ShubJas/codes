class ListNode:
    def __init__(self,val = 0 ,next=None):
        self.val = val
        self.next = next
        
class MyLinkedList:
    def __init__(self):
        self.head = None


    def get(self, index: int) -> int:
        curr = self.head
        while curr and index:
            curr = curr.next
            index-=1
        return curr.val if curr else -1


    def addAtHead(self, val: int) -> None:
        if not self.head:
            self.head = ListNode(val)
            return
        
        self.head = ListNode(val,self.head)


    def addAtTail(self, val: int) -> None:
        if not self.head:
            self.head = ListNode(val)
            return
        
        curr = self.head

        while curr.next:
            curr = curr.next
        
        curr.next = ListNode(val)
        
        

    def addAtIndex(self, index: int, val: int) -> None:

        if index == 0:
            self.head = ListNode(val,self.head)
            return

        curr = self.head

        while curr and index-1 :
            curr = curr.next
            index-=1
        
        if curr:
            temp = curr.next
            curr.next = ListNode(val,temp)



        

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            self.head = self.head.next
            return

        curr = self.head

        while curr and index-1 :
            curr = curr.next
            index-=1
        
        if curr and curr.next:
            curr.next = curr.next.next


        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)