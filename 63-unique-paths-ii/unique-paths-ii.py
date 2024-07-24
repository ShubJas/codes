class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])

        if obstacleGrid[n-1][m-1] == 1 or obstacleGrid[0][0] == 1:
            return 0


        prev = [-1] * m 
        
        # this may set the 
        prev[0] = 1

        for i in range(n):
            curr = [-1] * m
            for j in range(m):
                if i == 0 and j == 0:
                    curr[0] = 1
                    continue
                up = left = 0
                if i>0 and obstacleGrid[i-1][j] != 1:
                    up = prev[j]
                if j>0 and obstacleGrid[i][j-1] != 1:
                    left = curr[j-1]
                
                curr[j] = left + up
            prev = curr
        return prev[m-1]

# class Solution:
#     def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
#         n = len(obstacleGrid)
#         m = len(obstacleGrid[0])

#         if obstacleGrid[n-1][m-1] == 1 or obstacleGrid[0][0] == 1:
#             return 0


#         dp = [[-1] * m for _ in range(n)]

#         dp[0][0] = 1

#         for i in range(n):
#             for j in range(m):
#                 if i == 0 and j == 0:
#                     continue
#                 up = left = 0
#                 if i>0 and obstacleGrid[i-1][j] != 1:
#                     up = dp[i-1][j]
#                 if j>0 and obstacleGrid[i][j-1] != 1:
#                     left = dp[i][j-1]
                
#                 dp[i][j] = left + up
        
#         return dp[n-1][m-1]

# class Solution:
#     def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
#         n = len(obstacleGrid)
#         m = len(obstacleGrid[0])

#         if obstacleGrid[n-1][m-1] == 1 or obstacleGrid[0][0] == 1:
#             return 0


#         dp = [[-1] * m for _ in range(n)]

#         def calc(x,y):

#             if x<0 or x>=n or y<0 or y>=m or obstacleGrid[x][y] == 1:
#                 return 0
            
#             if x == 0 and y==0:
#                 return 1
            
#             if dp[x][y] != -1:
#                 return dp[x][y]
            
#             up = calc(x-1,y)
#             left = calc(x,y-1)
            
#             dp[x][y] = up + left
#             return dp[x][y] 
        
#         return calc(n-1,m-1)


# class Solution:
#     def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
#         """
#         Approach:
#         - This function calculates the number of unique paths from the top-left corner to the 
#           bottom-right corner of a grid with obstacles. 
#         - The grid is represented by a 2D list 'obstacleGrid' where a 1 represents an obstacle 
#           and a 0 represents an empty cell.
#         - The approach uses recursion to explore all possible paths from the top-left to 
#           the bottom-right corner, and it avoids paths that hit an obstacle.
#         - The base cases handle the out-of-bounds conditions, obstacles, and the starting cell.
#         - The recursive case sums the results of the paths from the top and left cells.
#         - This approach does not use memoization, which makes it inefficient for large grids due 
#           to overlapping subproblems.

#         Args:
#         - obstacleGrid: List[List[int]]: A 2D list representing the grid with obstacles.

#         Returns:
#         - int: The number of unique paths from the top-left to the bottom-right corner.
#         """
        
#         n = len(obstacleGrid)      # Number of rows in the grid
#         m = len(obstacleGrid[0])   # Number of columns in the grid

#         # If the bottom-right cell is an obstacle, return 0 as there's no path
#         if obstacleGrid[n-1][m-1] == 1:
#             return 0

#         def calc(x, y):
#             """
#             Recursive helper function to calculate the number of unique paths to the cell (x, y).
            
#             Args:
#             - x: int: The row index of the current cell.
#             - y: int: The column index of the current cell.
            
#             Returns:
#             - int: The number of unique paths to the cell (x, y).
#             """
            
#             # Base case: If the current cell is out of bounds or an obstacle, return 0
#             if x < 0 or x >= n or y < 0 or y >= m or obstacleGrid[x][y] == 1:
#                 return 0
            
#             # Base case: If the current cell is the starting cell (0, 0), return 1
#             if x == 0 and y == 0:
#                 return 1
            
#             # Recursive case: Calculate the number of unique paths from the top and left cells
#             up = calc(x - 1, y)   # Number of unique paths from the cell above
#             left = calc(x, y - 1) # Number of unique paths from the cell to the left

#             # Sum the results of the paths from the top and left cells
#             return up + left
        
#         # Calculate the number of unique paths to the bottom-right cell (n-1, m-1)
#         return calc(n - 1, m - 1)
