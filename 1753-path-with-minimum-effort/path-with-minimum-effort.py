import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # Initialize the priority queue with a tuple (effort, x, y)
        # Start from the top-left corner with an initial effort of 0
        pq = [(0, 0, 0)]
        
        self.rows = len(heights)  # Number of rows in the grid
        self.cols = len(heights[0])  # Number of columns in the grid

        # Create a 2D list to store the minimum effort to reach each cell
        efforts = [[float('inf') for _ in range(self.cols)] for _ in range(self.rows)]
        efforts[0][0] = 0  # Starting point effort is 0

        # Directions for moving up, down, left, and right
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        while pq:
            # Pop the cell with the minimum effort from the priority queue
            effort, x, y = heapq.heappop(pq)

            # If the current effort is greater than the known minimum effort to this cell, skip it
            if effort > efforts[x][y]:
                continue

            # Early exit: If we reach the bottom-right cell, return the effort
            if x == self.rows - 1 and y == self.cols - 1:
                return effort

            # Explore all possible directions
            for dx, dy in directions:
                nx = x + dx
                ny = y + dy

                # Check if the new position is within the grid bounds
                if 0 <= nx < self.rows and 0 <= ny < self.cols:
                    # Calculate the new effort to move to the neighboring cell
                    new_effort = max(effort, abs(heights[x][y] - heights[nx][ny]))
                    
                    # If the new effort is less than the known effort to the neighboring cell, update and push to the queue
                    if new_effort < efforts[nx][ny]:
                        efforts[nx][ny] = new_effort
                        heapq.heappush(pq, (new_effort, nx, ny))

        # Return the effort to reach the bottom-right cell
        return efforts[self.rows - 1][self.cols - 1]
