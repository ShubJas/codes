# if we min the abs diff between all then we maximize the overall
class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        n = len(start)

        #  sorting so we can directly compare(adj)
        start.sort()

        #  will check if a new array is psbl with abs diff(in all) = target or less
        def feasible(target):

            nums = start[:]
            for i in range(1,n):
                
                diff = nums[i] - nums[i-1] 
                if diff >= target:
                    continue
                
                extra_needed = target - diff
                if extra_needed > d:
                    return False
                nums[i] += extra_needed
            
            return True
                


        l = 0 
        r = start[-1] + d - start[0]



        while l < r:

            mid = (l + r + 1) // 2


            if feasible(mid):
                l = mid
            else:
                r = mid - 1

        
        return l

        