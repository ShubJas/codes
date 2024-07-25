# Intuition -  S1 + S2 = S , S1 = S2 , SO S1 = S2 = S/2
# find any subset = S/2
class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        S = sum(nums)
        if S % 2 != 0:
            return False

        n = len(nums)
        reach =  S//2

        dp = [[None] * (reach+1) for _ in range(n)]
        
        def calc(i,target):


            if target == 0:
                return True
            
            if i == 0:
                return target == nums[0]
            
            if dp[i][target] is not None:
                return dp[i][target]
            
            pick = False
            if nums[i] <= target:
                pick = calc(i-1,target-nums[i])
            
            not_pick  = calc(i-1,target)

            dp[i][target] = pick or not_pick
            return dp[i][target]
        
        return calc(n-1,reach)


# # Intuition -  S1 + S2 = S , S1 = S2 , SO S1 = S2 = S/2
# # find any subset = S/2
# class Solution:
#     def canPartition(self, nums: List[int]) -> bool:

#         reach = sum(nums)/2

#         if int(reach) != reach:
#             return False

        
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
        
#         return calc(len(nums)-1,reach)
