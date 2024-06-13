# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:

        result = []

        total = 0

        curr = head
        while curr:
            total+=1
            curr = curr.next
        
        size = total // k
        extra = total % k
        curr = head

        for i in range(k):

            length = size + (1 if i< extra else 0)
            curr_head = curr
            for _ in range(length-1):
                curr = curr.next
            
            if curr:
                temp = curr.next
                curr.next = None
                curr = temp
            
            result.append(curr_head)
    
        return result



