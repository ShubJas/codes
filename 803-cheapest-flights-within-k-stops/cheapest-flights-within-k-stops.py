class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Initialize the graph as an adjacency list
        # graph[u] will be a list of tuples (v, w) where there is an edge from u to v with weight w
        graph = collections.defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))
        
        # Initialize the distance array with infinity
        # dist[i][j] will represent the minimum cost to reach node i with exactly j stops
        dist = [[float('inf')] * (k + 2) for _ in range(n)]
        
        # Priority queue (min-heap) to keep track of (cost, current_node, stops)
        pq = [(0, src, 0)]
        
        # The distance to reach the source node with 0 stops is 0
        dist[src][0] = 0
        
        while pq:
            # Pop the element with the smallest cost from the priority queue
            cost, node, stops = heapq.heappop(pq)
            
            # If the destination node is reached, return the cost
            if node == dst:
                return cost
            
            # If the number of stops exceeds k, skip this path
            if stops > k:
                continue
            
            # Explore all neighbors of the current node
            for neighbor, weight in graph[node]:
                new_cost = cost + weight  # Calculate the new cost to reach the neighbor
                
                # If the new cost is cheaper or within the allowed number of stops
                if new_cost < dist[neighbor][stops + 1]:
                    dist[neighbor][stops + 1] = new_cost  # Update the distance array
                    heapq.heappush(pq, (new_cost, neighbor, stops + 1))  # Push the new state into the priority queue
        
        # Find the minimum cost to reach the destination within k stops
        min_cost = min(dist[dst])
        
        # If no valid path is found, return -1
        return -1 if min_cost == float('inf') else min_cost

        """
        Explanation:

        1. **Graph Construction**:
           - The graph is constructed using an adjacency list where each node points to its neighbors along with the edge weights.
           - Example: If there is a flight from node 0 to node 1 with a cost of 100, it is represented as `graph[0] = [(1, 100)]`.

        2. **Distance Array Initialization**:
           - The distance array `dist` is initialized to infinity (`float('inf')`), indicating that initially all nodes are unreachable.
           - `dist[i][j]` represents the minimum cost to reach node `i` with exactly `j` stops.
           - This is crucial to handle the constraint on the maximum number of stops (`k`).

        3. **Priority Queue Initialization**:
           - A priority queue (min-heap) is used to always expand the least costly path first.
           - The queue stores tuples `(cost, node, stops)` where `cost` is the total cost to reach `node` with `stops` number of stops.

        4. **Processing the Priority Queue**:
           - The node with the smallest cost is popped from the priority queue.
           - If this node is the destination (`dst`), the cost is returned as the result.
           - If the number of stops exceeds `k`, this path is skipped as it doesn't meet the constraint.
           - For each neighbor of the current node, the new cost to reach that neighbor is calculated.
           - If this new cost is cheaper and within the allowed number of stops, the neighbor is pushed into the priority queue with the updated cost and stops count.

        5. **Finding the Minimum Cost**:
           - The minimum cost to reach the destination node within `k` stops is found by taking the minimum value from the distance array for the destination node.
           - If no valid path is found (i.e., the minimum cost is still infinity), `-1` is returned.

        **Why This Approach Works**:
        - By using a priority queue, we always explore the most promising paths first, ensuring that we find the shortest path efficiently.
        - The 2D distance array allows us to keep track of the minimum costs associated with each node for each possible number of stops.
        - This ensures that we handle the constraint on the number of stops correctly, avoiding unnecessary computations and incorrect paths.


        Including the initial state (0 stops) and up to k stops, we need to account for k + 1 possible states.
        Additionally, we use k + 2 to ensure there is room for indexing up to k + 1 stops without going out of bounds.
        """
        