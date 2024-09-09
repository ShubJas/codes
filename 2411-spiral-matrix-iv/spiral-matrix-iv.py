# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        
        result = [[-1] * n for _ in range(m)]

        t = l = 0
        r , b = n - 1 , m - 1 


        while head:

            for j in range(l,r+1):
                if not head:
                    return result
                result[t][j] = head.val
                head = head.next
            t+=1

            for i in range(t,b+1):
                if not head:
                    return result
                result[i][r] = head.val
                head = head.next
            r-=1

            for j in range(r,l-1,-1):
                if not head:
                    return result
                result[b][j] = head.val
                head = head.next
            b-=1

            for i in range(b,t-1,-1):
                if not head:
                    return result
                result[i][l] = head.val
                head = head.next
            l+=1

        return result

