class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
            
        if len(bloomDay)< m*k:
            return -1

        def feasible(days) -> bool:
            
            bouquets = 0
            flowers = 0
            for bloom in bloomDay:
                if bloom <= days:
                    flowers += 1
                    if flowers == k:
                        bouquets +=1
                        flowers = 0
                else:
                    flowers = 0
            return bouquets >= m

                    
        
        l = min(bloomDay)
        r = max(bloomDay)

        while(l<r):
            #dont use same var name
            mid = (l+r)//2
            if(feasible(mid)):
                r = mid
            else:
                l = mid +1

        return l