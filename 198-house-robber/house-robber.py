class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        # Base case: if there's no house, the maximum amount is 0.
        if n == 0:
            return 0
        # Base case: if there's only one house, rob that house.
        elif n == 1:
            return nums[0]
        # Base case: if there are two houses, rob the one with more money.
        elif n == 2:
            return max(nums)
        

        dp =[-1] * (n+1)

        def calc(i):

            if dp[i] != -1:
                return dp[i]

            if i == 0:
                return nums[0]
            
            if i == 1:
                return max(nums[0],nums[1])

        
            pick = nums[i] + calc(i-2)
            not_pick = calc(i-1)
            

            dp[i] = max(pick,not_pick)
            return dp[i]
        
        return calc(n-1)

