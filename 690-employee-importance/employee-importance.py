"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def dfs(self,idx,emp_imp,emp_sub):

        self.total +=emp_imp[idx]
        
        if len(emp_sub[idx]) == 0:
            return 
        
        for emp in emp_sub[idx]:
            self.dfs(emp,emp_imp,emp_sub)

    def getImportance(self, employees: List['Employee'], id: int) -> int:
        self.total =0
        emp_sub = defaultdict(list)
        emp_imp = defaultdict(list)
        for emp in employees:
            idx = emp.id
            emp_imp[idx] = emp.importance
            emp_sub[idx] = emp.subordinates

        self.dfs(id,emp_imp,emp_sub)
                
        return self.total
