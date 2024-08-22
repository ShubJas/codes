class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        



        graph = defaultdict(list)


        for u,v,p in flights:
            graph[u].append((v,p))
        

        pq = [(0,src,0)]

        distance = [[float('inf')] * (k+2) for _ in range(n)]

        distance[src][0] = 0

        while pq:

            price, curr, stop_count = heapq.heappop(pq)

            if curr == dst:
                return price
            if stop_count > k:
                continue

            

            for neighbor, weight in graph[curr]:
                new_cost = price +  weight

                if new_cost < distance[neighbor][stop_count + 1]:
                    distance[neighbor][stop_count + 1] = new_cost
                    heapq.heappush(pq,(new_cost,neighbor,stop_count+1))


        min_cost = min(distance[dst])

        return min_cost if min_cost != float('inf') else -1


