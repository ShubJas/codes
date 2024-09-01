class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []

        def backtrack(i, stack):
            # Base case: If we've considered all elements
            if i == n:
                result.append(stack[:])  # Append a copy of the current stack
                return
            
            # Include the current element
            stack.append(nums[i])
            backtrack(i + 1, stack)

            # Exclude the current element
            stack.pop()
            backtrack(i + 1, stack)

        # Start backtracking from index 0 with an empty stack
        backtrack(0, [])
        
        return result
