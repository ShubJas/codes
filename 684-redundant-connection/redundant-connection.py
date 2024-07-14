class Solution:
    def find(self,x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        n = len(edges)
        self.parent = list(range(n+1))

        for u,v in edges:

            root_u = self.find(u)
            root_v = self.find(v)

            if root_u != root_v:
                self.parent[root_v] = root_u
            else:
                return [u,v]
        
        return []
            




