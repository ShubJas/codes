class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Get the number of rows and columns in the matrix
        rows = len(matrix)
        if rows == 0:
            return False
        cols = len(matrix[0])

        # Step 1: Binary Search to find the correct row where the target might be present
        top = 0
        bottom = rows - 1

        while top <= bottom:
            midr = (top + bottom) // 2
            # Check if the target lies within the current row
            if matrix[midr][0] <= target <= matrix[midr][-1]:
                # Step 2: Binary search within the identified row to find the target
                l, r = 0, cols - 1
                while l <= r:
                    mid = (l + r) // 2
                    if matrix[midr][mid] == target:
                        return True
                    elif matrix[midr][mid] < target:
                        l = mid + 1
                    else:
                        r = mid - 1
                return False
            elif target < matrix[midr][0]:
                bottom = midr - 1
            else:
                top = midr + 1

        return False
