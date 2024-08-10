# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head


        def mergesort(node):

            if not node or not node.next:
                return node

            mid = getmid(node)
            l = node
            r = mid.next
            mid.next = None
            left = mergesort(l)
            right = mergesort(r) 
            return merge(left,right)
        
        def getmid(node):

            slow = node
            fast = node.next

            while fast and fast.next:

                fast = fast.next.next
                slow = slow.next
            
            return slow
        
        def merge(l1,l2):
            
            dummy = ListNode()
            tail = dummy
            while l1 and l2:

                if l1.val < l2.val:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next
                tail = tail.next
            
            if l1:
                tail.next = l1
            else:
                tail.next = l2
            
            return dummy.next

        
        return mergesort(head)



