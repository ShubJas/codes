class Solution:
    def dfs(self,grid,i,j):
        if i<0 or j<0 or i >=self.rows or j >=self.cols or grid[i][j]==0:
            return 0
        grid[i][j] = 0
        u = self.dfs(grid,i+1,j)
        d = self.dfs(grid,i-1,j)
        l = self.dfs(grid,i,j+1)
        r = self.dfs(grid,i,j-1)
        return 1 + u + d + l + r 
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        self.rows = len(grid)
        self.cols = len(grid[0])

        maxA = 0
        for i in range(self.rows):
            for j in range(self.cols):
                if grid[i][j] == 1:
                    maxA = max(maxA,self.dfs(grid,i,j))
        return maxA