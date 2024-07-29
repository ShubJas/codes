class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:

        n = len(prices)

        dp = [[-1] * 2 for _ in range(n)]



        def calc(i,buy):

            if i == n:
                return 0

            if dp[i][buy] != -1:
                return dp[i][buy]

            if buy == 1:
                take = -prices[i] + calc(i+1,0)
                ntake = calc(i+1,1)
                result =  max(take,ntake)
            else:
                sell = prices[i] - fee + calc(i+1,1)
                nsell = calc(i+1,0)
                result =  max(sell,nsell)
            
            dp[i][buy] = result
            return dp[i][buy]
            
            

        
        return calc(0,1)


# class Solution:
#     def maxProfit(self, prices: List[int], fee: int) -> int:

#         n = len(prices)


#         def calc(i,buy):

#             if i == n:
#                 return 0

#             if buy == 1:
#                 take = -prices[i] + calc(i+1,0)
#                 ntake = calc(i+1,1)
#                 return max(take,ntake)
#             else:
#                 sell = prices[i] - fee + calc(i+1,1)
#                 nsell = calc(i+1,0)
#                 return max(sell,nsell)
        
#         return calc(0,1)