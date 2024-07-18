# Cycle detection using DFS and self.visited
class Solution:
    def dfs(self, i, graph):
        # If the node has been processed before, return its state (True if safe, False otherwise)
        if self.visited[i] != 0:
            return self.visited[i] == 1

        # Mark the node as being processed to detect cycles
        self.visited[i] = -1

        # Recursively process all the neighbors
        for con in graph[i]:
            # If any neighbor is not safe, the current node is also not safe
            if not self.dfs(con, graph):
                return False
        
        # If all neighbors are safe, mark the current node as safe
        self.visited[i] = 1
        return True

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        result = []  # List to store the safe nodes
        n = len(graph)  # Number of nodes in the graph
        self.visited = [0] * n  # self.visited array to store the state of each node (-1: being processed, 1: safe, 0: unknown)

        # Process each node in the graph
        for i in range(n):
            # If the node is safe, add it to the result list
            if self.dfs(i, graph):
                result.append(i)

        return result  # Return the list of safe nodes
