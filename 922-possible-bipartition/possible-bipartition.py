from collections import defaultdict, deque

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        # Initialize color array with -1, representing uncolored nodes
        color = [-1] * n
        
        # Initialize deque for BFS
        q = deque()

        # Create an adjacency list for the graph
        dis = defaultdict(set)

        # Populate the adjacency list with dislikes
        for d in dislikes:
            dis[d[0] - 1].add(d[1] - 1)
            dis[d[1] - 1].add(d[0] - 1)

        # Iterate through each node to ensure all components are checked
        for i in range(n):
            # If the node is already colored, skip it
            if color[i] != -1:
                continue
            
            # Color the starting node and add it to the queue
            color[i] = 1
            q.append(i)

            # Perform BFS
            while q:
                curr = q.popleft()  # Get the current node

                # Iterate through all neighbors of the current node
                for neighbor in dis[curr]:
                    if color[neighbor] == -1:  # If the neighbor is uncolored
                        q.append(neighbor)  # Add the neighbor to the queue
                        color[neighbor] = 1 - color[curr]  # Color it with the opposite color
                    elif color[neighbor] == color[curr]:  # If the neighbor has the same color
                        return False  # The graph is not bipartite

        # If all nodes are processed without conflicts, the graph is bipartite
        return True
