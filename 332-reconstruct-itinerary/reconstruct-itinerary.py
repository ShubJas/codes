class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        graph = defaultdict(list)
        for u , v in sorted(tickets,reverse=True):
            graph[u].append(v)

        result = []
        def dfs(node):
            while graph[node]:
                dfs(graph[node].pop())
            result.append(node)
        
        dfs("JFK")
        return result[::-1]
        