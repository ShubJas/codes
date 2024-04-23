class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:


        def feasible(speed) -> bool:
            hours = 0
            for p in piles:
                hours+= (p-1)//speed + 1
            if hours > h:
                 return False
            return True

        l= 1
        r = max(piles)

        while( l < r):
            m = (l+r)//2

            if(feasible(m)):
                r = m
            else:
                l = m + 1
        return l
        