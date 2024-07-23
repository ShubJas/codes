class Solution:
    def rob(self, nums: List[int]) -> int:

        
        n = len(nums)

        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        dp1 = [-1] * (n+1)
        dp2 = [-1] * (n)

        def calc(i,end,dp):

            if i < end:
                return 0

            if dp[i] != -1:
                return dp[i]
            
            pick = nums[i] + calc(i-2,end,dp)
            not_pick = calc(i-1,end,dp)

            dp[i] = max(pick,not_pick)
            return dp[i]



        max1 = calc(n-2,0,dp1)
        max2 = calc(n-1,1,dp2)

        return max(max1,max2)



        