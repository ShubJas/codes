from collections import deque
from typing import List

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        # Get the number of rows and columns in the grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        
        # Initialize a deque for BFS
        q = deque()

        # Enqueue all water cells adjacent to land cells
        for i in range(self.rows):
            for j in range(self.cols):
                if grid[i][j] == 1:  # Land cell found
                    q.append((i + 1, j))
                    q.append((i - 1, j))
                    q.append((i, j + 1))
                    q.append((i, j - 1))
        
        step = 0  # Initialize step counter
        visited = [[False for _ in range(self.cols)] for _ in range(self.rows)]  # Initialize visited matrix

        while q:
            step += 1
            qlen = len(q)  # Get the current level size

            for _ in range(qlen):
                i, j = q.popleft()  # Dequeue the next cell
                
                # Check if the cell is within bounds, unvisited, and is a water cell
                if 0 <= i < self.rows and 0 <= j < self.cols and not visited[i][j] and grid[i][j] != 1:
                    visited[i][j] = True  # Mark cell as visited
                    q.append((i + 1, j))  # Enqueue adjacent cells for BFS
                    q.append((i - 1, j))
                    q.append((i, j + 1))
                    q.append((i, j - 1))

        # If no valid step was made, return -1; otherwise, return the number of steps minus 1
        return step - 1 if step > 1 else -1
