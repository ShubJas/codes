class Solution:
    def minSteps(self, n: int) -> int:
        # Memoization dictionary to store results of subproblems
        memo = {}

        def calc(l, clipboard):
            # Base case: if the current length equals n, no more steps needed
            if l == n:
                return 0
            
            # If current length exceeds n, return infinity to indicate it's not a valid path
            if l > n:
                return float('inf')
            
            # Check if the result for the current state is already computed
            if (l, clipboard) in memo:
                return memo[(l, clipboard)]

            # Case 1: Copy the current length and store it in the clipboard
            copy = float('inf')
            if clipboard != l:  # Only copy if clipboard doesn't already have the current length
                copy = 1 + calc(l, l)
            
            # Case 2: Paste the clipboard content to the current length
            paste = float('inf')
            if clipboard > 0:  # Only paste if there's something in the clipboard
                paste = 1 + calc(l + clipboard, clipboard)
            
            # Store the result in memo and return the minimum of copy and paste
            memo[(l, clipboard)] = min(copy, paste)
            return memo[(l, clipboard)]

        # Start the calculation with length 1 and nothing on the clipboard (clipboard = 0)
        return calc(1, 0)
