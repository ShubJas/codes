class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        n1 = len(word1)
        n2 = len(word2)


        # Initialize dp array
        prev = [0] * (n2 + 1) 

        # Fill the dp array
        for i1 in range(1, n1 + 1):
            curr = [0] * (n2 + 1) 

            for i2 in range(1, n2 + 1):
                if word1[i1 - 1] == word2[i2 - 1]:
                    curr[i2] = 1 + prev[i2 - 1]
                else:
                    curr[i2] = max(prev[i2], curr[i2 - 1])
            prev = curr
        # get longest pal ( see last leetcode in striver playlist)
        

        return n1 + n2 - 2*prev[n2]