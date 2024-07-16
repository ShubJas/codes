class Solution:
    def dfs(self, grid, i, j, val, color):
        # Base case: if the current cell is out of bounds, already visited, or not equal to the original color
        if i < 0 or j < 0 or i >= self.rows or j >= self.cols or self.visited[i][j] or grid[i][j] != val:
            return 
        # Mark the current cell as visited
        self.visited[i][j] = True
    
        # Recursively call dfs for all 4 directions (down, up, right, left)
        self.dfs(grid, i + 1, j, val, color)  # Move down
        self.dfs(grid, i - 1, j, val, color)  # Move up
        self.dfs(grid, i, j + 1, val, color)  # Move right
        self.dfs(grid, i, j - 1, val, color)  # Move left
    
    def border_surr(self, i, j):
        # If the cell is on the border of the grid, it is a border cell
        if i == 0 or j == 0 or i == self.rows - 1 or j == self.cols - 1:
            return True
        
        # Check if any of the 4 adjacent cells are not visited, indicating a border cell
        u =  self.visited[i - 1][j]
        d =  self.visited[i + 1][j]
        l =  self.visited[i][j - 1]
        r =  self.visited[i][j + 1]
        
        # If all adjacent cells are visited, it is not a border cell
        if u and d and l and r:
            return False
        return True

    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        # Initialize the number of rows and columns
        self.rows = len(grid)
        self.cols = len(grid[0])
        # Initialize a visited matrix to keep track of visited cells
        self.visited = [[False for _ in range(self.cols)] for _ in range(self.rows)]
        
        # Perform DFS to mark all cells in the connected component starting from (row, col)
        self.dfs(grid, row, col, grid[row][col], color)

        # Iterate over all cells to apply the new color to the border cells
        for i in range(self.rows):
            for j in range(self.cols):
                # Check if the cell is visited and is a border cell
                if self.visited[i][j] and self.border_surr(i, j):
                    # Change the color of the border cell
                    grid[i][j] = color
        
        return grid
