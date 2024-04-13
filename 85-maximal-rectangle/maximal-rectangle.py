class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        # Initialize the histogram matrix with the same dimensions as the input matrix.
        # The histogram matrix will store heights of consecutive '1's in each column.
        n, m = len(matrix), len(matrix[0])
        hist = [[0] * m for _ in range(n)]
        
        # Fill the histogram matrix based on the input matrix.
        for j in range(m):
            for i in range(n):
                if matrix[i][j] == '1':
                    hist[i][j] = hist[i-1][j] + 1 if i != 0 else 1

        # Function to find the maximum area of a rectangle in a histogram.
        def largestRectangleArea(heights):
            maxArea = 0
            stack = []
            for i, h in enumerate(heights + [0]):
                while stack and heights[stack[-1]] > h:
                    height = heights[stack.pop()]
                    width = i if not stack else i - stack[-1] - 1
                    maxArea = max(maxArea, height * width)
                stack.append(i)
            return maxArea
        
        # For each row in the histogram matrix, find the maximum area of a rectangle
        # and update maxArea accordingly.
        maxArea = 0
        for row in hist:
            maxArea = max(maxArea, largestRectangleArea(row))
        
        return maxArea
