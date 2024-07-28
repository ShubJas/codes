class Solution:
    def maxProfit(self, prices: List[int]) -> int:


        n = len(prices)
        min_p = float('inf')
        profit = 0
        for i in range(1,n):
            min_p = min(min_p,prices[i-1])
            profit = max(profit,prices[i]-min_p)
        
        return profit

        