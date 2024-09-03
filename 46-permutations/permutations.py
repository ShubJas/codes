class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        # Define a helper function for backtracking
        def backtrack(start):
            # If we've reached the end of the array, add the current permutation to the result
            if start == len(nums):
                result.append(nums[:])  # Make a deep copy since nums will be modified
                return
            
            # Iterate through the array and swap elements to generate permutations
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]  # Swap to place nums[i] at position start
                backtrack(start + 1)  # Recur with the next position
                nums[start], nums[i] = nums[i], nums[start]  # Swap back to restore the original order
        
        # Start backtracking from the first position
        backtrack(0)
        return result
