class Solution:
    def dfs(self, grid, i, j, val, color):
        # Base case: if the current cell is out of bounds or not equal to the original color
        if i < 0 or j < 0 or i >= self.rows or j >= self.cols or self.visited[i][j] or grid[i][j] != val:
            return 
        # Change the color of the current cell to the target color
        self.visited[i][j] = True
    
        # Recursively call dfs for all 4 directions
        self.dfs(grid, i + 1, j, val, color)  # Move down
        self.dfs(grid, i - 1, j, val, color)  # Move up
        self.dfs(grid, i, j + 1, val, color)  # Move right
        self.dfs(grid, i, j - 1, val, color)  # Move left
    
    def border_surr(self,i,j):
        if i == 0 or j ==0  or i == self.rows -1 or j == self.cols -1:
            return True
        
        u = self.visited[i+1][j]
        d = self.visited[i-1][j]
        l = self.visited[i][j-1]
        r = self.visited[i][j+1]
        if u and d and l and r:
            return False
        return True
    

    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:

        self.rows = len(grid)
        self.cols = len(grid[0])
        self.visited = [[False for _ in range(self.cols)] for _ in range(self.rows) ]
        self.dfs(grid,row,col,grid[row][col],color)

        for i in range(self.rows):
            for j in range(self.cols):
                if self.visited[i][j] and self.border_surr(i,j):
                    grid[i][j] = color
        

        return grid