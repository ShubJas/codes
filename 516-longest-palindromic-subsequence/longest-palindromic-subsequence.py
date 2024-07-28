class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        n = len(s)

        dp = [[-1] * (n) for _ in range(n)]

        def calc(i1,i2):

            
            if i1 > i2:  # if the starting index crosses the ending index
                return 0


            if i1 == i2:
                return 1
            
            if dp[i1][i2] != -1:
                return dp[i1][i2]
            
            # p = -float('inf')
            if s[i1] == s[i2]:
                # pick case
                dp[i1][i2] = 2 + calc(i1+1,i2-1)
            else:
                # not pick case
                dp[i1][i2] = max(calc(i1+1,i2),calc(i1,i2-1))
            return dp[i1][i2]
        
        return calc(0,n-1)
        

# class Solution:
#     def longestPalindromeSubseq(self, s: str) -> int:

#         n = len(s)

#         dp = [[-1] * (n) for _ in range(n)]

#         def calc(i1,i2):

            
#             if i1 > i2:  # if the starting index crosses the ending index
#                 return 0


#             if i1 == i2:
#                 return 1
            
#             if dp[i1][i2] != -1:
#                 return dp[i1][i2]
            
#             p = -float('inf')
#             if s[i1] == s[i2]:
#                 p = 2 + calc(i1+1,i2-1)
            
#             np1 = calc(i1+1,i2)
#             np2 = calc(i1,i2-1)

#             dp[i1][i2] = max(p,np1,np2)
#             return dp[i1][i2]
        
#         return calc(0,n-1)
        


# class Solution:
#     def longestPalindromeSubseq(self, s: str) -> int:

#         n = len(s)


        
#         def calc(i1,i2):

            
#             if i1 > i2:  # if the starting index crosses the ending index
#                 return 0


#             if i1 == i2:
#                 return 1
            
#             p = -float('inf')
#             if s[i1] == s[i2]:
#                 p = 2 + calc(i1+1,i2-1)
            
#             np1 = calc(i1+1,i2)
#             np2 = calc(i1,i2-1)

#             return max(p,np1,np2)
        
#         return calc(0,n-1)
        