# Intuition - find longest palindrome (fix it) (by reversing and LCS), the remaining letters have to be added
class Solution:
    def minInsertions(self, s: str) -> int:
        

        n = len(s)
        t = s[::-1]

        # Initialize dp array
        prev = [0] * (n + 1) 

        # Fill the dp array
        for i1 in range(1, n + 1):
            curr = [0] * (n + 1) 

            for i2 in range(1, n + 1):
                if s[i1 - 1] == t[i2 - 1]:
                    curr[i2] = 1 + prev[i2 - 1]
                else:
                    curr[i2] = max(prev[i2], curr[i2 - 1])
            prev = curr
        # get longest pal ( see last leetcode in striver playlist)
        

        return n - prev[n]

# class Solution:
#     def minInsertions(self, s: str) -> int:

#         n = len(s)

#         dp = [[-1] * (n) for _ in range(n)]

#         def calc(i1,i2):

            
#             if i1 > i2:  # if the starting index crosses the ending index
#                 return 0


#             if i1 == i2:
#                 return 1
            
#             if dp[i1][i2] != -1:
#                 return dp[i1][i2]
            
#             if s[i1] == s[i2]:
#                 # pick case
#                 dp[i1][i2] = 2 + calc(i1+1,i2-1)
#             else:
#                 # not pick case
#                 dp[i1][i2] = max(calc(i1+1,i2),calc(i1,i2-1))
#             return dp[i1][i2]
        
#         return n - calc(0,n-1)

