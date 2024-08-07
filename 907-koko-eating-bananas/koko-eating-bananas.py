class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:


        def feasible(eat_rate):
            hours = 0         
            for bananas in piles:

                hours += ((bananas-1) // eat_rate ) + 1
                if hours > h:
                    return False
            
            return True

        


        l = 1
        r = max(piles)

        while l<r:
            m  =(l+r)//2
            if feasible(m):
                r = m
            else:
                l = m + 1
        
        return l