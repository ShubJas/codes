class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
   
        self.rows = len(grid)
        self.cols = len(grid[0])

        q = collections.deque()
        if self.rows == 1 and self.cols== 1 and grid[0][0] == 0:
            return 1


        for i in [-1,1]:
            for j in [-1,1]:
                q.append((i,j))
        for i in [-1,1]:
            q.append((i,0))
        for j in [-1,1]:
            q.append((0,j))
        
        print(q)

        visited = [[False for _ in range(self.cols)] for _ in range(self.rows)]
        visited[0][0] = True
        step = 0
        while q:
            step+=1
            qlen = len(q)

            for _ in range(qlen):
                i , j = q.popleft()
                
                if 0 <= i < self.rows and 0 <=j < self.cols and not visited[i][j] and grid[i][j] == 0:
                    if i == self.rows -1 and j == self.cols - 1:
                        return step + 1
                    visited[i][j] = True
                    q.append((i+1,j+1)) 
                    q.append((i-1,j-1)) 
                    q.append((i-1,j+1)) 
                    q.append((i+1,j-1)) 
                    q.append((i+1,j)) 
                    q.append((i-1,j)) 
                    q.append((i,j+1)) 
                    q.append((i,j-1)) 
        return -1

