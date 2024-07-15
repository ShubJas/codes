class Solution:
    def find(self, x):
        # Path compression heuristic to find the root of x
        # If x is not its own parent, recursively find the root and update the parent of x
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, u, v):
        # Find the roots of the sets u and v belong to
        root_u = self.find(u)
        root_v = self.find(v)

        # If the roots are the same, u and v are already connected
        if root_u == root_v:
            return False

        # Union by rank: attach the smaller tree under the root of the deeper tree
        if self.rank[root_u] < self.rank[root_v]:
            root_u, root_v = root_v, root_u

        # Update the parent of root_v to root_u
        self.parent[root_v] = root_u

        # Update the rank if necessary
        if self.rank[root_u] == self.rank[root_v]:
            self.rank[root_u] += 1

        return True

    def equationsPossible(self, equations: List[str]) -> bool:
        # Set to store unique variables
        var = set()
        for eq in equations:
            var.add(eq[0])
            var.add(eq[3])

        # Dictionary to encode variables to indices
        encoding = {}
        for i, x in enumerate(var):
            encoding[x] = i

        n = len(var)
        # Initialize the parent list such that each variable is its own parent
        self.parent = list(range(n))
        # Initialize the rank list with 1
        self.rank = [1] * n

        # Process equality equations first
        for eq in equations:
            a = encoding[eq[0]]
            b = encoding[eq[3]]
            op = eq[1]

            # If the equation is '==', union the sets containing a and b
            if op == '=':
                self.union(a, b)

        # Process inequality equations
        for eq in equations:
            a = encoding[eq[0]]
            b = encoding[eq[3]]
            op = eq[1]

            # If the equation is '!=', check if a and b are in the same set
            if op == '!':
                if self.find(a) == self.find(b):
                    return False

        # If all checks pass, return True
        return True

