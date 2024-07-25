class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        S = sum(nums)
        if S % 2 != 0:  # if odd
            return False

        n = len(nums)
        reach = S // 2

        # Initialize a single array for the dp
        dp = [False] * (reach + 1)
        dp[0] = True  # Base case: A subset sum of 0 is always possible

        for num in nums:
            # Iterate backwards to prevent overwriting values we still need to use
            for target in range(reach, num - 1, -1):
                dp[target] = dp[target] or dp[target - num]

        return dp[reach]

# class Solution:
#     def canPartition(self, nums: List[int]) -> bool:

#         S = sum(nums)
#         if S % 2 != 0:
#             return False

#         n = len(nums)
#         reach =  S//2

#         dp = [[None] * (reach+1) for _ in range(n)]


#         for i in range(n):
#             dp[i][0] = True
        
#         if nums[0] <= reach:
#             dp[0][nums[0]] = True


#         for i in range(1,n):

#             for target in range(1,reach+1):

#                 pick = False
#                 if nums[i] <= target:
#                     pick = dp[i-1][target-nums[i]]
                
#                 not_pick  = dp[i-1][target]

#                 dp[i][target] = pick or not_pick

#         return dp[n-1][reach]

# class Solution:
#     def canPartition(self, nums: List[int]) -> bool:

#         S = sum(nums)
#         if S % 2 != 0:
#             return False

#         n = len(nums)
#         reach =  S//2

#         dp = [[None] * (reach+1) for _ in range(n)]
        
#         def calc(i,target):


#             if target == 0:
#                 return True
            
#             if i == 0:
#                 return target == nums[0]
            
#             if dp[i][target] is not None:
#                 return dp[i][target]
            
#             pick = False
#             if nums[i] <= target:
#                 pick = calc(i-1,target-nums[i])
            
#             not_pick  = calc(i-1,target)

#             dp[i][target] = pick or not_pick
#             return dp[i][target]
        
#         return calc(n-1,reach)

# # Intuition -  S1 + S2 = S , S1 = S2 , SO S1 = S2 = S/2
# # find any subset = S/2
# class Solution:
#     def canPartition(self, nums: List[int]) -> bool:

#         S = sum(nums)
#         if S % 2 != 0:
#             return False

#         n = len(nums)
#         reach =  S//2


#         def calc(i,target):


#             if target == 0:
#                 return True
            
#             if i == 0:
#                 return target == nums[0]
            
#             pick = False
#             if nums[i] <= target:
#                 pick = calc(i-1,target-nums[i])
            
#             not_pick  = calc(i-1,target)


#             return pick or not_pick
        
#         return calc(n-1,reach)
