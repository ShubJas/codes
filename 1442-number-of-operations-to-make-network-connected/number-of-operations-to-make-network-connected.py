class Solution:
    def find(self,x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        
        self.parent = list(range(n))
        self.extra = 0
        connected = set()

        for u,v in connections:
            root_u = self.find(u)
            root_v = self.find(v)

            if root_u != root_v:
                self.parent[root_v] = root_u
                connected.add(u)
                connected.add(v)

            else:
                self.extra +=1
        print(self.extra)        

        unique = set(self.find(i) for i in range(n))
        needed =len(unique) - 1
        # cords needed unique-1
        if needed <= self.extra:
            return needed
        else:
            return -1




