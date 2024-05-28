# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        fast = slow = head
        rev =None

        while fast and fast.next:
            fast = fast.next.next
            rev , rev.next , slow = slow , rev  ,slow.next

        #  For odd number skip mid
        if fast:
            slow = slow.next

        
        while rev and slow:
            if rev.val != slow.val:
                return False
            rev = rev.next
            slow = slow.next
        
        return True



        # def reverse(node):
        #     prev = None
        #     curr =node
        #     while curr:
        #         forw = curr.next
        #         curr.next = prev
        #         prev = curr
        #         curr = forw
        #     return prev
        
        # fast = head
        # slow = head
        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        
        # slow = reverse(slow)

        # while head and slow:
        #     if head.val != slow.val:
        #         return False
        #     head = head.next
        #     slow = slow.next
        
        # return True
        