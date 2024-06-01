# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)

        prev = head
        curr = head.next
        while curr:
            if curr.val >=prev.val:
                prev = curr
                curr = curr.next
                continue
            
            pos = dummy

            while pos.next.val  < curr.val:
                pos = pos.next
            
            prev.next = curr.next
            curr.next = pos.next
            pos.next = curr
            curr = prev.next
        
        return dummy.next

        