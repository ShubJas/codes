class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        

        graph = collections.defaultdict(list)

        for i,(u,v) in enumerate(edges):
            graph[u].append((v,succProb[i]))
            graph[v].append((u,succProb[i]))

        probabilities = [0] * n

        probabilities[start_node] = 1

        pq = [(-1,start_node)]

        while pq:

            prob , node = heapq.heappop(pq)
            prob = - prob
            if prob < probabilities[node]:
                continue
            
            if node == end_node:
                return prob

            for neighbor , edge_prob in graph[node]:
                new_prob = prob * edge_prob
                if new_prob > probabilities[neighbor]:
                    probabilities[neighbor] = new_prob
                    heapq.heappush(pq,(-new_prob,neighbor))
        
        return probabilities[end_node] 
            
