class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        # looking for the max length of a subsequence that 
        # is strictly ascending order i.e, num[i-blah] < num[i]
        # look for the max val of a subsequence ending at index
        # i the minimum value of the length of the subsequence 
        # ending at i is at least 1 (the smallest subsquence)
        # will store calculated answers in dp
        
        n = len(nums)
        dp = [1]*n
        
        for i in range(1, n):  # calculate the value of i in dp
            for j in range(i): # will look at the prior answer for every value proceeding i
                if nums[i] > nums[j]:  # if i is greater than j then i can be tacked on to the
                                       # the subsequence ending at j BUT ... 
                        
                    dp[i] = max(dp[i], dp[j]+1)   # only update dp[i] if dp[j]+1 is larger than 
                                                  # what was already found.  
        
        return max(dp) 

# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
        
#         n = len(nums)


#         dp = [[-1]* (n+1) for _ in range(n)]

#         def calc(i,prev_i):

#             if i < 0:
#                 return 0


#             if dp[i][prev_i] != -1:
#                 return dp[i][prev_i]

#             pick = -float('inf')
#             if prev_i == n or nums[i] < nums[prev_i]:
#                 pick = 1 + calc(i-1,i)
            
#             npick = calc(i-1,prev_i)

#             dp[i][prev_i] = max(pick,npick)

#             return dp[i][prev_i]
        

#         return calc(n-1,n)

# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         """
#         This function returns the length of the longest increasing subsequence in the given array nums.
        
#         Args:
#         - nums: List[int]: A list of integers representing the sequence of numbers.
        
#         Returns:
#         - int: The length of the longest increasing subsequence.
#         """
        
#         n = len(nums)  # The length of the input list nums.

#         # The function calc recursively finds the length of the longest increasing subsequence ending at index i.
#         # prev_i represents the index of the previous element in the increasing subsequence.
#         def calc(i, prev_i):
#             """
#             Recursive helper function to compute the length of the longest increasing subsequence.

#             Args:
#             - i: int: The current index being considered in nums.
#             - prev_i: int: The index of the previous element included in the LIS.

#             Returns:
#             - int: The length of the longest increasing subsequence up to index i.
#             """

#             # Base case: If i is below 0, there are no elements left to consider.
#             if i < 0:
#                 return 0

#             # Option 1: Pick the current element if it forms an increasing sequence.
#             pick = -float('inf')  # Initialize with negative infinity to represent an invalid subsequence.
#             # We can pick the current element nums[i] if:
#             # - prev_i is out of bounds (meaning we haven't picked any element yet).
#             # - The current element nums[i] is less than the previous element nums[prev_i].
#             if prev_i == n or nums[i] < nums[prev_i]:
#                 pick = 1 + calc(i - 1, i)

#             # Option 2: Do not pick the current element.
#             npick = calc(i - 1, prev_i)

#             # Return the maximum value obtained from the two options.
#             return max(pick, npick)

#         # Start the recursion from the last element of the array with prev_i set to n (out of bounds).
#         return calc(n - 1, n)
