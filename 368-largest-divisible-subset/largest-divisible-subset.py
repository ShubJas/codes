class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:


        n = len(nums)
        nums.sort() # convert to already increasing subseq
        
        backtrack =  [-1] * n

        dp = [1] * n
        for i in range(1,n):

            for prev_i in range(i):


                if nums[i] % nums[prev_i] == 0 and (dp[prev_i]+1) > dp[i]:
                    dp[i] = dp[prev_i] + 1
                    backtrack[i] = prev_i
        
        start_index = max(range(n),key = lambda i: dp[i])

        result = []
        
        while start_index != -1:
            result.append(nums[start_index])
            start_index = backtrack[start_index]
        
        return result




