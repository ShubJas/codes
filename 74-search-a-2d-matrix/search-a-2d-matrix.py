class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        row_first, row_last = 0, len(matrix) - 1

        while row_first <= row_last:
            row_mid = (row_first + row_last) // 2
            # Directly start binary search in the potential row.
            l, r = 0, len(matrix[0]) - 1
            
            while l <= r:
                m = (l + r) // 2
                if matrix[row_mid][m] == target:
                    return True
                elif matrix[row_mid][m] < target:
                    l = m + 1
                else:
                    r = m - 1

            # Update row search boundaries based on comparison with the first and last elements of the mid row.
            if target > matrix[row_mid][-1]:
                row_first = row_mid + 1
            else:
                row_last = row_mid - 1
        
        return False
