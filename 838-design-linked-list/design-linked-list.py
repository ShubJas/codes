class ListNode:
    def __init__(self,value=0,next=None):
        self.val =value
        self.next=next


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

        new_node = ListNode(val,self.head)
        self.head = new_node
        

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
            self.addAtHead(val)
            return
        
        curr  =self.head
        while curr and index-1:
            curr  = curr.next
            index-=1
        if curr:
            new_node = ListNode(val,curr.next)
            curr.next = new_node

    def deleteAtIndex(self, index: int) -> None:
        
        if index==0 and self.head:
            self.head = self.head.next
            return
        
        curr = self.head
        while curr and index-1:
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

# class ListNode:
#     def __init__(self, value=0,next=None):
#         self.val = value
#         self.next = next

# class MyLinkedList:

#     def __init__(self):
#         self.head = None
        

        

#     def get(self, index: int) -> int:
        
#         cur = self.head
#         while cur and index:
#             cur = cur.next
#             index-=1

        
#         return cur.val if cur else -1


        

#     def addAtHead(self, val: int) -> None:
        
#         new = ListNode(val,self.head)
#         self.head = new

        
        

        

#     def addAtTail(self, val: int) -> None:
#         if not self.head:
#             self.head = ListNode(val)
#             return
#         cur = self.head
#         while cur.next:
#             cur = cur.next
#         cur.next = ListNode(val)
        

#     def addAtIndex(self, index: int, val: int) -> None:
#         if index==0:
#             self.addAtHead(val)
#         cur = self.head
#         while cur and index-1:
#             cur = cur.next
#             index-=1
#         if cur:
#             new = ListNode(val)
#             new.next = cur.next
#             cur.next= new




        

#     def deleteAtIndex(self, index: int) -> None:
#         if index == 0 and self.head:
#             self.head=self.head.next
#         cur = self.head
#         while cur and index-1:
#             cur = cur.next
#             index-=1
#         if cur and cur.next:
#             cur.next = cur.next.next
        


# # Your MyLinkedList object will be instantiated and called as such:
# # obj = MyLinkedList()
# # param_1 = obj.get(index)
# # obj.addAtHead(val)
# # obj.addAtTail(val)
# # obj.addAtIndex(index,val)
# # obj.deleteAtIndex(index)


# class MyLinkedList:

#     def __init__(self):
#         self.linkedList=[]
#         self.length=0
#     def get(self, index: int) -> int:
#         if(0<=index<self.length):
#             return self.linkedList[index]
#         return -1
#     def addAtHead(self, val: int) -> None:
#         self.linkedList.insert(0,val)
#         self.length+=1

#     def addAtTail(self, val: int) -> None:
#         self.linkedList.append(val)
#         self.length+=1

#     def addAtIndex(self, index: int, val: int) -> None:
#         if(0<=index<=self.length):
#             self.linkedList.insert(index,val)
#             self.length+=1

#     def deleteAtIndex(self, index: int) -> None:
#         if(0<=index<self.length):
#             self.linkedList.pop(index)
#             self.length-=1


# # Your MyLinkedList object will be instantiated and called as such:
# # obj = MyLinkedList()
# # param_1 = obj.get(index)
# # obj.addAtHead(val)
# # obj.addAtTail(val)
# # obj.addAtIndex(index,val)
# # obj.deleteAtIndex(index)