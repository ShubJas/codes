# Cycle detection 
class Solution:
    def dfs(self,i,graph,dp):


        if dp[i] !=0:
            return dp[i] == 1

        dp[i] = -1

        for con in graph[i]:
            if not self.dfs(con,graph,dp):
                return False
        
        dp[i] = 1
        return True

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        result = []
        n = len(graph)
        dp = [0] * n
        for i in range(n):
            if self.dfs(i,graph,dp):
                result.append(i)


        return result
