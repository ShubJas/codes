class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        n = len(height)
        maxleft = [0] * n
        maxright = [0] * n
        total = 0

        # Fill maxleft array
        maxleft[0] = height[0]
        for i in range(1, n):
            maxleft[i] = max(maxleft[i-1], height[i])

        # Fill maxright array
        maxright[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            maxright[i] = max(maxright[i+1], height[i])

        # Calculate total trapped water
        for i in range(n):
            # The trapped water at each bar is the minimum of max heights from both sides minus its own height
            total += min(maxleft[i], maxright[i]) - height[i]

        return total

        # total = 0

        # for i in range(1,len(height)-1):

        #     curr = min(max(height[:i]),max(height[i+1:])) - height[i] 
        #     curr = curr if curr > 0 else 0
        #     # print(curr)

        #     total+=curr

        #     # print(total)
        # return total

        
        