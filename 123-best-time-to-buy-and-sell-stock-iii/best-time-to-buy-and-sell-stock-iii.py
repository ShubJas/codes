class Solution:
    def maxProfit(self, prices: List[int]) -> int:


        
        n = len(prices)
        
        dp = [[[-1 for _ in range(3)] for _ in range(2)] for _ in range(n)]

        def calc(i,buy,count):


            if count == 2 or i == n:
                return 0
            

            if dp[i][buy][count] != -1:
                return dp[i][buy][count]

            if buy == 1:
                take = -prices[i] + calc(i+1,0,count)
                ntake = calc(i+1,1,count)
                result = max(take,ntake)
            
            else:
                sell = prices[i] + calc(i+1,1,count+1)
                nsell = calc(i+1,0,count)
                result = max(sell,nsell)
            
            dp[i][buy][count] = result
            return dp[i][buy][count]
        
        return calc(0,1,0)


# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:


        
#         n = len(prices)

#         def calc(i,buy,count):


#             if count == 2 or i == n:
#                 return 0


#             if buy == 1:
#                 take = -prices[i] + calc(i+1,0,count)
#                 ntake = calc(i+1,1,count)
#                 return max(take,ntake)
            
#             else:
#                 sell = prices[i] + calc(i+1,1,count+1)
#                 nsell = calc(i+1,0,count)
#                 return max(sell,nsell)
        
#         return calc(0,1,0)
        
        