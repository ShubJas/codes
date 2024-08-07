class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        if len(bloomDay) < m*k:
            return -1

        def feasible(day):

            flowers = 0
            bouquets = 0
            for bday in bloomDay:
                if bday <= day:
                    flowers+=1
                    if flowers == k:
                        bouquets +=1
                        flowers = 0 
                else:
                    flowers = 0
                
            
            return bouquets >= m




        l = min(bloomDay)
        r = max(bloomDay)


        while l<r:

            mid = (l+r)//2
            
            if feasible(mid):
                r = mid
            else:
                l = mid+1
        
        return l
        