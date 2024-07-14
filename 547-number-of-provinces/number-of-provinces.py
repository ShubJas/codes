class Solution:
    def find(self, x):
        # Path compression heuristic
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_y] = root_x
            self.count +=1

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        self.parent = list(range(n))  # Initialize parent list
        self.count = 0

        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    self.union(i, j)

        # Find all unique roots to determine the number of provinces
        # unique_roots = set(self.find(i) for i in range(n))
        return n - self.count
        # return len(unique_roots)

