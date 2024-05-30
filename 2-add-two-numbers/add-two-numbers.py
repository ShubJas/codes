# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        i= j = n1= n2 = 0
        while l1:
            n1 += l1.val * (10**i)
            i+=1
            l1= l1.next

        while l2:
            n2 += l2.val * (10**j)
            j+=1
            l2= l2.next
        
        total = n1 + n2

        if total == 0:
            return ListNode(0)
        dummy = ListNode(0)
        tail = dummy

        while total > 0:
            last = total % 10
            total //= 10
            tail.next = ListNode(last)
            tail = tail.next
        
        return dummy.next





        