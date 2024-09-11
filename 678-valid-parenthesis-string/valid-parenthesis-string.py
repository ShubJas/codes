class Solution:
    def checkValidString(self, s: str) -> bool:
        
        n = len(s)
        dp = [[None]*n for _ in range(n)]

        def calc(i,c):

            if c < 0:
                return False 
            
            if i == n:
                return c == 0
            
            if dp[i][c] is not None:
                return dp[i][c]
                

            if s[i] == '(':
                dp[i][c] = calc(i+1,c+1)
                return dp[i][c]

            elif s[i] == ')':
                dp[i][c] = calc(i+1,c-1)
                return dp[i][c]
            else:
                dp[i][c] = calc(i+1,c) or calc(i+1,c+1) or calc(i+1,c-1)
                return dp[i][c]


        return calc(0,0)