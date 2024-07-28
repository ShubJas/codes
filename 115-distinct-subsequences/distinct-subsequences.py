class Solution:
    def numDistinct(self, s: str, t: str) -> int:


        n1 = len(s)
        n2 = len(t)


        dp = [[0] * (n2+1) for _ in range(n1+1)]


        for i2 in range(n2+1):
            dp[0][i2] = 0
        
        for i1 in range(n1+1):
            dp[i1][0] = 1

        for i1 in range(1,n1+1):

            for i2 in range(1,n2+1):

                if s[i1-1] == t[i2-1]:
                    dp[i1][i2] =  dp[i1-1][i2-1] + dp[i1-1][i2]
                else:
                    dp[i1][i2] = dp[i1-1][i2] 
        
        return dp[n1][n2]



# class Solution:
#     def numDistinct(self, s: str, t: str) -> int:


#         n1 = len(s)
#         n2 = len(t)


#         dp = [[-1] * n2 for _ in range(n1)]

#         def calc(i1,i2):

#             # In tabulation this will come after cuz this is first in recur
#             if i2 < 0:
#                 return 1

#             if i1 < 0:
#                 return 0 
            
#             if dp[i1][i2] != -1:
#                 return dp[i1][i2]

#             if s[i1] == t[i2]:
#                 dp[i1][i2] =  calc(i1-1,i2-1) + calc(i1-1,i2)
#             else:
#                 dp[i1][i2] = calc(i1-1,i2) 
#             return  dp[i1][i2]
        
#         return calc(n1-1,n2-1)

# class Solution:
#     def numDistinct(self, s: str, t: str) -> int:


#         n1 = len(s)
#         n2 = len(t)

#         def calc(i1,i2):


#             # if i2 < 0:
#             #     return 1

#             # if i1 < 0:
#             #     return 0 

#             mt = mnt = 0 #match take , match not take


        #     if s[i1] == t[i2]:
        #         mt = calc(i1-1,i2-1)
        #         mnt = calc(i1-1,i2)
        #         return mt + mnt
        #     else:
            
        #         # Not take
        #         nt = calc(i1-1,i2)


        #         return  nt 
        
        # return calc(n1-1,n2-1)
 
        