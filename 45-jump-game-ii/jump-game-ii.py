class Solution:
    def jump(self, nums: List[int]) -> int:
        
        n = len(nums)
        dp = [float('inf')] * n
        dp[n-1] = 0

        for i in range(n-2,-1,-1):
            for j in range(i + 1,min(i+nums[i]+1,n)):
                dp[i]  = min(dp[i] ,1 + dp[j])
        
        return dp[0]
    
# class Solution:
#     def jump(self, nums: List[int]) -> int:
        
#         n = len(nums)
#         dp = [-1] * n
#         def calc(i):

#             if i >= n-1:
#                 return 0
            
#             if dp[i] != -1:
#                 return dp[i]
            
#             mini = float('inf')
#             for j in range(i + 1,min(i+nums[i]+1,n)):
#                 mini = min(mini,1 + calc(j))
                
#             dp[i] = mini

#             return dp[i]
        

#         return calc(0)


# class Solution:
#     def jump(self, nums: List[int]) -> int:
        
#         n = len(nums)
#         def calc(i):

#             if i >= n-1:
#                 return 0
            
#             mini = float('inf')
#             for j in range(i + 1,min(i+nums[i]+1,n)):
#                 mini = min(mini,1 + calc(j))
            
#             return mini
        

#         return calc(0)