class Solution:
    def dfs(self, grid, i, j):
        # Base case: if the current cell is out of bounds or already visited (1), return
        if i < 0 or j < 0 or i >= self.rows or j >= self.cols or grid[i][j] == 1:
            return

        # Mark the current cell as visited by setting it to 1
        grid[i][j] = 1

        # Recursively call DFS for all four directions (down, up, right, left)
        self.dfs(grid, i + 1, j)  # Move down
        self.dfs(grid, i - 1, j)  # Move up
        self.dfs(grid, i, j + 1)  # Move right
        self.dfs(grid, i, j - 1)  # Move left

    def closedIsland(self, grid: List[List[int]]) -> int:
        # Get the number of rows and columns in the grid
        self.rows = len(grid)
        self.cols = len(grid[0])

        # Step 1: Flood fill all '0's connected to the borders to mark them as '1'
        for i in range(self.rows):
            for j in range(self.cols):
                # If the cell is on the border and is a '0', perform DFS to mark all connected cells
                if i == 0 or j == 0 or i == self.rows - 1 or j == self.cols - 1:
                    self.dfs(grid, i, j)

        # Step 2: Count the number of closed islands
        islands = 0
        for i in range(self.rows):
            for j in range(self.cols):
                # If the cell is a '0', it's part of a closed island
                if grid[i][j] == 0:
                    self.dfs(grid, i, j)  # Perform DFS to mark all connected cells
                    islands += 1  # Increment the closed island counter

        return islands