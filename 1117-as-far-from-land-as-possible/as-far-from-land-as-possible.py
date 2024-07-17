class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:


        self.rows = len(grid)
        self.cols = len(grid[0])
        
        q = collections.deque()

        for i in range(self.rows):
            for j in range(self.cols):
                if grid[i][j] == 1:
                    q.append((i+1,j))
                    q.append((i-1,j))
                    q.append((i,j+1))
                    q.append((i,j-1))
        
        step = 0
        # maxS = 0
        visited = [[False for _ in range(self.cols)] for _ in range(self.rows)]
        while q:
            step +=1
            qlen = len(q)
            for _ in range(qlen):
                # print(q[0])
                i , j  = q.popleft()

                if 0 <= i < self.rows and 0 <= j < self.cols and not visited[i][j] and grid[i][j] != 1:
                    # maxS = max()
                    print(i)  
                    visited[i][j] =  True   
                    q.append((i+1,j))
                    q.append((i-1,j))
                    q.append((i,j+1))
                    q.append((i,j-1))

        return step - 1 if step > 1 else -1

        