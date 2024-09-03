class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)  # Determine the length of the input list `nums`
        result = []  # This will store all the generated permutations

        # Define a helper function for backtracking
        def backtrack(i):
            # Base case: If we've reached the end of the array, add the current permutation to the result
            if i == n:
                result.append(nums[:])  # Append a deep copy of the current permutation to `result`
                return

            # Iterate through the array starting from index `i`
            for j in range(i, n):
                # Swap the current element `nums[i]` with `nums[j]` to explore a new permutation
                nums[i], nums[j] = nums[j], nums[i]

                # Recurse by moving to the next index (`i + 1`)
                backtrack(i + 1)

                # Backtrack: Swap the elements back to their original positions to restore the array
                nums[i], nums[j] = nums[j], nums[i]

        # Start the backtracking process from the first index (0)
        backtrack(0)
        
        # Return the list of all generated permutations
        return result
