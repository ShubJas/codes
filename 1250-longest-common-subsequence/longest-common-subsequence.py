class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        n1 = len(text1)
        n2 = len(text2)

        prev = [0] * n2

        for i2 in range(n2):
            if text1[0] in list(text2[:i2+1]):
                prev[i2] = 1
        
        # for i1 in range(n1):
        #     if text2[0] in list(text1[:i1+1]):
        #         dp[i1][0] = 1

        for i1 in range(1,n1):
            curr = [0] * n2
            if text2[0] in list(text1[:i1+1]):
                curr[0] = 1
            for i2 in range(1,n2):


                take = -float('inf') 

                if text1[i1] == text2[i2]:
                    take = 1 + prev[i2-1]

                ntake1 = prev[i2]
                ntake2 = curr[i2-1]


                curr[i2] = max(take,ntake1,ntake2)
            prev = curr     

        return prev[n2-1]


# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:

#         n1 = len(text1)
#         n2 = len(text2)

#         dp = [[0] * n2 for _ in range(n1)]

#         for i2 in range(n2):
#             if text1[0] in list(text2[:i2+1]):
#                 dp[0][i2] = 1
        
#         for i1 in range(n1):
#             if text2[0] in list(text1[:i1+1]):
#                 dp[i1][0] = 1

#         for i1 in range(1,n1):

#             for i2 in range(1,n2):


#                 take = -float('inf') 

#                 if text1[i1] == text2[i2]:
#                     take = 1 + dp[i1-1][i2-1]

#                 ntake1 = dp[i1-1][i2]
#                 ntake2 = dp[i1][i2-1]


#                 dp[i1][i2] = max(take,ntake1,ntake2)     

#         return dp[n1-1][n2-1]

# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:

#         n1 = len(text1)
#         n2 = len(text2)

#         dp = [[-1] * n2 for _ in range(n1)]

#         def calc(i1,i2):


#             # if i1< 0  or i2 < 0:
#             #     return 0


#             if i1 == 0:
#                 if text1[0] in list(text2[:i2+1]):
#                     return 1
#                 return 0
            
#             if i2 == 0:
#                 if text2[0] in list(text1[:i1+1]):
#                     return 1
#                 return 0

            
#             if dp[i1][i2] != -1:
#                 return dp[i1][i2]

#             take = -float('inf') 

#             if text1[i1] == text2[i2]:
#                 take = 1 + calc(i1-1,i2-1)

#             ntake1 = calc(i1-1,i2)
#             ntake2 = calc(i1,i2-1)


#             dp[i1][i2] = max(take,ntake1,ntake2)
#             return dp[i1][i2]

        

#         return calc(n1-1,n2-1)

# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:

#         n1 = len(text1)
#         n2 = len(text2)


#         def calc(i1,i2):


#             # if i1< 0  or i2 < 0:
#             #     return 0


#             # Base case: When we are at the first character of text1
#             if i1 == 0:
#                 if text1[0] in list(text2[:i2+1]):
#                     return 1  # If the first character of text1 is found in text2, return 1
#                 return 0  # Otherwise, return 0

#             # Base case: When we are at the first character of text2
#             if i2 == 0:
#                 if text2[0] in list(text1[:i1+1]):
#                     return 1  # If the first character of text2 is found in text1, return 1
#                 return 0  # Otherwise, return 0

#             take = -float('inf') 

#             if text1[i1] == text2[i2]:
#                 take = 1 + calc(i1-1,i2-1)

#             ntake1 = calc(i1-1,i2)
#             ntake2 = calc(i1,i2-1)

#             return max(take,ntake1,ntake2)

        

#         return calc(n1-1,n2-1)

