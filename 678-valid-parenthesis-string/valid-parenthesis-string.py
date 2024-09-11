class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        
        # dp[i][c] will be True if it's possible to have a valid string starting at index i with 'c' unmatched '('.
        dp = [[False] * (n + 1) for _ in range(n + 1)]
        
        # Base case: If we've processed the whole string and there are no unmatched '(', it's valid.
        dp[n][0] = True  # At the end of the string with 0 open parentheses, it's valid.
        
        # Fill dp table from bottom to top
        for i in range(n - 1, -1, -1):  # Iterate over the string from the end to the start
            for c in range(n):  # c represents the count of unmatched '(' so far (open parentheses)
                
                if s[i] == '(':
                    # If it's an opening parenthesis, we need to have at least one more closing one later
                    if c + 1 <= n:  # Only valid if we don't go out of bounds
                        dp[i][c] = dp[i + 1][c + 1]
                
                elif s[i] == ')':
                    # If it's a closing parenthesis, we need to have already opened one
                    if c - 1 >= 0:  # Only valid if unmatched '(' exists (c > 0)
                        dp[i][c] = dp[i + 1][c - 1]
                
                else:  # s[i] == '*'
                    # '*' can be '(', ')' or empty (nothing happens)
                    dp[i][c] = dp[i + 1][c]  # Treat '*' as an empty character (no change in 'c')
                    if c + 1 <= n:  # Treat '*' as an opening parenthesis '('
                        dp[i][c] = dp[i][c] or dp[i + 1][c + 1]
                    if c - 1 >= 0:  # Treat '*' as a closing parenthesis ')'
                        dp[i][c] = dp[i][c] or dp[i + 1][c - 1]

        # The answer will be stored in dp[0][0], meaning at the start of the string with no open parentheses.
        return dp[0][0]


# # i -> 0 to n - 1
# # c -> 0 to n + 1 
# class Solution:
#     def checkValidString(self, s: str) -> bool:
        
#         n = len(s)
#         dp = [[None]*n for _ in range(n)]

#         def calc(i,c):

#             if c < 0:
#                 return False 
            
#             if i == n:
#                 return c == 0
            
#             if dp[i][c] is not None:
#                 return dp[i][c]
                

#             if s[i] == '(':
#                 dp[i][c] = calc(i+1,c+1)
#                 return dp[i][c]

#             elif s[i] == ')':
#                 dp[i][c] = calc(i+1,c-1)
#                 return dp[i][c]
#             else:
#                 dp[i][c] = calc(i+1,c) or calc(i+1,c+1) or calc(i+1,c-1)
#                 return dp[i][c]


#         return calc(0,0)

# class Solution:
#     def checkValidString(self, s: str) -> bool:
        
#         n = len(s)


#         def calc(i,c):

#             if c < 0:
#                 return False 
            
#             if i == n:
#                 return c == 0
                

#             if s[i] == '(':
#                 return calc(i+1,c+1)

#             elif s[i] == ')':
#                 return calc(i+1,c-1)
#             else:
#                 return calc(i+1,c) or calc(i+1,c+1) or calc(i+1,c-1)


#         return calc(0,0)