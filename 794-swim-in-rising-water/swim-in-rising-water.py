class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        pq = [(grid[0][0],0,0)]

        n = len(grid)
        m = len(grid[0])
        visited = [[False] * m for _ in range(n)]
        while pq:

            time , x , y = heapq.heappop(pq)

            if x == n-1 and y == m-1:
                return time

            for nx , ny in [(x+1,y),(x,y+1),(x-1,y),(x,y-1)]:
                if 0<= nx <n and 0 <= ny < m and not visited[nx][ny]: 
                    visited[nx][ny] = True
                    heapq.heappush(pq,(max(time,grid[nx][ny]),nx,ny))
        
        return -1

    