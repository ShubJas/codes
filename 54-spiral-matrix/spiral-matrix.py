class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        # Initialize the boundaries for the matrix traversal
        left = top = 0  # `left` is the left boundary, `top` is the top boundary
        right = len(matrix[0]) - 1  # `right` is the right boundary, initialized to the last column index
        bottom = len(matrix) - 1  # `bottom` is the bottom boundary, initialized to the last row index
        result = []  # This list will store the elements in spiral order

        # Continue looping until the boundaries overlap
        while left <= right and top <= bottom:

            # Traverse from left to right across the top boundary (row `top`)
            for j in range(left, right + 1):
                result.append(matrix[top][j])  # Add each element in the top row to the result list
            top += 1  # Move the top boundary down after processing the top row

            # Traverse from top to bottom along the right boundary (column `right`)
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])  # Add each element in the right column to the result list
            right -= 1  # Move the right boundary left after processing the right column

            # Check if there are rows remaining to process (if `top` hasn't crossed `bottom`)
            if bottom >= top:
                # Traverse from right to left across the bottom boundary (row `bottom`)
                for j in range(right, left - 1, -1):
                    result.append(matrix[bottom][j])  # Add each element in the bottom row to the result list
                bottom -= 1  # Move the bottom boundary up after processing the bottom row

            # Check if there are columns remaining to process (if `left` hasn't crossed `right`)
            if left <= right:
                # Traverse from bottom to top along the left boundary (column `left`)
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])  # Add each element in the left column to the result list
                left += 1  # Move the left boundary right after processing the left column

        # After the loop, the result list contains all elements of the matrix in spiral order
        return result
