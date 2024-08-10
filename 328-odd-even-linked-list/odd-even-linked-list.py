# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        

        if not head or not head.next:
            return head
        dummy = ListNode(0,head)
        even = evenhead = head.next
        odd = head

        while even and even.next:

            odd.next  = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        
        odd.next = evenhead

        return dummy.next