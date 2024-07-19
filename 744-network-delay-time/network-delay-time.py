# Dijkstras
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Initialize the graph as an adjacency list
        # defaultdict(list) creates a dictionary where each value is a list by default
        graph = collections.defaultdict(list)

        # Populate the graph with edges
        for u, v, w in times:
            # For each edge (u, v) with weight w, add (v, w) to the adjacency list of node u
            graph[u].append((v, w))

        # Initialize the distance dictionary with all nodes set to infinity (unknown distance)
        # This dictionary will store the minimum distance from the start node to each node
        dist = {i: float('inf') for i in range(1, n + 1)}

        # Initialize a priority queue (min-heap) with the start node (k) and distance 0
        # The priority queue will help us process nodes in the order of their distance from the start node
        pq = [(0, k)]

        # Set the distance to the start node itself as 0
        dist[k] = 0

        # Process the priority queue until it is empty
        while pq:
            # Pop the node with the smallest distance from the priority queue
            d, node = heapq.heappop(pq)

            # If this distance is greater than the known distance to this node, skip processing
            # This check ensures we don't process stale entries in the priority queue
            if d > dist[node]:
                continue

            # Iterate over all neighbors of the current node
            for neighbor, weight in graph[node]:
                # Calculate the new distance to this neighbor through the current node
                new_dist = d + weight
                # If the new distance is smaller than the known distance, update it
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    # Push the neighbor and its new distance onto the priority queue
                    heapq.heappush(pq, (new_dist, neighbor))

        # Find the maximum distance from the start node to any other node
        max_dist = max(dist.values())

        # If the maximum distance is infinity, it means not all nodes are reachable
        # In that case, return -1; otherwise, return the maximum distance
        return max_dist if max_dist != float('inf') else -1
