# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # rev = None
        # curr = head

        # if not head or not head.next:
        #     return head

        # while curr.next:
        #     rev , rev.next, curr = curr, rev, curr.next
        
        # curr.next = rev
        # return curr

        prev = forw = None
        curr = head

        while curr:
            forw = curr.next
            curr.next = prev
            prev = curr
            curr = forw
        
        return prev
