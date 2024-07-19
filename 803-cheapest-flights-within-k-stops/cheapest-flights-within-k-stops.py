import collections
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Initialize the graph as an adjacency list
        graph = collections.defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))
        
        # Priority queue to keep track of (cost, current_node, stops)
        pq = [(0, src, 0)]
        # Dictionary to store the minimum cost to reach each node with a specific number of stops
        dist = {}

        while pq:
            cost, node, stops = heapq.heappop(pq)

            # If we reach the destination node, return the cost
            if node == dst:
                return cost

            # If the number of stops exceeds k, skip this path
            if stops > k:
                continue

            # Explore neighbors
            for neighbor, weight in graph[node]:
                new_cost = cost + weight
                # If the new cost is cheaper or we have not exceeded the maximum number of stops
                if new_cost < dist.get((neighbor, stops + 1), float('inf')):
                    dist[(neighbor, stops + 1)] = new_cost
                    heapq.heappush(pq, (new_cost, neighbor, stops + 1))
        
        # If we cannot reach the destination within k stops
        return -1

