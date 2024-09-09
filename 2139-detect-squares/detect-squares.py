class DetectSquares:
    def distance(p1,p2):
        return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

    def __init__(self):
        self.point_count = defaultdict(int)
        

    def add(self, point: List[int]) -> None:
        self.point_count[tuple(point)] += 1
        
        

    def count(self, point: List[int]) -> int:
        count = 0
        x1,y1 = point
        points = self.point_count.keys()
        for (x,y) in points:
            if abs(x1-x) == abs(y1-y) and x!=x1:
                if (x,y1) in points and (x1,y) in points:
                    count += self.point_count[(x,y1)] * self.point_count[(x1,y)] * self.point_count[(x,y)]

        return count


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)