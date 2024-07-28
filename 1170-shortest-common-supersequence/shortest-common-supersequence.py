# Intuition - n1 + n2 - LCS is the length of SCS. fill the table of LCS then traverse
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        
        n1 = len(str1)
        n2 = len(str2)


        dp = [[0] * (n2+1) for _ in range(n1+1)]


        for i1 in range(1,n1+1):

            for i2 in range(1,n2+1):

                if str1[i1-1] == str2[i2-1]:
                    dp[i1][i2] = 1 + dp[i1-1][i2-1]
                else:
                    dp[i1][i2] = max(dp[i1-1][i2],dp[i1][i2-1])
                

        # Reconstruct the shortest common supersequence
        i1 = n1
        i2 = n2  
        ans = []

        while i1 > 0 and i2 > 0:
            if str1[i1 - 1] == str2[i2 - 1]:
                ans.append(str1[i1 - 1])
                i1 -= 1
                i2 -= 1
            else:
                if dp[i1 - 1][i2] >= dp[i1][i2 - 1]:
                    ans.append(str1[i1 - 1])
                    i1 -= 1
                else:
                    ans.append(str2[i2 - 1])
                    i2 -= 1

        # Add remaining characters of str1 and str2
        while i1 > 0:
            ans.append(str1[i1 - 1])
            i1 -= 1

        while i2 > 0:
            ans.append(str2[i2 - 1])
            i2 -= 1

        # The characters were added in reverse order
        return ''.join(ans[::-1])



            




