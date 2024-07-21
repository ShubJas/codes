
#  KRuskals
class Solution:
    def find(self, x):
        # Path compression heuristic: If the parent of x is not itself,
        # recursively find the root of x and make the root the parent of x.
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, u, v):
        # Find the roots of the sets that u and v belong to
        root_u = self.find(u)
        root_v = self.find(v)
        
        # If both u and v have the same root, they are already connected, so return False
        if root_u == root_v:
            return False
        
        # Union by rank: attach the smaller tree under the root of the deeper tree
        if self.rank[root_u] < self.rank[root_v]:
            root_u, root_v = root_v, root_u
            
        # Make root_u the parent of root_v
        self.parents[root_v] = root_u
        
        # If the ranks of the roots are equal, increment the rank of the new root
        if self.rank[root_u] == self.rank[root_v]:
            self.rank[root_u] += 1
        
        return True

    def manhattan_distance(self, i, j, points):
        # Calculate the Manhattan distance between points i and j
        p1 = points[i]
        p2 = points[j]
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)  # Number of points
        self.parents = list(range(n))  # Initialize each point to be its own parent
        self.rank = [0] * n  # Initialize the rank for each point to 0

        edges = []
        # Generate all possible edges with their Manhattan distances
        for i in range(n):
            for j in range(i + 1, n):
                edges.append((self.manhattan_distance(i, j, points), i, j))
        
        # Sort the edges by distance in ascending order
        edges.sort(key=lambda x: x[0])

        edge_count = 0  # Count of edges included in the MST
        total_cost = 0  # Total cost to connect all points

        # Iterate through the sorted edges
        for cost, x, y in edges:
            # Use union to add the edge to the MST if it connects two different components
            if self.union(x, y):
                total_cost += cost  # Add the edge cost to the total cost
                edge_count += 1  # Increment the edge count
                
                # Early exit if we have used n-1 edges (MST for n nodes has n-1 edges)
                if edge_count == n - 1:
                    return total_cost
            
        # Return the total cost to connect all points
        return total_cost

# #  Prims
# class Solution:
#     def manhattan_distance(self, i, j, points):

#         p1 = points[i]
#         p2 = points[j]
#         return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

#     def minCostConnectPoints(self, points: List[List[int]]) -> int:

#         n = len(points)  # Number of points
#         visited = [False] * n  # Array to keep track of visited points

#         # Priority queue to store (cost, point_index), starting with cost 0 and point 0
#         pq = [(0, 0)]
#         edge_count = 0  # Counter for the number of edges added to the MST
#         total_cost = 0  # Total cost to connect all points

#         # While there are edges in the priority queue and we haven't connected all points
#         while pq and edge_count < n:
#             # Pop the smallest cost edge from the priority queue
#             cost, u = heapq.heappop(pq)

#             # If the point is already visited, skip it
#             if visited[u]: # wont allow cycles
#                 continue

#             # Mark the point as visited
#             visited[u] = True
#             # Add the cost of this edge to the total cost
#             total_cost += cost
#             # Increment the edge count
#             edge_count += 1

#             # Check all other points to find the next edge to add
#             for v in range(n):
#                 if not visited[v]:
#                     # Calculate the cost to connect point u to point v
#                     next_cost = self.manhattan_distance(u, v, points)
#                     # Add the edge to the priority queue
#                     heapq.heappush(pq, (next_cost, v))

#         # Return the total cost to connect all points
#         return total_cost

