class Solution:
    def dfs(self, grid, i, j):
        # Base case for the DFS: If out of bounds or if the cell is not land
        if i < 0 or j < 0 or i >= self.rows or j >= self.cols or grid[i][j] != 1:
            return
        
        # Mark the cell as visited by setting it to -1
        grid[i][j] = -1

        # Explore all four directions
        self.dfs(grid, i + 1, j)  # Down
        self.dfs(grid, i - 1, j)  # Up
        self.dfs(grid, i, j + 1)  # Right
        self.dfs(grid, i, j - 1)  # Left

    def numEnclaves(self, grid: List[List[int]]) -> int:
        self.rows = len(grid)
        self.cols = len(grid[0])

        # Perform DFS for all the boundary cells to mark all connected lands
        for i in range(self.rows):
            for j in range(self.cols):
                if i == 0 or j == 0 or i == self.rows - 1 or j == self.cols - 1:
                    self.dfs(grid, i, j)
        
        # Count the remaining land cells that are not connected to the boundary
        count = 0
        for i in range(self.rows):
            for j in range(self.cols):
                if grid[i][j] == 1:
                    count += 1    
        
        return count
