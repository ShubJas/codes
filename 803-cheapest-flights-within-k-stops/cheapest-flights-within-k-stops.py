import heapq
import collections

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Initialize the graph as an adjacency list
        graph = collections.defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))
        
        # Priority queue to keep track of (cost, current_node, stops)
        pq = [(0, src, 0)]
        # Initialize the distance array with infinity
        dist = [[float('inf')] * (k + 2) for _ in range(n)]
        dist[src][0] = 0
        
        while pq:
            # Pop the element with the smallest cost
            cost, node, stops = heapq.heappop(pq)
            
            # If the destination node is reached, return the cost
            if node == dst:
                return cost
            
            # If the number of stops exceeds k, skip this path
            if stops > k:
                continue
            
            # Explore neighbors
            for neighbor, weight in graph[node]:
                new_cost = cost + weight
                # If the new cost is cheaper or within the allowed number of stops
                if new_cost < dist[neighbor][stops + 1]:
                    dist[neighbor][stops + 1] = new_cost
                    heapq.heappush(pq, (new_cost, neighbor, stops + 1))
        
        # Find the minimum cost to reach the destination within k stops
        min_cost = min(dist[dst])
        return -1 if min_cost == float('inf') else min_cost
