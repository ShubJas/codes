# # start -> 0 to n+1
# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
#         n = len(s)

#         dp = [False] * (n+1)
#         dp[n] = True
#         words = set(wordDict)

#         for start in range(n-1, -1, -1):
#             word = ''
#             for i in range(start, n):
#                 word += s[i]
#                 if word in words:
#                     if dp[i + 1]:
#                         dp[start] = True
#                         break  # No need to check further, as we found a valid segmentation

#         return dp[0]



class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        n = len(s) 

        dp = [None] * (n+1)

        words = set(wordDict)
        def calc(start):

            if start >= n:
                return True
            
            if dp[start] is not None:
                return dp[start]

            word = ''
            for i in range(start,n):
                word += s[i]
                if word in words:
                    dp[i+1] = calc(i+1)
                    if dp[i+1]:
                        return True
            
            return False
        

        return calc(0)

