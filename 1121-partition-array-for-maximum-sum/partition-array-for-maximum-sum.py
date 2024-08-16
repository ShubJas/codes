#  i-> 0 to n-1
#  n base case -> 0
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:

        
        n = len(arr)
        


        dp = [0] * (n+1)

        for i in range(n-1,-1,-1):

            maxi = -float('inf') 
            for j in range(i,min(n,i+k)):
                S = (j-i+1) * max(arr[i:j+1]) + dp[j+1]
                maxi = max(maxi,S) 
            
            dp[i] = maxi
        
        return dp[0]


# class Solution:
#     def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:

        
#         n = len(arr)
        


#         dp = [-1] * (n+1)
#         def calc(i):

#             if i == n:
#                 return 0
            
#             if dp[i] != -1:
#                 return dp[i]

#             maxi = -float('inf') 
#             for j in range(i,min(n,i+k)):
#                 S = (j-i+1) * max(arr[i:j+1]) + calc(j+1)
#                 maxi = max(maxi,S) 
            
#             dp[i] = maxi

#             return dp[i]
        
#         return calc(0)



# class Solution:
#     def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:

#         # The length of the array 'arr'
#         n = len(arr)

#         # A helper function 'calc' that is used to calculate the maximum sum possible
#         # starting from index 'i' in the array.
#         def calc(i):
#             # Base case: If we have processed all elements in the array, return 0.
#             if i == n:
#                 return 0

#             # Initialize 'maxi' to a very small value to keep track of the maximum sum
#             # we can achieve starting from index 'i'.
#             maxi = -float('inf')

#             # Loop through the subarray starting at 'i' and ending at 'j', where 'j'
#             # can range from 'i' to 'min(n, i + k)'. This loop essentially checks all
#             # possible partitions of size up to 'k' starting from index 'i'.
#             for j in range(i, min(n, i + k)):
#                 # Calculate the sum 'S' for the current partition, which is the product
#                 # of the size of the partition '(j - i + 1)' and the maximum element
#                 # in the partition 'max(arr[i:j+1])'. We add the result of recursively
#                 # calling 'calc' for the next segment of the array starting at 'j + 1'.
#                 S = (j - i + 1) * max(arr[i:j + 1]) + calc(j + 1)

#                 # Update 'maxi' to be the maximum of the current 'maxi' and 'S'. This
#                 # ensures that 'maxi' will eventually hold the maximum sum possible
#                 # for any valid partition starting at index 'i'.
#                 maxi = max(maxi, S)

#             # Return the maximum sum for partitions starting at index 'i'.
#             return maxi

#         # Start the calculation from index 0, which means we're looking for the
#         # maximum sum possible for the entire array with partitions of size up to 'k'.
#         return calc(0)
