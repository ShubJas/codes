#  See take u forward 3 solutions
#  Space optimized (only one var)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])

        # Variable to track if the first column should be set to zero
        cextra = 1
        
        # First pass: Use first row and column as markers
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    if j == 0:
                        cextra = 0  # Mark that the first column should be zeroed
                    else:
                        matrix[0][j] = 0  # Mark that the j-th column should be zeroed
                    matrix[i][0] = 0  # Mark that the i-th row should be zeroed
        
        # Second pass: Set matrix elements to zero based on markers, skipping first row/column for now
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Handle the first row separately (if any zero was marked in the first row)
        if matrix[0][0] == 0:
            for j in range(1, col):
                matrix[0][j] = 0

        # Handle the first column separately
        if cextra == 0:
            for i in range(row):
                matrix[i][0] = 0

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])

        # Use sets to keep track of rows and columns that need to be zeroed
        zero_rows = set()
        zero_cols = set()

        # First pass: Identify the rows and columns that should be zeroed
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)

        # Second pass: Zero out the identified rows and columns
        for i in range(row):
            for j in range(col):
                if i in zero_rows or j in zero_cols:
                    matrix[i][j] = 0

