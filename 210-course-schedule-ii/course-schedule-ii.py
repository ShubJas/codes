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
        zero_in_degree_queue = deque([i for i in range(numCourses) if in_degree[i] == 0])

        topo_order = []

        while zero_in_degree_queue:
            course = zero_in_degree_queue.popleft()
            topo_order.append(course)

            # Reduce in-degree for all the neighbors
            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                # If in-degree becomes zero, add to queue
                if in_degree[neighbor] == 0:
                    zero_in_degree_queue.append(neighbor)

        # Check if topological sort is possible
        if len(topo_order) == numCourses:
            return topo_order
        else:
            return []