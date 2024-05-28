# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head.next:
            return head
        
        fast = head

        while fast and fast.next:
            head = head.next
            fast = fast.next.next
        
        return head
        