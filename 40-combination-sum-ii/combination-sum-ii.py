class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        n = len(candidates)
        result = []
        candidates.sort()  # Sort the candidates to handle duplicates

        def backtrack(S, i, stack):
            # Base case: if the current sum equals the target, add a copy of the current stack to the result
            if S == target:
                result.append(stack[:])  # Make a deep copy of stack to avoid reference issues
                return
            
            # If the sum exceeds the target or we've considered all candidates, return
            if i == n or S > target:
                return

            # Iterate through the candidates starting from the current index `i`
            for j in range(i, n):
                # Skip duplicates to ensure unique combinations
                if j > i and candidates[j] == candidates[j - 1]:
                    continue

                # If adding the current candidate exceeds the target, break the loop
                if S + candidates[j] > target:
                    break

                # Include the current candidate and move to the next candidate
                stack.append(candidates[j])
                backtrack(S + candidates[j], j + 1, stack)  # Move to the next index (j+1)
                stack.pop()  # Backtrack by removing the last candidate
        
        backtrack(0, 0, [])

        return result
