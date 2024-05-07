class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        
        l = 0

        pairs = result = count =  0
        hashset = defaultdict(int)
        for r in range(len(nums)):
            
            count += hashset[nums[r]]
            hashset[nums[r]] +=1

            while count>=k:
                result += len(nums) - r
                remove = nums[l]
                hashset[remove] -=1
                count-= hashset[remove]
                l+=1
        
        return result
            
        





        # left = ans = tally = 0
        # n, d = len(nums), defaultdict(int)

        # for right,num in enumerate(nums):    # <-- 1
        #     tally += d[num]
        #     d[num] += 1
            
        #     while tally >= k:                # <-- 2     
        #         ans+= n - right
        #         d[nums[left]] -= 1           # <-- 3
        #         tally -= d[nums[left]]
        #         left += 1
            
        # return ans                           # <-- 4