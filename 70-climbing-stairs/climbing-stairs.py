class Solution:
    def climbStairs(self, n: int) -> int:


        if n<2:
            return 1
        p2 = 1
        p1 = 1


        for i in range(2,n+1):
            curr = p1 + p2
            p2 = p1
            p1 = curr
        
        return p1


        