class Solution:
    def dfs(self,i,j,visited,heights):

        visited.add((i,j))

        
        for (x,y) in [(1,0),(0,1),(-1,0),(0,-1)]:
            dx = i + x
            dy = j + y
            if 0 <= dx<self.rows and 0<=dy<self.cols and (dx,dy) not in visited and heights[dx][dy] >= heights[i][j]:
                self.dfs(dx,dy,visited,heights)


 
        
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        self.rows = len(heights)
        self.cols = len(heights[0])

        pacific = set()
        atlantic = set()

        for i in range(self.rows):
            self.dfs(i,0,pacific,heights)
            self.dfs(i,self.cols-1,atlantic,heights)
        
        
        for j in range(self.cols):
            self.dfs(0,j,pacific,heights)
            self.dfs(self.rows-1,j,atlantic,heights)




        result = list(pacific & atlantic)
        
        
        return result
