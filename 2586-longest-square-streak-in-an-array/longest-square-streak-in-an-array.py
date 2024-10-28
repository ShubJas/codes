class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        
        # Step 1: Sort the list to ensure we process smaller numbers first
        # This way, we can use previously computed results in our hashmap for square roots
        nums.sort()
        
        # Step 2: Initialize a hashmap to keep track of the length of the longest square streak
        # for each number. `hm[x]` will store the streak length ending at `x`.
        hm = {}
        
        # Initialize `result` with -1 to keep track of the maximum streak length found.
        # If no square streak is found, we'll return -1 as per problem requirements.
        result = -1
        
        # Step 3: Iterate over each number in the sorted list `nums`
        for x in nums:

            # Calculate the integer square root of `x`
            root = math.isqrt(x)  # `math.isqrt(x)` returns the integer part of the square root of `x`
            
            # Step 4: Check if `x` is a perfect square and if its root exists in `nums`
            # `root * root == x` confirms that `x` is a perfect square
            # `root in nums` checks that the root of `x` is in the list and has been processed
            if root * root == x and root in hm:
                
                # If `x` is a square and `root` is in the hashmap,
                # update the streak count for `x` as `hm[root] + 1`
                hm[x] = hm[root] + 1
                
                # Update `result` to be the maximum streak length seen so far
                result = max(hm[x], result)
            
            else:
                # If `x` is not a square with an existing root in `hm`,
                # initialize the streak length for `x` as 1 (it starts its own streak)
                hm[x] = 1

        # Step 5: Return the maximum square streak length found, or -1 if none was found
        return result
