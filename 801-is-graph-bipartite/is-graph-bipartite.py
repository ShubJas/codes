from collections import deque

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n  # Initialize color array with -1 (uncolored state for all nodes)

        for i in range(n):
            if color[i] != -1:
                continue  # If the node is already colored, skip to the next node

            color[i] = 1  # Start coloring this node with color 1
            q = deque([i])  # Initialize the BFS queue with the current node

            while q:
                t = q.popleft()  # Dequeue a node 't' from the front of the queue

                for neighbor in graph[t]:  # Iterate over all neighbors of node 't'
                    if color[neighbor] == -1:  # If the neighbor is uncolored
                        color[neighbor] = 1 - color[t]  # Color the neighbor with the opposite color of 't'
                        q.append(neighbor)  # Enqueue the neighbor for further processing
                    elif color[neighbor] == color[t]:  # If the neighbor has the same color as 't'
                        return False  # The graph is not bipartite, return False

        return True  # If all nodes are processed without conflicts, the graph is bipartite

