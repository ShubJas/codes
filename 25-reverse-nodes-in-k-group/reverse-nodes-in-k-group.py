# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getkth(self,node,k):

        while node and k:
            node = node.next
            k -=1
        return node


    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode(0,head)

        grpprev = dummy


        while True:
            kth = self.getkth(grpprev,k)
            if not kth:
                break
            
            grpnext = kth.next

            prev = kth.next
            curr = grpprev.next

            while curr != grpnext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            # reconnect in order
            
            temp = grpprev.next
            grpprev.next = kth
            grpprev = temp
            
        return dummy.next



        
        