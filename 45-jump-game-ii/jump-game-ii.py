# Greedy
# jump reach in ranges
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)  # Total number of elements in the array
        jumps = 0  # This will store the number of jumps needed to reach the end
        l = r = 0  # `l` is the left bound, and `r` is the right bound of the range that we can jump to in the current step
        
        # We run the loop as long as the right bound hasn't reached or passed the last index
        while r < n - 1:
            jumps += 1  # We need to make a jump
            farthest = 0  # Track the farthest position we can reach with the next jump
            
            # We iterate over the range of indices from `l` to `r` (the current jump range)
            for i in range(l, r + 1):
                # For each index `i`, calculate how far we can jump from `i`
                # `i + nums[i]` gives the farthest position we can reach from `i`
                farthest = max(farthest, i + nums[i])
            
            # If the farthest we can reach from the current jump is beyond or exactly at the last index,
            # return the number of jumps, because we can reach the end with this jump.
            if farthest >= n - 1:
                return jumps 
            
            # Move the left and right bounds of the current range for the next jump:
            # `l = r + 1` moves the left bound to the next range after the current range
            # `r = farthest` updates the right bound to the farthest position we can reach from this range
            l = r + 1
            r = farthest
        
        return 0  # We should never reach this point as the problem guarantees we can always reach the end.


            









# # #  Dp solution
# class Solution:
#     def jump(self, nums: List[int]) -> int:
        
#         n = len(nums)
#         dp = [float('inf')] * n
#         dp[n-1] = 0

#         for i in range(n-2,-1,-1):
#             for j in range(i + 1,min(i+nums[i]+1,n)):
#                 dp[i]  = min(dp[i] ,1 + dp[j])
        
#         return dp[0]
    
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