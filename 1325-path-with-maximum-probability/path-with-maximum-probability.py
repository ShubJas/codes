class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        # Create the graph as an adjacency list where each edge has a success probability
        graph = collections.defaultdict(list)
        for i, (u, v) in enumerate(edges):
            graph[u].append((v, succProb[i]))
            graph[v].append((u, succProb[i]))

        # Initialize a list to keep track of the maximum probability to reach each node
        probabilities = [0] * n
        probabilities[start_node] = 1  # Start node has a probability of 1 to reach itself

        # Priority queue to process nodes with their current probability
        # We use negative probabilities because heapq is a min-heap and we need a max-heap
        pq = [(-1, start_node)]

        while pq:
            # Get the node with the highest probability
            prob, node = heapq.heappop(pq)
            prob = -prob  # Convert back to positive

            # If this probability is less than the already known maximum probability for this node, skip it
            if prob < probabilities[node]:
                continue

            # If we reached the end node, return the probability
            if node == end_node:
                return prob

            # Check all neighbors of the current node
            for neighbor, edge_prob in graph[node]:
                new_prob = prob * edge_prob
                # If the new probability is greater than the known probability for this neighbor, update it
                if new_prob > probabilities[neighbor]:
                    probabilities[neighbor] = new_prob
                    # Push the neighbor to the priority queue with the updated probability
                    heapq.heappush(pq, (-new_prob, neighbor))
        
        # Return the maximum probability to reach the end node
        return probabilities[end_node]