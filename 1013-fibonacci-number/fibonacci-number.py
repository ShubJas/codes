# Bottom - up - iterative ( optimized)
class Solution:
    def fib(self, n: int) -> int:
        # Handle the base case where n is 0
        if n == 0:
            return 0
        
        # Initialize the first two Fibonacci numbers
        p2 = 0  # Fibonacci number for index 0
        p1 = 1  # Fibonacci number for index 1
        
        # If n is 1, we can return the result early
        if n == 1:
            return p1
        
        # Iterate from 2 to n to compute the Fibonacci sequence
        for i in range(2, n + 1):
            curr = p1 + p2  # Compute the current Fibonacci number
            p2 = p1  # Update p2 to the previous Fibonacci number
            p1 = curr  # Update p1 to the current Fibonacci number
        
        # Return the Fibonacci number for index n
        return p1
        
# # Bottom - up - iterative 
# class Solution:
#     def fib(self, n: int) -> int:
#         # Initialize a list to store the computed Fibonacci values. 
#         # The size of the list is n+1 because we want to include the value for index n.
#         dp = [-1] * (n + 1)
        
#         # Base cases: 
#         # fib(0) is 0
#         dp[0] = 0
        
#         # fib(1) is 1. 
#         # We need to handle the case when n is 0 separately to avoid index out of range error.
#         if n > 0:
#             dp[1] = 1

#         # Fill the dp array from index 2 to n.
#         for i in range(2, n + 1):
#             # fib(i) is the sum of fib(i-1) and fib(i-2)
#             dp[i] = dp[i - 1] + dp[i - 2]
        
#         # Return the Fibonacci number for index n.
#         return dp[n]



# # TOP down -recusion
# class Solution:
#     def fib(self, n: int) -> int:
#         # Initialize a list to store the computed Fibonacci values. 
#         # The size of the list is n+1 because we want to include the value for index n.
#         dp = [-1] * (n + 1)
        
#         def fibbo(i):
#             # Base case: if i is 0 or 1, return i. 
#             # This is because fib(0) = 0 and fib(1) = 1.
#             if i <= 1:
#                 return i
            
#             # If the value for fib(i) is already computed and stored in dp, return that value.
#             if dp[i] != -1:
#                 return dp[i]
            
#             # Otherwise, compute the value by making recursive calls to fibbo(i-1) and fibbo(i-2)
#             # and store the result in dp[i].
#             dp[i] = fibbo(i - 1) + fibbo(i - 2)
            
#             # Return the computed value for fib(i).
#             return dp[i]
        
#         # Start the computation by calling fibbo(n). This will compute and return fib(n).
#         return fibbo(n)
