# Cycle detection using DFS and dp
class Solution:
    def dfs(self, i, graph, dp):
        # If the node has been processed before, return its state (True if safe, False otherwise)
        if dp[i] != 0:
            return dp[i] == 1

        # Mark the node as being processed to detect cycles
        dp[i] = -1

        # Recursively process all the neighbors
        for con in graph[i]:
            # If any neighbor is not safe, the current node is also not safe
            if not self.dfs(con, graph, dp):
                return False
        
        # If all neighbors are safe, mark the current node as safe
        dp[i] = 1
        return True

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        """
        Find all eventual safe nodes in the graph.
        
        :param graph: Adjacency list representing the graph
        :return: List of all safe nodes sorted in ascending order
        """
        
        result = []  # List to store the safe nodes
        n = len(graph)  # Number of nodes in the graph
        dp = [0] * n  # dp array to store the state of each node (-1: being processed, 1: safe, 0: unknown)

        # Process each node in the graph
        for i in range(n):
            # If the node is safe, add it to the result list
            if self.dfs(i, graph, dp):
                result.append(i)

        return result  # Return the list of safe nodes
