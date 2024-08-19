# l -> 1 to n-1
# base case dp[n][] = 0
# clipboard -> 0 to l



# class Solution:
#     def minSteps(self, n: int) -> int:

#         dp = [[float('inf')]* (n+1) for _ in range(n+1)]

#         for clipboard in range(n+1):
#             dp[n][clipboard] = 0


#         for l in range(n-1,0,-1):

#             for clipboard in range(l,-1,-1):

#                 copy = paste = float('inf')

#                 if l!= clipboard:
#                     copy = 1 + dp[l][l]
                
#                 if clipboard>0 and l + clipboard <= n:
#                     paste = 1 + dp[l + clipboard][clipboard]
                

#                 dp[l][clipboard] = min(copy,paste)

     
#         return dp[1][0]

class Solution:
    def minSteps(self, n: int) -> int:

        dp = [[-1]* (n+1) for _ in range(n+1)]
        
        def calc(l,clipboard):

            if l == n:
                return 0
            
            if l>n:
                return float('inf')
            

            if dp[l][clipboard] != -1:
                return dp[l][clipboard]
            copy = paste = float('inf')
            if l!= clipboard:
                copy = 1 + calc(l,l)
            
            if clipboard>0:
                paste = 1 + calc(l + clipboard,clipboard)
            

            dp[l][clipboard] = min(copy,paste)
            return dp[l][clipboard]
        

        
        return calc(1,0)



# class Solution:
#     def minSteps(self, n: int) -> int:
#         # Define a recursive function 'calc' to calculate the minimum steps
#         # 'l' represents the current length of the string "A"
#         # 'clipboard' represents the current content of the clipboard (number of "A"s copied)

#         def calc(l, clipboard):

#             # Base case: If the current length 'l' equals the target length 'n',
#             # we don't need any more steps, so return 0
#             if l == n:
#                 return 0
            
#             # If the current length 'l' exceeds the target 'n',
#             # return infinity to indicate that this is not a valid path
#             if l > n:
#                 return float('inf')

#             # Initialize the steps required for both possible operations (copy and paste)
#             # Set to infinity initially, indicating that if no valid operation is found, this path is not optimal
#             copy = paste = float('inf')

#             # If the current length 'l' is not the same as the clipboard content,
#             # we can perform a copy operation (this avoids redundant copying)
#             if l != clipboard:
#                 # Perform the copy operation, which takes 1 step, and then recursively calculate
#                 # the steps required from the new state where the clipboard is updated to the current length
#                 copy = 1 + calc(l, l)
            
#             # If there is something in the clipboard (clipboard > 0),
#             # we can perform a paste operation
#             if clipboard > 0:
#                 # Perform the paste operation, which takes 1 step, and then recursively calculate
#                 # the steps required from the new state where the length is increased by the clipboard content
#                 paste = 1 + calc(l + clipboard, clipboard)
            
#             # Return the minimum steps required between performing a copy or a paste operation
#             return min(copy, paste)

#         # Start the recursive calculation with an initial length of 1 (the initial "A")
#         # and an empty clipboard (represented by 0)
#         return calc(1, 0)
