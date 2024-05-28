# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        ptr1 = headA
        ptr2 = headB

        while ptr1 != ptr2:
            if ptr1:
                ptr1 = ptr1.next
            else:
                ptr1 = headB
            if ptr2:
                ptr2= ptr2.next
            else:
                ptr2 = headA 
        
        return ptr1

        # nodeset =set()

        # while headA:
        #     nodeset.add(headA)
        #     headA = headA.next
        
        # while headB:
        #     if headB in nodeset:
        #         return headB
        #     headB = headB.next
        
        # return None

            