class Solution:
    def fib(self, n: int) -> int:

        dp = [-1] * (n+1)
        def fibbo(i):
            
            if i<=1:
                return i
            
            if dp[i] != -1:
                return dp[i]
            
            dp[i] = fibbo(i-1) + fibbo(i-2)

            return dp[i] 
        

        return fibbo(n)