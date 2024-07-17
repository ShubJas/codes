class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        self.rows = len(mat)  # Number of rows
        self.cols = len(mat[0])  # Number of columns

        q = deque()  # Initialize deque for BFS

        # Enqueue all cells that are 0
        for i in range(self.rows):
            for j in range(self.cols):
                if mat[i][j] == 0:
                    q.append((i-1, j))
                    q.append((i+1, j))
                    q.append((i, j-1))
                    q.append((i, j+1))

        step = 0  # Initialize step counter
        visited = [[False for _ in range(self.cols)] for _ in range(self.rows)]  # Initialize visited matrix

        while q:
            step += 1
            qlen = len(q)  # Get the current level size
            for _ in range(qlen): # for these many pops only step was taken
                i, j = q.popleft()
                # Check boundaries and if the cell is unvisited and has value 1
                if 0 <= i < self.rows and 0 <= j < self.cols and not visited[i][j] and mat[i][j] != 0:
                    visited[i][j] = True  # Mark cell as visited
                    mat[i][j] = step  # Update matrix with current step count
                    # Enqueue adjacent cells
                    q.append((i-1, j))
                    q.append((i+1, j))
                    q.append((i, j-1))
                    q.append((i, j+1))

        return mat  # Return the updated matrix