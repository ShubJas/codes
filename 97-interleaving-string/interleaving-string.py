class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        n3 = len(s3)

        # If the total length of s3 is not equal to the sum of s1 and s2, return False
        if n3 != n1 + n2:
            return False

        # Initialize a 2D DP array with False
        dp = [[False] * (n2 + 1) for _ in range(n1 + 1)]

        # Base case: Empty strings can interleave to form an empty string
        dp[0][0] = True

        # Fill the first row (considering only s1 and s3)
        for i1 in range(1, n1 + 1):
            dp[i1][0] = dp[i1 - 1][0] and s1[i1 - 1] == s3[i1 - 1]

        # Fill the first column (considering only s2 and s3)
        for i2 in range(1, n2 + 1):
            dp[0][i2] = dp[0][i2 - 1] and s2[i2 - 1] == s3[i2 - 1]

        # Fill the rest of the DP table
        for i1 in range(1, n1 + 1):
            for i2 in range(1, n2 + 1):
                # The character in s3 must match the current character in s1 or s2
                dp[i1][i2] = (dp[i1 - 1][i2] and s1[i1 - 1] == s3[i1 + i2 - 1]) or \
                             (dp[i1][i2 - 1] and s2[i2 - 1] == s3[i1 + i2 - 1])

        # The result is whether the entirety of s1 and s2 can interleave to form s3
        return dp[n1][n2]




# class Solution:
#     def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
#         n1 = len(s1)
#         n2 = len(s2)
#         n3 = len(s3)

#         if n3 != n1 + n2:
#             return False

#         dp = [[-1]* n2 for _ in range(n1)]
#         def calc(i1,i2):
#             i = i1 + i2 + 1
#             if i1<0:
#                 return s2[:i2+1] == s3[:i+1]
#             elif i2<0:
#                 return s1[:i1+1] == s3[:i+1]
            
#             if dp[i1][i2] != -1:
#                 return dp[i1][i2]

#             if s1[i1] == s2[i2] == s3[i]:
#                 dp[i1][i2] = calc(i1-1,i2) or calc(i1,i2-1)
#                 return dp[i1][i2]
#             elif s1[i1] == s3[i]:
#                 dp[i1][i2] = calc(i1-1,i2)
#                 return dp[i1][i2]
#             elif s2[i2] == s3[i]:
#                 dp[i1][i2] = calc(i1,i2-1)
#                 return dp[i1][i2]
#             else:
#                 dp[i1][i2] = False
#                 return dp[i1][i2]
        
#         return calc(n1-1,n2-1)