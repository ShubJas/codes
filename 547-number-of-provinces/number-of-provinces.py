class Solution:
    def find(self, x):
        # Path compression heuristic
        # If the current node is not its own parent, find the root of its set
        # and make the current node point directly to the root.
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # Find the roots of the sets x and y belong to
        root_x = self.find(x)
        root_y = self.find(y)
        # If the roots are different, merge the sets by making one root point to the other
        if root_x != root_y:
            self.parent[root_y] = root_x
            # Uncomment the next line if you want to keep track of the number of union operations
            # self.count +=1

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)  # Get the number of cities
        # Initialize the parent list such that each city is its own parent initially
        self.parent = list(range(n))
        # Uncomment the next line if you want to keep track of the number of union operations
        # self.count = 0

        # Iterate through the upper triangular part of the adjacency matrix (excluding the diagonal)
        for i in range(n):
            for j in range(i + 1, n):
                # If city i and city j are directly connected, perform a union operation
                if isConnected[i][j] == 1:
                    self.union(i, j)

        # Find all unique roots to determine the number of provinces
        unique_roots = set(self.find(i) for i in range(n))
        # Uncomment the next line if you want to return the number of provinces using the union count
        # return n - self.count
        return len(unique_roots)