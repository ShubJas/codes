"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        oldtonew ={None:None}

        curr  = head
        while curr:
            oldtonew[curr] = ListNode(curr.val)
            curr = curr.next
        

        curr = head
        while curr:
            oldtonew[curr].next = oldtonew[curr.next]
            oldtonew[curr].random = oldtonew[curr.random]
            curr = curr.next
        
        return oldtonew[head]