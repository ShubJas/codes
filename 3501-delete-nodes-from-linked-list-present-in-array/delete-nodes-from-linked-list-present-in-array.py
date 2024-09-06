# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        

        nums = set(nums)

        dummy = ListNode(0,head)
        prev = dummy
        curr = head

        if not head:
            return

        
        while curr:
            if curr.val in nums:
                curr = curr.next
                prev.next = curr
            else:
                curr = curr.next
                prev = prev.next
        
        return dummy.next


