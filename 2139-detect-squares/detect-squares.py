from collections import defaultdict

class DetectSquares:
    def __init__(self):
        # Initialize a dictionary to keep track of how many times each point has been added.
        # The key is the (x, y) coordinate tuple, and the value is the count of occurrences.
        self.point_count = defaultdict(int)
        

    def add(self, point: List[int]) -> None:
        # Convert the point list to a tuple , array cant be hashed as its mutable
        # This keeps track of how many times each point has been added to the system.
        self.point_count[tuple(point)] += 1
        
        

    def count(self, point: List[int]) -> int:
        # Initialize the count of squares to 0.
        count = 0
        
        # Extract the x and y coordinates of the target point.
        x1, y1 = point
        
        # Get all points that have been added so far.
        points = self.point_count.keys()

        # Loop through each point that has been added.
        for (x, y) in points:
            # To form a square, the distance between x1 and x (horizontal side) should be equal to the distance
            # between y1 and y (vertical side). Also, x != x1 to ensure that this is not a point on the same vertical line.
            if abs(x1 - x) == abs(y1 - y) and x != x1:
                
                # If this condition is true, we're forming the other two corners of a square.
                # We check if the points (x, y1) and (x1, y) exist, which would form the necessary square.
                # (x, y1) is the point directly above/below (x, y) on the vertical line,
                # and (x1, y) is the point directly left/right of (x, y) on the horizontal line.
                
                if (x, y1) in points and (x1, y) in points:
                    # If both points exist, we count the number of times these points appear.
                    # The total number of squares formed is the product of the occurrences of these points.
                    count += self.point_count[(x, y1)] * self.point_count[(x1, y)] * self.point_count[(x, y)]

        # Return the total number of squares formed that have the input point as one corner.
        return count