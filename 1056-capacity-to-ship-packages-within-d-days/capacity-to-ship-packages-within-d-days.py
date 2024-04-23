class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def feasible(cap) -> bool:
            total = 0
            D = 1
            for weight in weights:
                total += weight
                if total > cap:
                    total = weight
                    D += 1
                    if D > days:
                        return False
            return True



        l = max(weights)
        r = sum(weights)

        while(l< r):
            m = (l+r)//2

            if feasible(m):
                r = m
            else:
                l = m + 1
        return l
        