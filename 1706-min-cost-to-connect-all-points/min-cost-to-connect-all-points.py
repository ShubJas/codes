class Solution:
    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        
        if root_u == root_v:
            return False
        
        if self.rank[root_u] < self.rank[root_v]:
            root_u, root_v = root_v, root_u
            
        self.parents[root_v] = root_u
        
        if self.rank[root_u] == self.rank[root_v]:
            self.rank[root_u] += 1
        
        return True

    def manhattan_distance(self,i,j,points):
        p1 = points[i]
        p2 = points[j]
        return abs(p1[0]- p2[0]) + abs(p1[1] - p2[1])

    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        n = len(points)
        self.parents = list(range(n))
        self.rank = [0] * n

        edge =  []
        for i in range(n):
            for j in range(i+1,n):

                edge.append((self.manhattan_distance(i,j,points),i,j))
        

        edge.sort(key = lambda x : x[0])
        edge_count = 0 
        total_cost = 0
        for cost , x , y in edge:
            if self.union(x,y):
                total_cost += cost
                edge_count +=1
                if edge_count == n - 1:
                    return total_cost
            
        return total_cost

        