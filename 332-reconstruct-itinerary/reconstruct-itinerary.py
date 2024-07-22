class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        """
        Reconstructs the itinerary in order using all the tickets once and only once.
        The itinerary must begin with "JFK".
        If there are multiple valid itineraries, return the one with the smallest lexical order.
        """
        
        # Step 1: Build the graph
        # Create a default dictionary where each key's value is a list
        graph = defaultdict(list)
        
        # Step 2: Sort the tickets in reverse order and build the graph
        # We sort tickets in reverse order because we want to pop the smallest lexical order
        # ticket last. This ensures we can use DFS and a stack to get the correct order.
        for u, v in sorted(tickets, reverse=True):
            graph[u].append(v)

        # Step 3: Initialize a result list to store the final itinerary
        result = []

        # Step 4: Define a DFS function to traverse the graph
        def dfs(node):
            # While there are neighbors for the current node
            while graph[node]:
                # Pop the next destination from the graph and perform DFS on it
                # This ensures we always visit the smallest lexical order ticket first
                dfs(graph[node].pop())
            # Once there are no more neighbors, append the node to the result
            # This happens during backtracking, so the nodes are added in reverse order
            result.append(node)

        # Step 5: Start the DFS traversal from 'JFK'
        dfs("JFK")

        # Step 6: The result list is in reverse order, so we reverse it before returning
        return result[::-1]
