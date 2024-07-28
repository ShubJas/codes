class Solution:
    def maxProfit(self, prices: List[int]) -> int:


        n = len(prices)
        min_p = prices[0]
        profit = 0
        for i in range(1,n):
            profit = max(profit,prices[i]-min_p)
            min_p = min(min_p,prices[i])
        
        return profit

        