class Solution:
    def minDistance(self, word1: str, word2: str) -> int:



        n1 = len(word1)
        n2 = len(word2)


        dp = [[-1]* n2 for _ in range(n1)]

        def calc(i1,i2):


            if i1<0:
                return i2+1

            if i2<0:
                return i1+1

            
            if dp[i1][i2] != -1:
                return dp[i1][i2]

            if word1[i1] == word2[i2]: # match case
                dp[i1][i2] = calc(i1-1,i2-1)
                return dp[i1][i2]
            
            else: # mis-match case
                insert = 1 + calc(i1,i2-1)
                delete = 1 + calc(i1-1,i2)
                replace = 1 + calc(i1-1,i2-1)
                dp[i1][i2] = min(insert,delete,replace)
                return dp[i1][i2]
        

        return calc(n1-1,n2-1)


# class Solution:
#     def minDistance(self, word1: str, word2: str) -> int:

#         # Get the lengths of the two words
#         n1 = len(word1)
#         n2 = len(word2)

#         # Recursive function to calculate minimum operations
#         def calc(i1, i2):
#             # Base case: if we have exhausted word1, we need to insert all remaining characters of word2
#             if i1 < 0:
#                 return i2 + 1

#             # Base case: if we have exhausted word2, we need to delete all remaining characters of word1
#             if i2 < 0:
#                 return i1 + 1

#             # If the characters match, move both pointers one step back
#             if word1[i1] == word2[i2]:  # match case
#                 return calc(i1 - 1, i2 - 1)
#             else:  # mis-match case
#                 # Calculate the cost for each operation
#                 insert = 1 + calc(i1, i2 - 1)  # Insert character from word2 into word1
#                 delete = 1 + calc(i1 - 1, i2)  # Delete character from word1
#                 replace = 1 + calc(i1 - 1, i2 - 1)  # Replace character in word1 with character from word2
#                 # Return the minimum cost among the three operations
#                 return min(insert, delete, replace)

#         # Call the recursive function starting from the end of both words
#         return calc(n1 - 1, n2 - 1)

        