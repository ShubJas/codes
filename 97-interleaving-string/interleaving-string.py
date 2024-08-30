class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        

        n1 = len(s1)
        n2 = len(s2)
        n3 = len(s3)

        if n3 != n1 + n2:
            return False
        


        dp = [[False]* (n2+1) for _ in range(n1+1)]

        dp[0][0] = True

        for i1 in range(1,n1+1):
            dp[i1][0] = dp[i1-1][0] and s1[i1-1] == s3[i1 - 1]
        

        for i2 in range(1,n2+1):
            dp[0][i2] = dp[0][i2-1] and s2[i2-1] == s3[i2 -1]
        

        for i1 in range(1,n1+1):
            for i2 in range(1,n2+1):

                dp[i1][i2] = (dp[i1-1][i2] and s1[i1-1] == s3[i1 + i2 -1]) or (dp[i1][i2-1] and s2[i2-1] == s3[i1 + i2 -1]) 


        return dp[n1][n2]