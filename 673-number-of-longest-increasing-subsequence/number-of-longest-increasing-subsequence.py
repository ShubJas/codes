class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:

        n = len(nums)

        dp = [1] * n
        count = [1] * n

        for i in range(1,n):

            for prev_i in range(i):

                if nums[prev_i] < nums[i] :
                    if dp[i] < dp[prev_i] + 1:
                        dp[i] = dp[prev_i] + 1
                        count[i] = count[prev_i]
                    elif  dp[i] == dp[prev_i] + 1:
                        count[i] += count[prev_i]
        

        ans = 0
        max_val = max(dp)
        for i in range(n):
            if dp[i] == max_val:
                ans += count[i]
        return ans
        