class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        n = len(grid)
        m = len(grid[0])

        dp = [[-1] * m for _ in range(n)]


        dp[0][0] = grid[0][0]

        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    continue
                up = left = float('inf') 
                if i>0:
                    up = dp[i-1][j]
                if j >0:
                    left = dp[i][j-1]
                dp[i][j] = grid[i][j] + min(up,left)
        
        return dp[n-1][m-1]
        


# class Solution:
#     def minPathSum(self, grid: List[List[int]]) -> int:

#         n = len(grid)
#         m = len(grid[0])

#         dp = [[-1] * m for _ in range(n)]
#         def calc(x,y):

#             if x == 0 and y == 0:
#                 return grid[x][y]
            
#             if x< 0  or y < 0 or x>= n or y >= m:
#                 return float('inf')
            
#             if dp[x][y] != -1:
#                 return dp[x][y]

#             up = calc(x-1,y)
#             left = calc(x,y-1)

#             dp[x][y] = grid[x][y] + min(up,left) 
#             return dp[x][y]
        
#         return calc(n-1,m-1)


# class Solution:
#     def minPathSum(self, grid: List[List[int]]) -> int:
#         """
#         This function calculates the minimum path sum from the top-left corner to the bottom-right corner
#         of a grid. The path can only move either down or right at any point in time.

#         Args:
#         - grid: A 2D list of integers representing the grid.

#         Returns:
#         - The minimum sum of the path from the top-left to the bottom-right of the grid.
#         """

#         # Get the number of rows and columns in the grid
#         n = len(grid)
#         m = len(grid[0])
        
#         def calc(x, y):
#             """
#             This recursive function calculates the minimum path sum to reach cell (x, y).

#             Args:
#             - x: Row index of the current cell.
#             - y: Column index of the current cell.

#             Returns:
#             - The minimum path sum to reach cell (x, y).
#             """

#             # Base case: If we are at the starting cell (0, 0), return its value
#             if x == 0 and y == 0:
#                 return grid[x][y]
            
#             # If the current cell is out of bounds, return a large number (infinity) to avoid considering this path
#             if x < 0 or y < 0 or x >= n or y >= m:
#                 return float('inf')

#             # Recursively calculate the minimum path sum from the top (cell above) and the left (cell to the left)
#             up = calc(x-1, y)
#             left = calc(x, y-1)
            
#             # Return the value of the current cell plus the minimum of the sums from the top and left
#             return grid[x][y] + min(up, left)
        
#         # Start the recursive calculation from the bottom-right corner of the grid
#         return calc(n-1, m-1)

        