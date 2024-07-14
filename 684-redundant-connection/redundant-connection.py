class Solution:
    def find(self, x):
        # Path compression heuristic: Make each node in the path point directly to the root
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Determine the number of edges, which also indicates the number of nodes (since nodes are 1-indexed)
        n = len(edges)
        
        # Initialize the parent array for union-find. Each node is its own parent initially.
        self.parent = list(range(n + 1))  # Use n+1 to handle 1-based indexing

        # Iterate through each edge in the edges list
        for u, v in edges:
            # Find the roots of the sets u and v belong to
            root_u = self.find(u)
            root_v = self.find(v)

            # If the roots are different, union the sets by making one root point to the other
            if root_u != root_v:
                self.parent[root_v] = root_u
            else:
                # If u and v are already connected, this edge is redundant
                return [u, v]

        # If no redundant connection is found (should not happen in a valid input), return an empty list
        return []
