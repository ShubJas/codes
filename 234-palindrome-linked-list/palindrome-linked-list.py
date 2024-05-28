# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        def reverse(node):
            prev = None
            curr =node
            while curr:
                forw = curr.next
                curr.next = prev
                prev = curr
                curr = forw
            return prev
        
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        slow = reverse(slow)

        while head and slow:
            if head.val != slow.val:
                return False
            head = head.next
            slow = slow.next
        
        return True
        