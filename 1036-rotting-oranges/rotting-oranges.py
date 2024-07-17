class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Initialize number of rows and columns
        self.rows = len(grid)
        self.cols = len(grid[0])

        # Initialize a deque for BFS
        q = deque()

        # Enqueue all initially rotten oranges
        for i in range(self.rows):
            for j in range(self.cols):
                if grid[i][j] == 2:  # Rotten orange found
                    q.append((i + 1, j))  # Add adjacent cells to the queue
                    q.append((i - 1, j))
                    q.append((i, j + 1))
                    q.append((i, j - 1))

        visited = [[False for _ in range(self.cols)] for _ in range(self.rows)]  # Initialize visited matrix
        minutes = 0  # Initialize time counter

        while q:
            minutes += 1  # Increment minutes for each level of BFS
            qlen = len(q)  # Get the current level size
            for _ in range(qlen):
                i, j = q.popleft()  # Dequeue the next cell

                # Check if the cell is within bounds, unvisited, and is a fresh orange
                if 0 <= i < self.rows and 0 <= j < self.cols and not visited[i][j] and grid[i][j] == 1:
                    grid[i][j] = 2  # Mark orange as rotten
                    visited[i][j] = True  # Mark cell as visited
                    # Enqueue adjacent cells for BFS
                    q.append((i + 1, j))
                    q.append((i - 1, j))
                    q.append((i, j + 1))
                    q.append((i, j - 1))

        # Check if there are any fresh oranges left
        for i in range(self.rows):
            for j in range(self.cols):
                if grid[i][j] == 1:
                    return -1  # If any fresh orange is left, return -1

        # If no fresh oranges, return 0 minutes, otherwise return total minutes - 1
        return max(0, minutes - 1)
