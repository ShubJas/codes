# Khans / BFS

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Initialize graph and in-degree array
        graph = defaultdict(list)
        in_degree = [0] * numCourses

        # Build the graph and fill in-degree array
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1

        # Initialize queue with courses having zero in-degree
        q = deque([i for i in range(numCourses) if in_degree[i] == 0])

        topo = []

        while q:
            course = q.popleft()
            topo.append(course)

            # Reduce in-degree for all the neighbors
            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                # If in-degree becomes zero, add to queue
                if in_degree[neighbor] == 0:
                    q.append(neighbor)

        # Check if topological sort is possible
        if len(topo) == numCourses:
            return topo
        else:
            return []

# # DFS approach
# class Solution:
#     def dfs(self, i, graph):
#         # If the node is already visited, check its state
#         if self.visited[i] != 0:
#             # If the node is being visited (part of the current path), a cycle is detected
#             return self.visited[i] == 1

#         # Mark the node as being visited (part of the current path)
#         self.visited[i] = -1

#         # Recursively visit all the neighbors
#         for neighbor in graph[i]:
#             # If a cycle is detected in any neighbor, return False
#             if not self.dfs(neighbor, graph):
#                 return False

#         # Mark the node as visited and add it to the topo list
#         self.visited[i] = 1
#         self.topo.append(i)
#         return True
        
#     def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
#         # Create the graph using adjacency list representation
#         graph = defaultdict(list)
#         for course, prereq in prerequisites:
#             graph[prereq].append(course)
        
#         # Initialize the topo list and visited array
#         self.topo = []
#         self.visited = [0] * numCourses
        
#         # Perform DFS for each course
#         for i in range(numCourses):
#             if self.visited[i] == 0:
#                 if not self.dfs(i, graph):
#                     # If a cycle is detected, return an empty list
#                     return []

#         # Return the topo list in reverse order
#         return self.topo[::-1]

