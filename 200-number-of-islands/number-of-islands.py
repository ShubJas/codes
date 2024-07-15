class Solution:
    def dfs(self, grid, i, j, visited):
        # Base case: if the current cell is out of bounds, contains '0' (water), or has been visited, return
        if i < 0 or j < 0 or i >= self.rows or j >= self.cols or grid[i][j] == "0" or visited[i][j]:
            return
        
        # Mark the current cell as visited
        visited[i][j] = True

        # Recursively call DFS for all four directions (down, up, right, left)
        self.dfs(grid, i + 1, j, visited)  # Move down
        self.dfs(grid, i - 1, j, visited)  # Move up
        self.dfs(grid, i, j + 1, visited)  # Move right
        self.dfs(grid, i, j - 1, visited)  # Move left

    def numIslands(self, grid: List[List[str]]) -> int:
        # Get the number of rows and columns in the grid
        self.rows = len(grid)
        self.cols = len(grid[0])

        # Initialize a visited matrix of the same size as the grid with all False values
        visited = [[False for _ in range(self.cols)] for _ in range(self.rows)]

        # Initialize the counter for the number of islands
        islands = 0

        # Iterate over each cell in the grid
        for i in range(self.rows):
            for j in range(self.cols):
                # If the cell contains land ('1') and has not been visited, perform DFS
                if grid[i][j] == "1" and not visited[i][j]:
                    self.dfs(grid, i, j, visited)  # Perform DFS to mark all connected land cells
                    islands += 1  # Increment the island counter after a complete DFS traversal
        
        # Return the total number of islands
        return islands


# class Solution:
#     def dfs(self, grid, i, j):
#         # Base case: if the current cell is out of bounds, contains '0' (water), or has been visited, return
#         if i < 0 or j < 0 or i >= self.rows or j >= self.cols or grid[i][j] == "0":
#             return
        
#         # Mark the current cell as visited
#         grid[i][j] = "0"

#         # Recursively call DFS for all four directions (down, up, right, left)
#         self.dfs(grid, i + 1, j)  # Move down
#         self.dfs(grid, i - 1, j)  # Move up
#         self.dfs(grid, i, j + 1)  # Move right
#         self.dfs(grid, i, j - 1)  # Move left

#     def numIslands(self, grid: List[List[str]]) -> int:
#         # Get the number of rows and columns in the grid
#         self.rows = len(grid)
#         self.cols = len(grid[0])

#         # Initialize a visited matrix of the same size as the grid with all False values
#         # visited = [[False for _ in range(self.cols)] for _ in range(self.rows)]

#         # Initialize the counter for the number of islands
#         islands = 0

#         # Iterate over each cell in the grid
#         for i in range(self.rows):
#             for j in range(self.cols):
#                 # If the cell contains land ('1') and has not been visited, perform DFS
#                 if grid[i][j] == "1":
#                     self.dfs(grid, i, j)  # Perform DFS to mark all connected land cells
#                     islands += 1  # Increment the island counter after a complete DFS traversal
        
#         # Return the total number of islands
#         return islands

