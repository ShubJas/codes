class Solution:
    def dfs(self, grid, i, j):
        # Check if the current cell is out of bounds or water (0)
        if i < 0 or j < 0 or i >= self.rows or j >= self.cols or grid[i][j] == 0:
            return 0
        
        # Mark the current cell as visited by setting it to 0
        grid[i][j] = 0
        
        # Recursively visit all 4 directions (up, down, left, right) and sum up the areas
        u = self.dfs(grid, i + 1, j)  # Move down
        d = self.dfs(grid, i - 1, j)  # Move up
        l = self.dfs(grid, i, j + 1)  # Move right
        r = self.dfs(grid, i, j - 1)  # Move left
        
        # Return the total area of the island including the current cell
        return 1 + u + d + l + r 
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Initialize the number of rows and columns in the grid
        self.rows = len(grid)
        self.cols = len(grid[0])

        # Initialize the variable to store the maximum area of an island found
        maxA = 0

        # Iterate over each cell in the grid
        for i in range(self.rows):
            for j in range(self.cols):
                # If the cell is land (1), perform DFS to find the area of the island
                if grid[i][j] == 1:
                    # Update the maximum area if the current island's area is larger
                    maxA = max(maxA, self.dfs(grid, i, j))
        
        # Return the maximum area of an island found
        return maxA

# class Solution:
#     def dfs(self, grid, i, j):
#         # Base case: if the current cell is out of bounds or already computed
#         if i < 0 and j < 0 and i >= self.rows and j >= self.cols and self.memo[i][j] != -1:
#             return self.memo[i][j]

#         # If the current cell is out of bounds or water (0)
#         if i < 0 or j < 0 or i >= self.rows or j >= self.cols or grid[i][j] == 0:
#             return 0
        
#         # Mark the current cell as visited by setting it to 0
#         grid[i][j] = 0

#         # Recursively visit all 4 directions (up, down, left, right) and sum up the areas
#         u = self.dfs(grid, i + 1, j)  # Move down
#         d = self.dfs(grid, i - 1, j)  # Move up
#         l = self.dfs(grid, i, j + 1)  # Move right
#         r = self.dfs(grid, i, j - 1)  # Move left

#         # Store the result in memoization table to avoid recomputation
#         self.memo[i][j] = 1 + u + d + l + r

#         # Return the total area of the island including the current cell
#         return self.memo[i][j]
    
#     def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
#         # Initialize the number of rows and columns in the grid
#         self.rows = len(grid)
#         self.cols = len(grid[0])

#         # Initialize a memoization table to store already computed results
#         self.memo = [[-1 for _ in range(self.cols)] for _ in range(self.rows)] 

#         # Initialize the variable to store the maximum area of an island found
#         maxA = 0

#         # Iterate over each cell in the grid
#         for i in range(self.rows):
#             for j in range(self.cols):
#                 # If the cell is land (1), perform DFS to find the area of the island
#                 if grid[i][j] == 1:
#                     # Update the maximum area if the current island's area is larger
#                     maxA = max(maxA, self.dfs(grid, i, j))

#         # Return the maximum area of an island found
#         return maxA
