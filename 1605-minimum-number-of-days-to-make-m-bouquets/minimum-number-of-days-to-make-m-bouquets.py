class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        def feasible(days) -> bool:
            
            flowers = 0
            bouquets = 0
            for bloom in bloomDay:
                if bloom > days:
                    flowers = 0
                else:
                    bouquets+= (flowers + 1)// k 
                    flowers=(flowers+ 1) % k

            return bouquets >= m
    
        if len(bloomDay)< m*k:
            return -1
                    
        
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