class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:

        l =0
        n = len(nums)
        max_window = -1
        target = sum(nums) - x
        window = 0
        for r in range(n):
            window += nums[r]
            
            while l <= r and window >target:
                window -= nums[l]
                l+=1 

            if window == target:
                max_window = max(max_window, r - l + 1)
            
            

        return -1 if max_window== -1 else n - max_window 


        
        
        # n = len(nums)
        # prefix = [0] * (n+1)
        # rev_suffix = [0] * (n+1)
        # min_op = float("inf")
        # # start with one buffer zero

        # for i in range(1,n+1):
        #     prefix[i] = prefix[i-1] + nums[i-1]

        #     if prefix[i] == x:
        #         min_op = min(min_op,i)
        
        # for i in range(n-1,-1,-1):
        #     rev_suffix[n-i] = rev_suffix[n-i-1] + nums[i]

        #     if rev_suffix == x:
        #         min_op = min(min_op,n-i)

        
        # prefix_map = {prefix[i]: i for i in range(n+1)}

        # for i in range(n+1):
        #     remaining = x - rev_suffix[i]

        #     if remaining in prefix_map and prefix_map[remaining] + i <=n:
        #         min_op = min(min_op,i + prefix_map[remaining])

        
        # return min_op if min_op != float("inf") else -1

        
        
        
        
        
        
        
        
        
        # brute force
        
        
        # n = len(nums)
        # prefix = [0] * (n + 1)
        # suffix = [0] * (n + 1)
        # min_op = float('inf')  # Use inf to simplify min comparisons
        
        # # Compute prefix sums
        # for i in range(1, n + 1):
        #     prefix[i] = prefix[i - 1] + nums[i - 1]
        #     if prefix[i] == x:
        #         min_op = min(min_op, i)
        
        # # Compute reverse suffix sums
        # for i in range(n - 1, -1, -1):
        #     suffix[n - i] = suffix[n - i - 1] + nums[i]
        #     if suffix[n - i] == x:
        #         min_op = min(min_op, n - i)
        
        # # Check for combinations of prefix and suffix sums
        # prefix_map = {prefix[i]: i for i in range(n + 1)}  # Mapping sum to index
        # for j in range(n + 1):
        #     remaining = x - suffix[j]
        #     if remaining in prefix_map and prefix_map[remaining] + j <= n:
        #         min_op = min(min_op, prefix_map[remaining] + j)
        
        # return min_op if min_op != float('inf') else -1
