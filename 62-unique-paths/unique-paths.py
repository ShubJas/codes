class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1]* m for _ in range(n)]
        def calc(x, y):
            # Base case: If the cell is out of bounds, there are no paths.
            if x < 0 or x >= n or y < 0 or y >= m:
                return 0

            if dp[x][y] != -1:
                return dp[x][y]
                
            # Base case: If we are at the top-left corner, there's exactly one path to this cell.
            if x == 0 and y == 0:
                return 1

            # Recursive case: Calculate the number of paths from the cell above and the cell to the left.
            paths_from_above = calc(x - 1, y)
            paths_from_left = calc(x, y - 1)


            dp[x][y] = paths_from_above + paths_from_left
            # The total number of paths to the current cell is the sum of the paths from above and from the left.
            return dp[x][y]

        # Start the recursion from the bottom-right corner.
        return calc(n - 1, m - 1)

        