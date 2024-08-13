# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# If psum exists in the hashmap, it means that the sublist between the node stored in hashmap[psum] and the current node has a sum of zero.
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:

        hashmap = defaultdict(ListNode)
        dummy = ListNode(0,head)
        curr = dummy    
        psum = 0
        while curr:
            psum += curr.val
            if psum in hashmap:
                node = hashmap[psum].next
                temp_sum = psum
                while node != curr:
                    temp_sum += node.val
                    if temp_sum in hashmap:
                        del hashmap[temp_sum] 
                    node = node.next
                hashmap[psum].next = curr.next
            else:
                hashmap[psum] = curr
            curr = curr.next
        
        return dummy.next

        
            
            



        