class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Initialize in-degree array and adjacency list
        indeg = [0] * numCourses
        graph = defaultdict(list)

        # Build the graph and update in-degrees
        for course, pre in prerequisites:
            graph[pre].append(course)
            indeg[course] += 1

        # Initialize the queue with all nodes having in-degree 0
        q = deque([i for i in range(numCourses) if indeg[i] == 0])
        topo = []

        # Process the nodes with in-degree 0
        while q:
            course = q.popleft()
            topo.append(course)

            # Update the in-degrees of neighbors and add to queue if in-degree becomes 0
            for neighbor in graph[course]:
                indeg[neighbor] -= 1
                if indeg[neighbor] == 0:
                    q.append(neighbor)

        # If topological sort includes all courses, return True, else return False
        return len(topo) == numCourses