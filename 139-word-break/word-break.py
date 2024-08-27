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


