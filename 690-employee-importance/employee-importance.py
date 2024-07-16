# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class Solution:
    def dfs(self, idx, emp_imp, emp_sub):
        # Add the importance of the current employee to the total
        self.total += emp_imp[idx]
        
        # If the employee has no subordinates, return
        if len(emp_sub[idx]) == 0:
            return 
        
        # Recursively call dfs for each subordinate
        for emp in emp_sub[idx]:
            self.dfs(emp, emp_imp, emp_sub)

    def getImportance(self, employees: List['Employee'], id: int) -> int:
        self.total = 0  # Initialize total importance
        
        # Dictionaries to store employee importance and subordinates
        emp_sub = defaultdict(list)
        emp_imp = defaultdict(int)
        
        # Populate the dictionaries with employee data
        for emp in employees:
            idx = emp.id
            emp_imp[idx] = emp.importance
            emp_sub[idx] = emp.subordinates

        # Start DFS from the given employee id
        self.dfs(id, emp_imp, emp_sub)
                
        return self.total  # Return the total importance


# # Definition for Employee.
# class Employee:
#     def __init__(self, id: int, importance: int, subordinates: List[int]):
#         self.id = id
#         self.importance = importance
#         self.subordinates = subordinates

# class Solution:
#     def getImportance(self, employees: List['Employee'], id: int) -> int:
#         self.total = 0  # Initialize total importance
        
#         # Dictionaries to store employee importance and subordinates
#         emp_sub = defaultdict(list)
#         emp_imp = defaultdict(int)
        
#         # Populate the dictionaries with employee data
#         for emp in employees:
#             idx = emp.id
#             emp_imp[idx] = emp.importance
#             emp_sub[idx] = emp.subordinates
        
#         # Initialize a stack with the starting employee id and its importance
#         stack = [(id, emp_imp[id])]
        
#         # Perform DFS using the stack
#         while stack:
#             idx, imp = stack.pop()  # Pop an employee id and its importance from the stack
#             self.total += imp  # Add the importance to the total
            
#             # If the employee has subordinates, add them to the stack
#             if len(emp_sub[idx]) != 0:
#                 for emp in emp_sub[idx]:
#                     stack.append((emp, emp_imp[emp]))
        
#         return self.total  # Return the total importance
