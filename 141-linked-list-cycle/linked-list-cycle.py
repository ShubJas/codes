class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        if head.next is None:
            return False
        fast = head
        while fast and fast.next: #As fast moves 2 ptrs at a time
            head = head.next
            fast = fast.next.next
            if head is fast:
                return True
        return False