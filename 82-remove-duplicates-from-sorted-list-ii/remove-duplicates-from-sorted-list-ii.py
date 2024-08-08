# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        

        dummy = ListNode()
        dummy.next = head
        grpprev = dummy
        curr = head
        while curr:
            if curr.next and curr.val == curr.next.val:
                
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next

                grpprev.next = curr.next
            else:
                grpprev = grpprev.next
            
            curr = curr.next

        return  dummy.next


