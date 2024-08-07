# Kadane's Algorithm
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)

        curr_max = 0
        maxi = -float('inf')


        for n in nums:
            #           reset , continue
            curr_max = max(n,n+curr_max)
            maxi = max(curr_max,maxi)
        
        return maxi

# DP
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         n = len(nums)
#         prev = [None] * 2 


#         prev[True] = 0
#         prev[False] = -float('inf')


#         for i in range(1,n+1):
#             curr = [None] * 2 
#             for must_take in [True,False]:

#                 # Consider taking the current element
#                 pick = nums[i-1] + prev[True]

#                 # Consider not taking the current element
#                 if must_take:
#                     npick = 0  # If we must take, then npick is 0
#                 else:
#                     npick = prev[False]

#                 curr[must_take] = max(pick, npick)
#             prev = curr

#         return prev[False]


#  i -> n-1 to 0
#  0 base case
#  n to 1
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         n = len(nums)
#         dp = [[None] * 2 for _ in range(n+1)]


#         dp[0][True] = 0
#         dp[0][False] = -float('inf')


#         for i in range(1,n+1):

#             for must_take in [True,False]:

#                 # Consider taking the current element
#                 pick = nums[i-1] + dp[i - 1][True]

#                 # Consider not taking the current element
#                 if must_take:
#                     npick = 0  # If we must take, then npick is 0
#                 else:
#                     npick = dp[i - 1][False]

#                 dp[i][must_take] = max(pick, npick)

#         return dp[n][False]

# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         n = len(nums)
#         dp = [[None] * 2 for _ in range(n)]

#         def calc(i, must_take):
#             if i < 0:
#                 return 0 if must_take else -float('inf')

#             if dp[i][must_take] is not None:
#                 return dp[i][must_take]

#             # Consider taking the current element
#             pick = nums[i] + calc(i - 1, True)

#             # Consider not taking the current element
#             if must_take:
#                 npick = 0  # If we must take, then npick is 0
#             else:
#                 npick = calc(i - 1, False)

#             dp[i][must_take] = max(pick, npick)
#             return dp[i][must_take]

#         return calc(n - 1, False)


# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:

#         n = len(nums)


#         def calc(i,must_take):


#             if i<0:
#                 return 0


#             pick = nums[i] + calc(i-1,True)
#             if must_take:
#                 npick = 0
#             else:
#                 npick = calc(i-1,False)
            

#             return max(pick,npick)
        
#         return calc(n-1,False)            

# Brute
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:

#         n = len(nums)
#         maxsum = -float('inf')
#         for i in range(n):
#             curr_sum = 0
#             for j in range(i,n):
#                 curr_sum += nums[j]
#                 maxsum = max(maxsum,curr_sum)
        
#         return maxsum

        