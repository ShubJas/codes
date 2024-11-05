class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        

        n = len(grid)
        m = len(grid[0])
        dp = [[-1] * m for _ in range(n)]

        def calc(i,j):

            if dp[i][j] != -1:
                return dp[i][j] 
                
            curr = grid[i][j]
            u = d = s = 0
            if i-1>=0 and j+1<m and grid[i-1][j+1] > curr:
                u =  1 + calc(i-1,j+1)
            if i+1<n and j+1<m and grid[i+1][j+1] > curr:
                d = 1 + calc(i+1,j+1)
            if j+1<m and grid[i][j+1] > curr:
                s = 1 + calc(i,j+1)
            
            dp[i][j] = max(u,d,s)
            return dp[i][j]

        maxi = 0 
        for i in range(n):
            maxi = max(maxi,calc(i,0))


        return maxi