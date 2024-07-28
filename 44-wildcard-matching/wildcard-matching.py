class Solution:
    def isMatch(self, s: str, p: str) -> bool:


        n1 = len(s)
        n2 = len(p)

        prev = [False] * (n2+1) 

        # for i1 in range(1,n1+1):
        #     prev[0] =False


        for i2 in range(1,n2+1):
            for i in range(1,i2+1):
                if p[i-1] != '*': 
                    prev[i2]  = False
                    break
                prev[i2] = True
    
    
        prev[0] = True


        for i1 in range(1,n1+1):
            curr = [False] * (n2+1) 
            for i2 in range(1,n2+1):

                if p[i2-1] == '?':
                    result = prev[i2-1]

                elif p[i2-1] == '*':
                    use = prev[i2]
                    not_use = curr[i2-1]
                    result = use or not_use
                
                else:
                    if s[i1-1] == p[i2-1]:
                        result = prev[i2-1]
                    else:
                        result = False

                curr[i2] = result
            prev = curr



        return prev[n2]


# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:


#         n1 = len(s)
#         n2 = len(p)

#         dp = [[False] * (n2+1) for _ in range(n1+1)]

#         for i1 in range(1,n1+1):
#             dp[i1][0] =False


#         for i2 in range(1,n2+1):
#             for i in range(1,i2+1):
#                 if p[i-1] != '*': 
#                     dp[0][i2]  = False
#                     break
#                 dp[0][i2] = True
    
    
#         dp[0][0] = True


#         for i1 in range(1,n1+1):

#             for i2 in range(1,n2+1):

#                 if p[i2-1] == '?':
#                     result = dp[i1-1][i2-1]

#                 elif p[i2-1] == '*':
#                     use = dp[i1-1][i2]
#                     not_use = dp[i1][i2-1]
#                     result = use or not_use
                
#                 else:
#                     if s[i1-1] == p[i2-1]:
#                         result = dp[i1-1][i2-1]
#                     else:
#                         result = False

#                 dp[i1][i2] = result



#         return dp[n1][n2]


# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:


#         n1 = len(s)
#         n2 = len(p)

#         dp = [[None] * n2 for _ in range(n1)]

#         def calc(i1,i2):




            
#             if i1<0 and i2<0:
#                 return True
            

            
#             if i1<0 and i2>=0:
#                 for i in range(i2+1):
#                     if p[i] != '*':    
#                         return False
#                 return True

#             if i1>=0 and i2 <0:
#                 return False

#             if dp[i1][i2] is not None:
#                 return dp[i1][i2]


#             if p[i2] == '?':
#                 result = calc(i1-1,i2-1)

#             elif p[i2] == '*':
#                 use = calc(i1-1,i2)
#                 not_use = calc(i1,i2-1)
#                 result = use or not_use
            
#             else:
#                 if s[i1] == p[i2]:
#                     result = calc(i1-1,i2-1)
#                 else:
#                     result = False

#             dp[i1][i2] = result
#             return dp[i1][i2] 


#         return calc(n1-1,n2-1)
            


# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:

#         # Length of the input string `s`
#         n1 = len(s)
#         # Length of the pattern string `p`
#         n2 = len(p)

#         def calc(i1, i2):
            

#             # Base case 1: If both indices are out of range (both strings fully matched)
#             if i1 < 0 and i2 < 0:
#                 return True

#             # Base case 2: If `s` is out of range but `p` still has characters
#             if i1 < 0 and i2 >= 0:
#                 # If remaining characters in `p` are all '*'(can be considered ''), it's a match
#                 for i in range(i2 + 1):
#                     if p[i] != '*':    
#                         return False
#                 return True

#             # Base case 3: If `p` is out of range but `s` still has characters
#             if i1 >= 0 and i2 < 0:
#                 return False

#             # If the current character in `p` is '?', it matches any single character in `s`
#             if p[i2] == '?':
#                 return calc(i1 - 1, i2 - 1)

#             # If the current character in `p` is '*', it can match any sequence (including empty)
#             elif p[i2] == '*':
#                 # Use '*' to match the current character in `s` and move to the next character in `s`
#                 use = calc(i1 - 1, i2)
#                 # Use '*' as an empty sequence and move to the next character in `p`
#                 not_use = calc(i1, i2 - 1)
#                 return use or not_use
            
#             # If the current characters in `s` and `p` are the same
#             else:
#                 if s[i1] == p[i2]:
#                     return calc(i1 - 1, i2 - 1)
#                 else:
#                     return False
        
#         # Start the recursive check from the last characters of `s` and `p`
#         return calc(n1 - 1, n2 - 1)


        