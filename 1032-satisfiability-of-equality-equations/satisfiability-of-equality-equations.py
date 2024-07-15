class Solution:
    def find(self, x):
        # Path compression heuristic
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u == root_v:
            return False

        # Union by rank
        if self.rank[root_u] < self.rank[root_v]:
            root_u, root_v = root_v, root_u

        self.parent[root_v] = root_u
        if self.rank[root_u] == self.rank[root_v]:
            self.rank[root_u] += 1
        return True

    def equationsPossible(self, equations: List[str]) -> bool:
        var = set()
        for eq in equations:
            var.add(eq[0])
            var.add(eq[3])

        encoding = {}
        for i, x in enumerate(var):
            encoding[x] = i

        n = len(var)
        self.parent = list(range(n))
        self.rank = [1] * n

        for eq in equations:
            a = encoding[eq[0]]
            b = encoding[eq[3]]
            op = eq[1]

            if op == '=':
                self.union(a, b)

        for eq in equations:
            a = encoding[eq[0]]
            b = encoding[eq[3]]
            op = eq[1]

            if op == '!':
                if self.find(a) == self.find(b):
                    return False

        return True
