class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        suffix = [0] * (n + 1)
        min_op = float('inf')  # Use inf to simplify min comparisons
        
        # Compute prefix sums
        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] + nums[i - 1]
            if prefix[i] == x:
                min_op = min(min_op, i)
        
        # Compute suffix sums
        for i in range(n - 1, -1, -1):
            suffix[n - i] = suffix[n - i - 1] + nums[i]
            if suffix[n - i] == x:
                min_op = min(min_op, n - i)
        
        # Check for combinations of prefix and suffix sums
        prefix_map = {prefix[i]: i for i in range(n + 1)}  # Mapping sum to index
        for j in range(n + 1):
            remaining = x - suffix[j]
            if remaining in prefix_map and prefix_map[remaining] + j <= n:
                min_op = min(min_op, prefix_map[remaining] + j)
        
        return min_op if min_op != float('inf') else -1
