# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        

        hashmap = defaultdict(ListNode)
        dummy = ListNode(0,head)
        psum = 0
        curr = dummy

        while curr:
            psum += curr.val
            if psum in hashmap:
                temp = hashmap[psum].next
                temppsum = psum
                while temp != curr:
                    temppsum += temp.val
                    if temppsum in hashmap:
                        del hashmap[temppsum]
                    temp = temp.next
                hashmap[psum].next = curr.next
            else:
                hashmap[psum] = curr
            curr = curr.next
        
        return dummy.next
