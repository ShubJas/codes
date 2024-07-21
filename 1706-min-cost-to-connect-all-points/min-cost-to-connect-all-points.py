#  Prims
class Solution:
    def manhattan_distance(self,i,j,points):
        p1 = points[i]
        p2 = points[j]
        return abs(p1[0] - p2[0]) + abs(p1[1]-p2[1])

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        

        n = len(points)
        visited = [False] * n

        pq = [(0,0)]
        edge_count = 0
        total_cost = 0

        while pq and edge_count < n:
            cost ,  u = heapq.heappop(pq)

            if visited[u]:
                continue
            
            visited[u] = True
            total_cost += cost
            edge_count +=1

            for v in range(n):
                if not visited[v]:
                    next_cost = self.manhattan_distance(u,v,points)
                    heapq.heappush(pq,(next_cost,v))
        return total_cost


