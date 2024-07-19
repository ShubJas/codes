class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = collections.defaultdict(list)

        for u,v,w in times:
            graph[u].append((v,w))

        
        dist = {i : float('inf') for i in range(1,n+1)}

        pq = [(0,k)]
        dist[k] = 0

        while pq:
            d , node = heapq.heappop(pq)

            if d > dist[node]:
                continue
            

            for neighbor, weight in graph[node]:
                new_dist = d + weight
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    heapq.heappush(pq,(new_dist,neighbor))
        
        max_dist = max(dist.values())

        return max_dist if max_dist != float('inf') else -1