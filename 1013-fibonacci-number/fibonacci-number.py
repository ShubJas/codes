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
