class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        while fast and fast.next: #As fast moves 2 ptrs at a time
            head = head.next
            fast = fast.next.next
            if head is fast:
                return True
        return False