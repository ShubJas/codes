class Solution:
    def match(self,s1,s2):

        n1 = len(s1)
        n2 = len(s2)
        if n2 != n1 + 1:
            return False
            
        i1 = i2 = 0

        while i1 < n1 and i2 < n2:

            if s1[i1] == s2[i2] and i1 < n1:
                i1+=1
                i2+=1
            else:
                i2+=1
        
        return i1 == n1 # extra char case is handeled above



    def longestStrChain(self, words: List[str]) -> int:
        
        n = len(words)
        words.sort(key = lambda word: len(word))

        print(words)


        dp = [1] * n

        for i in range(1,n):

            for prev_i in range(i):
                count = 0
                if self.match(words[prev_i],words[i]) and (dp[prev_i] +1  > dp[i]):
                    dp[i] = dp[prev_i] +1
        
        return max(dp)

                        