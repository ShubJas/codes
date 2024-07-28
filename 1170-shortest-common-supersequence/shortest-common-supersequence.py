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


        # # Memoization for the backtrack function
        # memo = {}

        # # Function to backtrack and find all SCS
        # def backtrack(i, j):
        #     if (i, j) in memo:
        #         return memo[(i, j)]

        #     if i == 0:
        #         return {str2[:j]}
        #     if j == 0:
        #         return {str1[:i]}

        #     if str1[i - 1] == str2[j - 1]:
        #         result = {x + str1[i - 1] for x in backtrack(i - 1, j - 1)}
        #     else:
        #         result = set()
        #         if dp[i - 1][j] >= dp[i][j - 1]:
        #             result.update({x + str1[i - 1] for x in backtrack(i - 1, j)})
        #         if dp[i][j - 1] >= dp[i - 1][j]:
        #             result.update({x + str2[j - 1] for x in backtrack(i, j - 1)})

        #     memo[(i, j)] = result
        #     return result

        # # Get all SCS
        # scs_set = backtrack(n1, n2)
        # scs_list = list(scs_set)
        # scs_list.sort()

        # print(scs_list)

        # return scs_list[0]



            




