# Greedy approach
class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:

        n = len(nums)
        score = 0
        i = 0
        while i < n - 1:
            j = i + 1
            while j < n - 1 and nums[i] > nums[j]:
                j+=1
            score += (j - i) * nums[i]
            # print(i,j)
            i = j
        
        return score








# #  Dp solution dosent work see constraints ( 10^5)
# class Solution:
#     def findMaximumScore(self, nums: List[int]) -> int:
        
#         n = len(nums)
#         dp = [0]* (n+1)


#         for i in range(n-1,-1,-1):
#             for j in range(i+1,n):
#                 dp[i] = max(nums[i] * (j-i) + dp[j],dp[i])

#         return dp[0] 


# class Solution:
#     def findMaximumScore(self, nums: List[int]) -> int:
        
#         n = len(nums)
#         dp = [-1]* n

#         def calc(i):

#             if i >= n:
#                 return 0
            
#             if dp[i] != -1:
#                 return dp[i]

#             score = 0
#             for j in range(i+1,n):
#                 score = max(nums[i] * (j-i) + calc(j),score)
            
#             dp[i] = score
#             return dp[i]

#         return calc(0)

# class Solution:
#     def findMaximumScore(self, nums: List[int]) -> int:
        
#         n = len(nums)
        

#         def calc(i):

#             if i >= n:
#                 return 0

#             score = 0
#             for j in range(i+1,n):
#                 score = max(nums[i] * (j-i) + calc(j),score)
            
#             return score

#         return calc(0)
