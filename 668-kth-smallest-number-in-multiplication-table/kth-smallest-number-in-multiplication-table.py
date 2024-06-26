class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:


        def issmallerthan(num) -> bool:
            
            count = 0
            for div in range(1,m+1):
                if num//div > n:
                    count += n
                else:
                    count+= num//div
                # count += min( num//div , n)
                if count ==0:
                    break

            return count >= k



        l = 1
        r = m * n

        while l< r:
            mid = (l + r)//2

            if issmallerthan(mid):
                r = mid
            else:
                l = mid + 1
        
        return l
        