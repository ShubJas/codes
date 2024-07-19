class Solution:
    def dijkstras(self, s):
        # Initialize the priority queue with the starting node 's' and a distance of 0
        pq = [(0, s)]
        # Set the distance to the starting node itself as 0
        self.dist[s][s] = 0

        while pq:
            # Pop the node with the smallest distance from the priority queue
            d, node = heapq.heappop(pq)

            # If the current distance 'd' is greater than the recorded distance, continue to the next iteration
            # This helps in avoiding processing the node if it already has a shorter path recorded
            if d > self.dist[s][node]:
                continue 
            
            # Traverse all the neighbors of the current node
            for neighbor, weight in self.graph[node]:
                # Calculate the new distance to the neighbor
                new_dist = d + weight
                # If the new distance is shorter than the recorded distance, update it
                if new_dist < self.dist[s][neighbor]:
                    self.dist[s][neighbor] = new_dist
                    # Push the neighbor with the updated distance into the priority queue
                    heapq.heappush(pq, (new_dist, neighbor))

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Initialize the graph as an adjacency list using a default dictionary
        self.graph = collections.defaultdict(list)
        
        # Build the graph from the edges input
        # Since the graph is undirected, add both directions for each edge
        for u, v, w in edges:
            self.graph[u].append((v, w))
            self.graph[v].append((u, w))

        # Initialize the distance matrix with infinity
        # dist[i][j] will store the shortest distance from node i to node j
        self.dist = [[float('inf') for _ in range(n)] for _ in range(n)]

        # Run Dijkstra's algorithm for each node to find the shortest paths to all other nodes
        for node in range(n):
            self.dijkstras(node)
        
        # Initialize variables to track the minimum count of reachable cities and the corresponding city index
        min_count = float('inf')  # Start with infinity to ensure any count will be smaller
        ans = -1  # Initialize with -1, which will be updated to a valid city index
        
        # Iterate over each city's distances to other cities
        for i, city in enumerate(self.dist):
            count = 0  # Count of cities reachable within the distance threshold
            for d in city:
                if d <= distanceThreshold:
                    count += 1
            
            # If the current city's reachable count is less than or equal to the minimum count found so far
            # Update the minimum count and the corresponding city index
            # If there is a tie (count is the same), the city with the larger index will be chosen
            if count <= min_count:
                min_count = count
                ans = i
        
        # Return the city with the minimum number of reachable cities within the distance threshold
        return ans
