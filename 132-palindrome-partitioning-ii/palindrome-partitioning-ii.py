class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)  # Array to store the minimum cuts needed for each prefix
        is_palindrome = [[False] * n for _ in range(n)]  # Precompute palindrome status

        # Precompute the palindrome status for every substring
        for end in range(n):
            for start in range(end + 1):
                if s[start] == s[end] and (end - start <= 2 or is_palindrome[start + 1][end - 1]):
                    is_palindrome[start][end] = True

        # Fill dp array from the end to the start
        for i in range(n - 1, -1, -1):
            min_cuts = float('inf')
            # Calculate the minimum cuts needed for the substring s[i:n]
            for j in range(i, n):
                if is_palindrome[i][j]:
                    cuts = 1 + dp[j + 1]
                    min_cuts = min(min_cuts, cuts)
            dp[i] = min_cuts

        return dp[0] - 1  # Subtract 1 because we want the number of cuts, not partitions


# class Solution:
#     def ispal(self,sub):
#         i = 0
#         j = len(sub) -1
#         while i < j:
#             if sub[i] != sub[j]:
#                 return False
#             i +=1
#             j -=1
#         return True
# # i -> 0 to n - 1
# # base case - at n = 0 
#     def minCut(self, s: str) -> int:

#         n = len(s)


#         dp = [0] * (n+1) # base case covered here


#         for i in range(n-1,-1,-1):

#             sub  = ''
#             min_cuts = float('inf')

#             for j in range(i,n):

#                 sub += s[j]
#                 if self.ispal(sub):
#                     cuts  = 1 + dp[j+1]
#                     min_cuts = min(min_cuts,cuts)
            
#             dp[i] = min_cuts
        
#         return dp[0] - 1 


# class Solution:
#     def ispal(self,sub):
#         i = 0
#         j = len(sub) -1
#         while i < j:
#             if sub[i] != sub[j]:
#                 return False
#             i +=1
#             j -=1
#         return True

#     def minCut(self, s: str) -> int:

#         n = len(s)


#         dp = [-1] * n


#         def calc(i):

#             if i == n:
#                 return 0

#             if dp[i] != -1:
#                 return dp[i]



#             # sub  = ''
#             min_cuts = float('inf')

#             for j in range(i,n):

#                 # sub += s[j]
#                 # if self.ispal(sub):
#                 if self.ispal(s[i:j+1]):
#                     cuts  = 1 + calc(j+1)
#                     min_cuts = min(min_cuts,cuts)
            
#             dp[i] = min_cuts
            
#             return dp[i]
        
    
#         return calc(0) - 1 


# class Solution:
#     def ispal(self, sub):
#         """
#         Helper function to check if a given substring is a palindrome.
#         """
#         i = 0
#         j = len(sub) - 1
#         while i < j:
#             if sub[i] != sub[j]:  # Check corresponding characters
#                 return False  # If mismatch, not a palindrome
#             i += 1  # Move left pointer inward
#             j -= 1  # Move right pointer inward
#         return True  # All characters matched, it's a palindrome

#     def minCut(self, s: str) -> int:
#         """
#         Main function to find the minimum number of cuts needed for a palindrome partitioning of the string.
#         """

#         n = len(s)

#         def calc(i):
#             """
#             Recursive function to calculate the minimum cuts required starting from index i.
#             """
#             if i == n:
#                 return 0  # Reached the end of the string, no more cuts needed

#             sub = ''  # Initialize the current substring
#             min_cuts = float('inf')  # Initialize the minimum cuts to infinity

#             # Loop through each character from the current index to the end of the string
#             for j in range(i, n):
#                 sub += s[j]  # Extend the current substring
#                 if self.ispal(sub):  # Check if the current substring is a palindrome
#                     # If it's a palindrome, recursively find the minimum cuts needed
#                     cuts = 1 + calc(j + 1)
#                     # Update the minimum cuts if the current partition requires fewer cuts
#                     min_cuts = min(min_cuts, cuts)

#             return min_cuts

#         return calc(0) - 1  # Subtract 1 because as it atts last extra cut at end




        