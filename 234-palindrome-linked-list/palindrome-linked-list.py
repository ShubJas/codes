# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:


        fast = head
        slow = head
    
        rev = None
        while fast and fast.next:
            fast = fast.next.next
            rev , rev.next, slow = slow , rev , slow.next
        
        if fast:
            slow = slow.next
        

        


        while rev and slow:
            if rev.val != slow.val:
                return False
            rev= rev.next
            slow= slow.next
        
        return True
