class Solution:
    def dfs(self,grid,i,j):

        if i < 0 or j<0 or i>=self.rows or j>=self.cols or grid[i][j] == 1:
            return
        
        
        grid[i][j] = 1
        
        self.dfs(grid, i + 1, j)  # Move down
        self.dfs(grid, i - 1, j)  # Move up
        self.dfs(grid, i, j + 1)  # Move right
        self.dfs(grid, i, j - 1)  # Move left
        

    def closedIsland(self, grid: List[List[int]]) -> int:


        self.rows = len(grid)
        self.cols = len(grid[0])

        for i in range(self.rows):
            for j in range(self.cols):
                if i == 0 or j == 0 or i == self.rows-1 or j == self.cols-1:
                    self.dfs(grid,i,j)
        islands = 0
        for i in range(self.rows):
            for j in range(self.cols):
                if grid[i][j] == 0:
                    self.dfs(grid,i,j)
                    islands +=1
        
        return islands

        