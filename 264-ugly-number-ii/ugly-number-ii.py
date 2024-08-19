class Solution:
    def nthUglyNumber(self, n: int) -> int:
        
        i5 = i2 = i3 = 0

        dp = [1] * n
        for i in range(1,n):

            p2 = dp[i2]*2
            p3 = dp[i3]* 3
            p5 = dp[i5] * 5

            dp[i] = min(p2,min(p3,p5))

            if dp[i] == p2:
                i2+=1
            if dp[i] == p3:
                i3+=1
            if dp[i] == p5:
                i5+=1
        

        return dp[n-1]
                
