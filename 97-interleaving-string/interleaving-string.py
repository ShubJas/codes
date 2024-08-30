# class Solution:
#     def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
#         n1 = len(s1)
#         n2 = len(s2)
#         n3 = len(s3)

#         if n3 != n1 + n2:
#             return False

#         dp = [[[False]* n3 for _ in range(n2+1)] for _ in range(n1+1)]


#         for i in range(n3):
#             for i2 in range(1,n2+1):
#                 dp[0][i2][i] = s2[:i2] == s3[:i+1]
        

#         for i in range(n3):
#             for i1 in range(1,n1+1):
#                 dp[i1][0][i] = s1[:i1] == s3[:i+1]


#         for i1 in range(1,n1+1):
#             for i2 in range(1,n2+1):
#                 for i in range(n3):
#                     if s1[i1-1] == s2[i2-1] == s3[i]:
#                         dp[i1][i2][i] = dp[i1-1][i2][i-1] or dp[i1][i2-1][i-1]
#                     elif s1[i1-1] == s3[i]:
#                         dp[i1][i2][i] = dp[i1-1][i2][i-1]
#                     elif s2[i2-1] == s3[i]:
#                         dp[i1][i2][i] = dp[i1][i2-1][i-1]
#                     else:
#                         dp[i1][i2][i] = False

        
#         return dp[n1][n2][n3-1]



class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        n1 = len(s1)
        n2 = len(s2)
        n3 = len(s3)

        if n3 != n1 + n2:
            return False

        dp = [[-1]* n2 for _ in range(n1)]
        def calc(i1,i2):
            i = i1 + i2 + 1
            if i1<0:
                return s2[:i2+1] == s3[:i+1]
            elif i2<0:
                return s1[:i1+1] == s3[:i+1]
            
            if dp[i1][i2] != -1:
                return dp[i1][i2]

            if s1[i1] == s2[i2] == s3[i]:
                dp[i1][i2] = calc(i1-1,i2) or calc(i1,i2-1)
                return dp[i1][i2]
            elif s1[i1] == s3[i]:
                dp[i1][i2] = calc(i1-1,i2)
                return dp[i1][i2]
            elif s2[i2] == s3[i]:
                dp[i1][i2] = calc(i1,i2-1)
                return dp[i1][i2]
            else:
                dp[i1][i2] = False
                return dp[i1][i2]
        
        return calc(n1-1,n2-1)