class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:

        # Convert obstacles to a set of tuples for O(1) lookup time
        obstacle_set = set(map(tuple, obstacles))
        
        # Function to calculate the distance
        def dist(x, y):
            return x ** 2 + y ** 2

        # Initializing the variables
        maxD = 0
        x = y = 0
        d = 0
        
        # Directions array representing north, east, south, and west
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # North, East, South, West

        for c in commands:
            if c == -1:  # Turn right
                d = (d + 1) % 4
            elif c == -2:  # Turn left
                d = (d + 3) % 4
            else:
                dx, dy = directions[d]
                for _ in range(c):
                    if (x + dx, y + dy) not in obstacle_set:
                        x += dx
                        y += dy
                    else:
                        break
                # Update maximum distance
                maxD = max(maxD, dist(x, y))

        return maxD
