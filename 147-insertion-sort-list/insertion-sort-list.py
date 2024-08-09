# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        



        dummy = ListNode()
        dummy.next = head

        prev= head
        curr = head.next


        while curr:

            if prev.val <= curr.val:
                prev = prev.next
                curr = curr.next
                continue
            
            start = dummy


            while start.next.val < curr.val:
                start = start.next
            

            prev.next = curr.next
            curr.next = start.next
            start.next = curr
            curr = prev.next
        
        return dummy.next