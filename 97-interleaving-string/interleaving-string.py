class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        n1 = len(s1)
        n2 = len(s2)
        n3 = len(s3)

        if n3 != n1 + n2:
            return False

        dp = [[[-1]* n3 for _ in range(n2)] for _ in range(n1)]
        def calc(i1,i2,i):

            if i1<0:
                return s2[:i2+1] == s3[:i+1]
            elif i2<0:
                return s1[:i1+1] == s3[:i+1]
            
            if dp[i1][i2][i] != -1:
                return dp[i1][i2][i]

            if s1[i1] == s2[i2] == s3[i]:
                dp[i1][i2][i] = calc(i1-1,i2,i-1) or calc(i1,i2-1,i-1)
                return dp[i1][i2][i]
            elif s1[i1] == s3[i]:
                dp[i1][i2][i] = calc(i1-1,i2,i-1)
                return dp[i1][i2][i]
            elif s2[i2] == s3[i]:
                dp[i1][i2][i] = calc(i1,i2-1,i-1)
                return dp[i1][i2][i]
            else:
                dp[i1][i2][i] = False
                return dp[i1][i2][i]
        
        return calc(n1-1,n2-1,n3-1)