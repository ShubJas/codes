class Solution:
    def find(self, x):
        # Path compression heuristic to find the root of x
        # If x is not the root of itself, recursively find the root
        # and make x point directly to the root to flatten the structure
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        # Initialize the Union-Find structure
        self.parent = list(range(n))  # Each computer is its own parent initially
        self.extra = 0  # Counter for the number of extra cables
        connected = set()  # Set to store connected computers

        for u, v in connections:
            # Find the roots of u and v
            root_u = self.find(u)
            root_v = self.find(v)

            if root_u != root_v:
                # Union the sets containing u and v
                self.parent[root_v] = root_u
                connected.add(u)
                connected.add(v)
            else:
                # If u and v are already connected, the cable is extra
                self.extra += 1

        # Find all unique roots to determine the number of disconnected components
        unique = set(self.find(i) for i in range(n))
        needed = len(unique) - 1  # Number of cables needed to connect all components

        # If we have enough extra cables to connect all components, return the number needed
        if needed <= self.extra:
            return needed
        else:
            # Otherwise, return -1 indicating it's not possible
            return -1