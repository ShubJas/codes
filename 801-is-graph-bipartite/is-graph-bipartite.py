class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n
        q = collections.deque()
        for i in range(n):

            if color[i] != -1:
                continue
            
            color[i] = 1
            q.append(i)

            while q:

                curr = q.popleft()

                for neighbour in graph[curr]:
                    if color[neighbour] == -1:
                        color[neighbour] = 1 - color[curr]
                        q.append(neighbour)
                    elif color[neighbour] == color[curr]:
                        return False
        return True