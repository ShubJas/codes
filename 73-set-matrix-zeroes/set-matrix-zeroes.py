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
