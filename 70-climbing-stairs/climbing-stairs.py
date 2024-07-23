class Solution:
    def climbStairs(self, n: int) -> int:
        """
        This function calculates the number of distinct ways to climb a staircase with `n` steps,
        where each time you can either climb 1 step or 2 steps.

        Approach:
        - Use a bottom-up dynamic programming approach with space optimization.
        - Instead of maintaining a full DP array, we only keep track of the last two computed values.
        - The base cases are:
          - If there are 0 or 1 steps, there is exactly 1 way to reach the top.
        - For each step from 2 to n, the number of ways to reach that step is the sum of:
          - The number of ways to reach the previous step (`i-1` steps).
          - The number of ways to reach the step before the previous step (`i-2` steps).
        
        Args:
        - n: The total number of steps in the staircase.

        Returns:
        - The number of distinct ways to reach the top of the staircase.
        """

        # Base case: If there are 0 or 1 steps, there's exactly 1 way to reach the top.
        if n < 2:
            return 1

        # Initialize the variables to keep track of the last two computed values.
        p2 = 1  # This represents dp[i-2] initially
        p1 = 1  # This represents dp[i-1] initially

        # Iterate from step 2 to n and calculate the number of ways to reach each step.
        for i in range(2, n + 1):
            # Current number of ways to reach the i-th step.
            curr = p1 + p2
            # Update p2 to the previous p1 (i-1 step).
            p2 = p1
            # Update p1 to the current number of ways (i-th step).
            p1 = curr

        # Return the number of ways to reach the n-th step.
        return p1

# class Solution:
#     def climbStairs(self, n: int) -> int:
#         """
#         This function calculates the number of distinct ways to climb a staircase with `n` steps,
#         where each time you can either climb 1 step or 2 steps.

#         Approach:
#         - Use a bottom-up dynamic programming approach to build the solution iteratively.
#         - The base cases are:
#           - If there are 0 steps, there is 1 way to stay at the top (do nothing).
#           - If there is 1 step, there is only 1 way to reach the top (take 1 step).
#         - For each step from 2 to n, the number of ways to reach that step is the sum of:
#           - The number of ways to reach the previous step (`i-1` steps).
#           - The number of ways to reach the step before the previous step (`i-2` steps).
#         - Store the number of ways to reach each step in a `dp` array.

#         Args:
#         - n: The total number of steps in the staircase.

#         Returns:
#         - The number of distinct ways to reach the top of the staircase.
#         """

#         # Initialize the memoization array with -1, indicating that the subproblems have not been solved yet.
#         dp = [-1] * (n + 1)

#         # Base case: If there are 0 steps, there's 1 way to stay at the top.
#         dp[0] = 1

#         # Base case: If there is 1 step, there's only 1 way to reach the top.
#         dp[1] = 1

#         # Fill the dp array for each step from 2 to n.
#         for i in range(2, n + 1):
#             # The number of ways to reach the i-th step is the sum of:
#             # - The number of ways to reach the (i-1)-th step.
#             # - The number of ways to reach the (i-2)-th step.
#             dp[i] = dp[i - 1] + dp[i - 2]

#         # Return the number of ways to reach the n-th step.
#         return dp[n]

# class Solution:
#     def climbStairs(self, n: int) -> int:
#         """
#         This function calculates the number of distinct ways to climb a staircase with `n` steps,
#         where each time you can either climb 1 step or 2 steps.

#         Approach:
#         - Use a top-down dynamic programming (memoization) approach to avoid redundant calculations.
#         - The base cases are:
#           - If there are 0 steps remaining, there is 1 way to stay at the top (do nothing).
#           - If there is 1 step remaining, there is only 1 way to reach the top (take 1 step).
#         - For each step, you can either:
#           - Take 1 step and solve the subproblem for `n-1` steps.
#           - Take 2 steps and solve the subproblem for `n-2` steps.
#         - Use a memoization array `dp` to store the results of subproblems.
#         - The result for each step `i` is stored in `dp[i]` to avoid recalculating it.

#         Args:
#         - n: The total number of steps in the staircase.

#         Returns:
#         - The number of distinct ways to reach the top of the staircase.
#         """

#         # Initialize the memoization array with -1, indicating that the subproblems have not been solved yet.
#         dp = [-1] * (n + 1)
        
#         def climb(i: int) -> int:
#             """
#             This is a helper function that calculates the number of ways to climb a staircase
#             with `i` steps remaining using recursion and memoization.

#             Args:
#             - i: The number of steps remaining.

#             Returns:
#             - The number of distinct ways to reach the top from step `i`.
#             """

#             # Base case: If there are 0 steps remaining, there's 1 way to stay at the top.
#             if i == 0:
#                 return 1
            
#             # Base case: If there is 1 step remaining, there's only 1 way to reach the top.
#             if i == 1:
#                 return 1
            
#             # If the result for `i` steps has already been calculated, return the stored result.
#             if dp[i] != -1:
#                 return dp[i]
            
#             # Recursive case: The total ways to reach the top from step `i` is the sum of:
#             # - The ways to reach the top from step `i-1` (taking 1 step).
#             # - The ways to reach the top from step `i-2` (taking 2 steps).
#             dp[i] = climb(i - 1) + climb(i - 2)
            
#             # Return the result for `i` steps.
#             return dp[i]
        
#         # Start the recursion from the given number of steps `n`.
#         return climb(n)


# Normal recursion
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         """
#         This function calculates the number of distinct ways to climb a staircase with `n` steps,
#         where each time you can either climb 1 step or 2 steps.

#         Approach:
#         - Use recursion to explore all possible ways to reach the top.
#         - The base cases are:
#           - If there are 0 steps remaining, there is 1 way to stay at the top (do nothing).
#           - If there is 1 step remaining, there is only 1 way to reach the top (take 1 step).
#         - For each step, you can either:
#           - Take 1 step and solve the subproblem for `n-1` steps.
#           - Take 2 steps and solve the subproblem for `n-2` steps.
#         - The result for each step `i` is the sum of the results of the two subproblems.

#         Note: This implementation uses a recursive approach without memoization, which is not efficient
#         for large `n` due to repeated calculations. A more efficient solution would use dynamic
#         programming with memoization or an iterative approach.

#         Args:
#         - n: The total number of steps in the staircase.

#         Returns:
#         - The number of distinct ways to reach the top of the staircase.
#         """

#         def climb(i: int) -> int:
#             """
#             This is a helper function that calculates the number of ways to climb a staircase
#             with `i` steps remaining using recursion.

#             Args:
#             - i: The number of steps remaining.

#             Returns:
#             - The number of distinct ways to reach the top from step `i`.
#             """
            
#             # Base case: If there are 0 steps remaining, there's 1 way to stay at the top.
#             if i == 0:
#                 return 1
            
#             # Base case: If there is 1 step remaining, there's only 1 way to reach the top.
#             if i == 1:
#                 return 1
            
#             # Recursive case: The total ways to reach the top from step `i` is the sum of:
#             # - The ways to reach the top from step `i-1` (taking 1 step).
#             # - The ways to reach the top from step `i-2` (taking 2 steps).
#             return climb(i - 1) + climb(i - 2)
        
#         # Start the recursion from the given number of steps `n`.
#         return climb(n)

        