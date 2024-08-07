class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # Initialize a dictionary to map each manager to their respective subordinates
        manager_emp = defaultdict(list)  # boss: employees
        for i, m in enumerate(manager):
            if m != -1:
                manager_emp[m].append(i)

        # Initialize a queue for BFS with the headID and initial inform time 0
        q = deque([(headID, 0)])
        maxT = 0  # Variable to keep track of the maximum time required to inform all employees
        
        while q:
            curr, time = q.popleft()  # Dequeue the current employee and the time taken to inform them
            maxT = max(maxT, time)  # Update the maximum time if the current time is greater
            
            # Iterate through all subordinates of the current employee
            for emp in manager_emp[curr]:
                # Enqueue each subordinate with the updated inform time
                q.append((emp, time + informTime[curr]))

        return maxT  # Return the maximum time required to inform all employees




        return maxT



# class Solution:
#     def dfs(self, idx, manager_emp, informTime, memo):
#         # If the inform time for this employee is already calculated, return it
#         if memo[idx] != -1:
#             return memo[idx]
        
#         # If the current employee has no subordinates (leaf node)
#         if idx not in manager_emp:
#             memo[idx] = 0  # Base case: no time needed to inform subordinates
#             return 0
        
#         max_time = 0
#         # Check all subordinates of the current manager (idx)
#         for i in manager_emp[idx]:
#             # Recursively call dfs for each subordinate and update max_time
#             max_time = max(max_time, self.dfs(i, manager_emp, informTime, memo))
        
#         # Calculate the total inform time for this employee and store it in memo
#         memo[idx] = max_time + informTime[idx]
#         return memo[idx]

#     def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
#         # Initialize memoization list with -1 (indicating uncalculated inform times)
#         memo = [-1] * n
#         # Initialize a dictionary to map each manager to their respective subordinates
#         manager_emp = defaultdict(list)  # boss: employees
        
#         # Populate the manager_emp dictionary
#         for i, m in enumerate(manager):
#             if m != -1:
#                 manager_emp[m].append(i)

#         # Calculate the total inform time starting from the headID
#         return self.dfs(headID, manager_emp, informTime, memo)
