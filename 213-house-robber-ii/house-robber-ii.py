class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        This function calculates the maximum amount of money that can be robbed from a circular row of houses,
        where robbing two adjacent houses is not allowed.

        Approach:
        - Use dynamic programming to calculate the maximum money that can be robbed.
        - Split the problem into two subproblems:
          1. Calculate the maximum amount by excluding the last house.
          2. Calculate the maximum amount by excluding the first house.
        - The final result will be the maximum of these two subproblems.

        Args:
        - nums: A list of integers representing the amount of money in each house.

        Returns:
        - The maximum amount of money that can be robbed without alerting the police.
        """
        n = len(nums)

        # Base case: If there are no houses, return 0.
        if n == 0:
            return 0
        # Base case: If there is only one house, return the amount of money in that house.
        if n == 1:
            return nums[0]

        # Helper function to calculate the maximum money that can be robbed from range start to end-1.
        def calc(start, end):
            if end - start <= 1:
                return nums[start]
            dp = [-1] * n
            dp[start] = nums[start]
            dp[start + 1] = max(nums[start], nums[start + 1])
            for i in range(start + 2, end):
                pick = nums[i] + dp[i - 2]
                not_pick = dp[i - 1]
                dp[i] = max(pick, not_pick)
            return dp[end - 1]

        # Calculate the maximum amount excluding the last house.
        max1 = calc(0, n - 1)
        # Calculate the maximum amount excluding the first house.
        max2 = calc(1, n)

        # Return the maximum of the two results.
        return max(max1, max2)


# class Solution:
#     def rob(self, nums: List[int]) -> int:

        
#         n = len(nums)

#         if n == 0:
#             return 0
#         if n == 1:
#             return nums[0]

#         dp1 = [-1] * (n+1)
#         dp2 = [-1] * (n)

#         def calc(i,end,dp):

#             if i < end:
#                 return 0

#             if dp[i] != -1:
#                 return dp[i]
            
#             pick = nums[i] + calc(i-2,end,dp)
#             not_pick = calc(i-1,end,dp)

#             dp[i] = max(pick,not_pick)
#             return dp[i]



#         max1 = calc(n-2,0,dp1)
#         max2 = calc(n-1,1,dp2)

#         return max(max1,max2)


# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         """
#         This function calculates the maximum amount of money that can be robbed from a circular row of houses,
#         where robbing two adjacent houses is not allowed.

#         Approach:
#         - Use a recursive approach without memoization.
#         - Split the problem into two subproblems:
#           1. Calculate the maximum amount by excluding the last house.
#           2. Calculate the maximum amount by excluding the first house.
#         - The final result will be the maximum of these two subproblems.

#         Args:
#         - nums: A list of integers representing the amount of money in each house.

#         Returns:
#         - The maximum amount of money that can be robbed without alerting the police.
#         """

#         n = len(nums)

#         # Base case: If there are no houses, return 0.
#         if n == 0:
#             return 0

#         # Base case: If there is only one house, return the amount of money in that house.
#         if n == 1:
#             return nums[0]

#         def calc(i, end):
#             """
#             Recursive function to calculate the maximum amount of money that can be robbed 
#             from the current house `i` to the end house `end`.

#             Args:
#             - i: Current house index.
#             - end: The end house index for the current calculation.

#             Returns:
#             - The maximum amount of money that can be robbed from house `i` to house `end`.
#             """

#             # Base case: If the current house index is less than the end index, return 0.
#             # This means that there are no more houses to rob in this range.
#             if i < end:
#                 return 0
            
#             # Calculate the maximum amount by:
#             # 1. Robbing the current house and adding its value to the maximum amount from the house two steps back.
#             pick = nums[i] + calc(i - 2, end)
            
#             # 2. Not robbing the current house and taking the maximum amount from the next house.
#             not_pick = calc(i - 1, end)

#             # Return the maximum amount between picking and not picking the current house.
#             return max(pick, not_pick)

#         # Calculate the maximum amount excluding the last house.
#         max1 = calc(n - 2, 0)

#         # Calculate the maximum amount excluding the first house.
#         max2 = calc(n - 1, 1)

#         # Return the maximum of the two results.
#         return max(max1, max2)

        