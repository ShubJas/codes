class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:


        pq =[(0,0,0)]

        self.rows = len(heights)
        self.cols = len(heights[0]) 

        efforts = [[float('inf') for _ in range(self.cols)] for _ in range(self.rows)]


        efforts[0][0] = 0
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        while pq:
            effort , x , y =  heapq.heappop(pq)


            if effort > efforts[x][y]:
                continue
            
            # if x == self.rows - 1 and y == self.cols - 1:
            #     return effort
            
            for dx , dy in directions:
                nx = x + dx
                ny = y + dy
                
                if  0 <= nx < self.rows and 0 <= ny < self.cols:
                    new_effort = max(effort, abs(heights[x][y] - heights[nx][ny]))
                    if new_effort < efforts[nx][ny]:
                        efforts[nx][ny] = new_effort
                        heapq.heappush(pq,(new_effort,nx,ny))
            

        return efforts[self.rows-1][self.cols-1]
            


            


        