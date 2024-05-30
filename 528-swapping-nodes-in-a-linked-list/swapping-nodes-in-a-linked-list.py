# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 0
        # val = 0
        curr = head
        while curr:
            count+=1
            if count ==k:
                val1 = curr.val
            curr = curr.next
        curr = head
        for _ in range(1,count-k+1):
            curr = curr.next
        val2 = curr.val
        curr.val = val1
        curr = head
        for _ in range(k-1):
            curr = curr.next
        curr.val  =val2
        return head
        




        