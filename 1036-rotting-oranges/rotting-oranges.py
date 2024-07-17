class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:



        self.rows = len(grid)
        self.cols = len(grid[0])


        q = collections.deque()

        for i in range(self.rows):
            for j in range(self.cols):
                if grid[i][j] == 2:
                    q.append((i+1,j))
                    q.append((i-1,j))
                    q.append((i,j+1))
                    q.append((i,j-1))
        

        visited = [[False for _ in range(self.cols)] for _ in range(self.rows)]
        minutes = 0
        while q:
            minutes +=1
            qlen = len(q)
            for _ in range(qlen):
                i , j = q.popleft()

                if  0<=i< self.rows and 0 <= j < self.cols and  not visited[i][j] and grid[i][j] == 1:
                    grid[i][j] = 2

                    visited[i][j] = True
                    q.append((i+1,j))
                    q.append((i-1,j))
                    q.append((i,j+1))
                    q.append((i,j-1))
        

        for i in range(self.rows):
            for j in range(self.cols):
                if grid[i][j] == 1:
                    return -1
        if minutes == 0:
            return 0
        return minutes -1