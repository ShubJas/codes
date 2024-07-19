class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # Initialize the in-degree array and the reversed graph
        indeg = [0] * len(graph)
        rev_graph = defaultdict(list)
        
        # rev_graph - Changing outgoing edge to to incoming so that we can use Khan algo ( safe node reversed- 0 incoming edge node as bfs runs in khan   )
        # Build the reversed graph and the in-degree array
        for i, adj in enumerate(graph):
            for j in adj:
                # Increase the in-degree for each node that has an incoming edge
                indeg[i] += 1
                # Add the edge in the reversed direction
                rev_graph[j].append(i)
        
        # Initialize the queue with nodes having in-degree 0 (terminal nodes)
        q = deque([i for i in range(len(graph)) if indeg[i] == 0])
        
        # List to store the safe nodes
        safe_nodes = []
        
        # Process the nodes in topological order
        while q:
            curr = q.popleft()
            safe_nodes.append(curr)
            # Iterate over all neighbors of the current node in the reversed graph
            for neighbor in rev_graph[curr]:
                indeg[neighbor] -= 1
                # If the in-degree of a neighbor becomes 0, add it to the queue
                if indeg[neighbor] == 0:
                    q.append(neighbor)
        
        # Return the sorted list of safe nodes
        return sorted(safe_nodes)