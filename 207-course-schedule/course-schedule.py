# DFS
class Solution:
    def dfs(self, i, graph):
        # If node is already visited (partially processed or fully processed)
        if self.visited[i] != 0:
            # Return True if fully processed, False if cycle detected
            return self.visited[i] == 1
        
        # Mark the node as partially processed (in the current recursion stack)
        self.visited[i] = -1

        # Process all the neighbors of the current node
        for neighbor in graph[i]:
            # If any neighbor leads to a cycle, return False
            if not self.dfs(neighbor, graph):
                return False
        
        # Mark the node as fully processed
        self.visited[i] = 1
        return True

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Initialize the visited list to track the state of each node (course)
        self.visited = [0] * numCourses
        # Initialize the adjacency list for the graph
        graph = defaultdict(list)

        # Build the graph based on the prerequisites
        for course, pre in prerequisites:
            graph[pre].append(course)

        # Check each course to see if it can be completed
        for i in range(numCourses):
            # If the course has not been visited, perform DFS
            if self.visited[i] == 0:
                # If a cycle is detected, return False
                if not self.dfs(i, graph):
                    return False

        # If no cycles are detected, return True
        return True

        
       

# # KHAN/ BFS
# class Solution:
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         # Initialize in-degree array and adjacency list
#         indeg = [0] * numCourses
#         graph = defaultdict(list)

#         # Build the graph and update in-degrees
#         for course, pre in prerequisites:
#             graph[pre].append(course)
#             indeg[course] += 1

#         # Initialize the queue with all nodes having in-degree 0
#         q = deque([i for i in range(numCourses) if indeg[i] == 0])
#         topo = []

#         # Process the nodes with in-degree 0
#         while q:
#             course = q.popleft()
#             topo.append(course)

#             # Update the in-degrees of neighbors and add to queue if in-degree becomes 0
#             for neighbor in graph[course]:
#                 indeg[neighbor] -= 1
#                 if indeg[neighbor] == 0:
#                     q.append(neighbor)

#         # If topological sort includes all courses, return True, else return False
#         return len(topo) == numCourses