class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        zero_count = nums.count(0)

        if zero_count == len(nums):

            if target == 0:
                return pow(2,zero_count)
            else:
                return 0

        nums = [ele for ele in nums if ele != 0]
        n = len(nums)
        S = sum(nums) 

        if (S - target) & 1 or S - target < 0:
            return 0
        reach  = (S- target) // 2
        

        dp = [[0] * (reach+1) for _ in range(n)]


        for i in range(n):
            dp[i][0] = 1

        if nums[0] <= reach:
            dp[0][nums[0]] = 1

        for i in range(1,n):

            for target in range(1,reach+1):

                pick = 0
                if nums[i] <=target:
                    pick = dp[i-1][target-nums[i]]
                
                npick = dp[i-1][target]

                dp[i][target] = pick + npick
        
        count_nonzeros = dp[n-1][reach]

        return count_nonzeros * pow(2,zero_count)

# class Solution:
#     def findTargetSumWays(self, nums: List[int], target: int) -> int:

#         zero_count = nums.count(0)

#         nums = [ele for ele in nums if ele != 0]
#         n = len(nums)
#         S = sum(nums) 

#         if (S - target) & 1 or S - target < 0:
#             return 0
#         reach  = (S- target) // 2
        

#         dp = [[-1] * (reach+1) for _ in range(n)]

#         def calc(i,target):

#             if target == 0:
#                 return 1

#             if i == 0:
#                 if nums[0] == target:
#                     return 1
#                 else:
#                     return 0
            
#             if dp[i][target] != -1:
#                 return dp[i][target]

#             pick = 0
#             if nums[i] <=target:
#                 pick = calc(i-1,target-nums[i])
            
#             npick = calc(i-1,target)

#             dp[i][target] = pick + npick
#             return dp[i][target]
        
#         count_nonzeros = calc(n-1,reach)

#         return count_nonzeros * pow(2,zero_count)

# # Intuition -  S1 - S2 = target , S1 + S2 = S -->  S2 = (S- target) // 2
# class Solution:
#     def findTargetSumWays(self, nums: List[int], target: int) -> int:





#         zero_count = nums.count(0)

#         nums = [ele for ele in nums if ele != 0]
#         n = len(nums)
#         S = sum(nums) 

#         if (S - target) & 1 or S - target < 0:
#             return 0
#         reach  = (S- target) // 2
        
        
#         def calc(i,target):

#             if target == 0:
#                 return 1

#             if i == 0:
#                 if nums[0] == target:
#                     return 1
#                 else:
#                     return 0
            
#             pick = 0
            
#             if nums[i] <=target:
#                 pick = calc(i-1,target-nums[i])
            
#             npick = calc(i-1,target)

#             return pick + npick
        
#         count_nonzeros = calc(n-1,reach)

#         return count_nonzeros * pow(2,zero_count)
            



#  Not good sol(see up)
# class Solution:
#     def findTargetSumWays(self, nums: List[int], target: int) -> int:


#         n = len(nums)
#         S = sum(nums) 
#         def calc(i,target):



#             if i == 0:
#                 if target == 0 and nums[0] == 0:
#                     return 2  # +0 and -0 are two ways
#                 if target == nums[0] or target == -nums[0]:
#                     return 1
#                 return 0
            

#             plus = calc(i-1,target-nums[i])
            
#             minus = calc(i-1,target+nums[i])


#             return plus + minus
        
#         return calc(n-1,target)
            
            

        