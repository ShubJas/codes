class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        """
        This function uses a priority queue (min-heap) to find the minimum time required 
        to swim from the top-left corner to the bottom-right corner of the grid. 
        It uses a modified Dijkstra's algorithm, considering the time as the maximum 
        elevation that needs to be overcome at any step.
        """

        # Initialize the priority queue with the starting cell (elevation, x, y)
        pq = [(grid[0][0], 0, 0)]

        n = len(grid)
        m = len(grid[0])

        # Create a visited array to keep track of processed cells
        visited = [[False] * m for _ in range(n)]

        # Directions for moving in the grid: right, down, left, up
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        while pq:
            # Pop the cell with the smallest elevation/time from the priority queue
            time, x, y = heapq.heappop(pq)

            # If we've reached the bottom-right corner, return the current time
            if x == n - 1 and y == m - 1:
                return time

            # Explore all 4 possible directions
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                # Check if the neighboring cell is within bounds and not visited
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                    visited[nx][ny] = True
                    # Push the neighboring cell into the priority queue with the time being
                    # the maximum of the current time and the elevation of the neighboring cell
                    heapq.heappush(pq, (max(time, grid[nx][ny]), nx, ny))

        # If we exit the loop without having reached the bottom-right corner, return -1
        # This line is theoretically unreachable because the problem guarantees a path exists
        return -1


