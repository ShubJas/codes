class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        color = [-1] * (n)
        q = collections.deque()

        dis = defaultdict(set)

        for d in dislikes:
            dis[d[0]-1].add(d[1]-1)
            dis[d[1]-1].add(d[0]-1)

        for i in range(n):

            if color[i] != -1:
                continue
            
            color[i] = 1
            q.append(i)

            while q:
                curr = q.popleft()

                for neighbour in dis[curr]:
                    if color[neighbour] == -1:
                        q.append(neighbour)
                        color[neighbour] = 1 - color[curr]
                    elif color[neighbour] == color[curr]:
                        return False
        return True