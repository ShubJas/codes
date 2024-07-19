class Solution:
    def dijkstras(self,s):

        pq = [(0,s)]
        self.dist[s][s] = 0

        while pq:
            d , node = heapq.heappop(pq)

            if d > self.dist[s][node]:
                continue 
            
            for neighbor, weight in self.graph[node]:
                new_dist = d + weight
                if new_dist < self.dist[s][neighbor]:
                    self.dist[s][neighbor] = new_dist
                    heapq.heappush(pq,(new_dist,neighbor))
            


    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        self.graph = collections.defaultdict(list)
        for u,v,w in edges:
            self.graph[u].append((v,w))
            self.graph[v].append((u,w))

        
        self.dist = [[float('inf') for _ in range(n)] for _ in range(n)]


        for node in range(n):
            self.dijkstras(node)
        
        min_count = float('inf')
        ans = -1
        for i,city in enumerate(self.dist):
            count = 0 
            for d in city:
                if d <= distanceThreshold:
                    count+=1

            if count <= min_count:
                min_count = count
                ans = i
        
        return ans



