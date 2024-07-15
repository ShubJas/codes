class Solution:
    def find(self, x):
        # Path compression heuristic to find the root of x
        # If x is not the root of itself, recursively find the root
        # and make x point directly to the root to flatten the structure
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # Find the roots of x and y
        root_x = self.find(x)
        root_y = self.find(y)

        # If they are already in the same set, no need to union
        if root_x == root_y:
            return False

        # Union by rank: attach the smaller tree under the root of the deeper tree
        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x

        # Merge the trees and update the rank
        self.rank[root_x] += self.rank[root_y]
        self.parent[root_y] = root_x
        return True

    def removeStones(self, stones: List[List[int]]) -> int:
        # Get the number of stones
        n = len(stones)

        # Initialize the Union-Find structure
        # Each stone is its own parent initially
        self.parent = list(range(n))

        # Each tree has rank 1 initially
        self.rank = [1] * n

        # Dictionary to store row representatives
        X = {}
        # Dictionary to store column representatives
        Y = {}

        # Counter for the number of stones that can be removed
        count = 0

        # Iterate through each stone
        for i, (x, y) in enumerate(stones):
            # Check if there is already a stone in row x
            if x in X:
                # Union current stone with the stone in the same row
                count += self.union(i, X[x])
            else:
                # Set the current stone as the representative for row x
                X[x] = i

            # Check if there is already a stone in column y
            if y in Y:
                # Union current stone with the stone in the same column
                count += self.union(i, Y[y])
            else:
                # Set the current stone as the representative for column y
                Y[y] = i

        # Return the total number of union operations performed
        return count