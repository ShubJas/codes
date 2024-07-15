class Solution:
    def dfs(self,grid,i,j,visited):

        if i<0 or j<0 or i >= self.rows or j >= self.cols or grid[i][j] =="0" or visited[i][j]:
            return
        
        visited[i][j] = True

        self.dfs(grid,i+1,j,visited)
        self.dfs(grid,i-1,j,visited)
        self.dfs(grid,i,j+1,visited)
        self.dfs(grid,i,j-1,visited)

    def numIslands(self, grid: List[List[str]]) -> int:

        self.rows = len(grid)
        self.cols = len(grid[0])


        visited = [[False for _ in range(self.cols)] for _ in range(self.rows)]
        islands = 0
        for i in range(self.rows):
            for j in range(self.cols):

                if grid[i][j] == "1" and not visited[i][j]:
                    self.dfs(grid,i,j,visited)
                    islands +=1
        
        return islands


        