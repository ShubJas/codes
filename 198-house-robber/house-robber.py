class Solution:
    def rob(self, nums: List[int]) -> int:


        n = len(nums)

        if n==0:
            return 0
        elif n == 1:
            return nums[0]

        p2 = nums[0]
        p1 = max(nums[0],nums[1])

        for i in range(2,n):
            pick = nums[i] + p2
            not_pick = p1
            
            curr = max(pick,not_pick)

            p2 = p1
            p1 = curr
        
        return p1



# class Solution:
#     def rob(self, nums: List[int]) -> int:


#         n = len(nums)

#         if n==0:
#             return 0
#         elif n == 1:
#             return nums[0]

#         dp = [-1] * (n + 1)
#         dp[0] = nums[0]
#         dp[1] = max(nums[0],nums[1])

#         for i in range(2,n):
#             pick = nums[i] + dp[i-2]
#             not_pick = dp[i-1]
            
#             dp[i] = max(pick,not_pick)
        
#         return dp[n-1]
    
# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         n = len(nums)
#         # Base case: if there's no house, the maximum amount is 0.
#         if n == 0:
#             return 0
#         # Base case: if there's only one house, rob that house.
#         elif n == 1:
#             return nums[0]
#         # Base case: if there are two houses, rob the one with more money.
#         elif n == 2:
#             return max(nums)
        

#         dp =[-1] * (n+1)

#         def calc(i):

#             if dp[i] != -1:
#                 return dp[i]

#             if i == 0:
#                 return nums[0]
            
#             if i == 1:
#                 return max(nums[0],nums[1])

        
#             pick = nums[i] + calc(i-2)
#             not_pick = calc(i-1)
            

#             dp[i] = max(pick,not_pick)
#             return dp[i]
        
#         return calc(n-1)


# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         """
#         This function calculates the maximum amount of money that can be robbed from a line of houses,
#         where robbing two adjacent houses is not allowed.

#         Approach:
#         - Use a recursive function to calculate the maximum amount that can be robbed up to the i-th house.
#         - For each house, decide whether to rob it or not based on the maximum amount that can be obtained.
#         - Use base cases for 0, 1, and 2 houses to simplify the recursion.

#         Args:
#         - nums: A list of integers representing the amount of money in each house.

#         Returns:
#         - The maximum amount of money that can be robbed without alerting the police.
#         """

#         n = len(nums)
        
#         # Base case: if there's no house, the maximum amount is 0.
#         if n == 0:
#             return 0
#         # Base case: if there's only one house, rob that house.
#         elif n == 1:
#             return nums[0]
#         # Base case: if there are two houses, rob the one with more money.
#         elif n == 2:
#             return max(nums)
        
#         def calc(i):
#             """
#             This recursive function calculates the maximum amount that can be robbed up to the i-th house.

#             Args:
#             - i: The index of the current house.

#             Returns:
#             - The maximum amount that can be robbed up to the i-th house.
#             """
#             # Base case: If the current house index is 0, return the amount in the first house.
#             if i == 0:
#                 return nums[0]
            
#             # Base case: If the current house index is 1, return the maximum amount between the first and second house.
#             if i == 1:
#                 return max(nums[0], nums[1])
        
#             # If robbing the current house, add its value to the maximum amount from two houses before.
#             pick = nums[i] + calc(i-2)
#             # If not robbing the current house, take the maximum amount from the previous house.
#             not_pick = calc(i-1)
            
#             # Return the maximum of robbing and not robbing the current house.
#             return max(pick, not_pick)
        
#         # Start the recursion from the last house.
#         return calc(n-1)

