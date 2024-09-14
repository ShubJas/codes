class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxL = 0  # This will store the maximum length of subarray
        i = 0
        maxi = max(nums)  # Find the maximum value in the array
        n = len(nums)

        while i < n:
            count = 0
            # Skip elements until you find the maximum value
            while i < n and nums[i] != maxi:
                i += 1
            # Count the length of the subarray where elements are equal to `maxi`
            while i < n and nums[i] == maxi:
                count += 1
                i += 1
            # Update the maximum length found
            maxL = max(maxL, count)
        
        return maxL

                
            