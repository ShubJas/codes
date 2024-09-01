class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        # This will store all the unique subsets
        result = []
        # Length of the input list
        n = len(nums)

        # Sort the input list to ensure duplicates are adjacent
        # This allows the algorithm to easily skip over duplicates later
        nums.sort()

        def backtrack(i, stack):
            # Base case: If we've considered all elements
            if i == n:
                # Add a copy of the current stack to the result
                # Using stack[:] to make a shallow copy to avoid reference issues
                result.append(stack[:])
                return

            # Include the current element in the subset
            stack.append(nums[i])
            # Recur to include the next element
            backtrack(i + 1, stack)

            # Backtrack: Remove the last element to explore subsets without the current element
            stack.pop()

            # Move to the next unique element to avoid duplicates in the result
            i += 1
            # Skip over any duplicate elements to avoid creating duplicate subsets
            while i < n and nums[i] == nums[i - 1]:
                i += 1

            # Recur to explore the subsets without including the current element
            backtrack(i, stack)
        
        # Start the backtracking with an empty subset
        backtrack(0, [])
        
        return result
