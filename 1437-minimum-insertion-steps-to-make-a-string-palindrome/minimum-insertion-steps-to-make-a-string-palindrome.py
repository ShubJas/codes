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

