class Solution:
    def maxProfit(self, prices: List[int]) -> int: 

        n = len(prices)


        aheadbuy = ahead_nbuy = 0


        for i in range(n-1,-1,-1):

            curr_buy = max(- prices[i] + ahead_nbuy,aheadbuy)
            curr_nbuy = max(prices[i] + aheadbuy,ahead_nbuy)
            
            aheadbuy = curr_buy
            ahead_nbuy = curr_nbuy
        
        return aheadbuy


# class Solution:
#     def maxProfit(self, prices: List[int]) -> int: 

#         n = len(prices)

#         ahead = [-1] * 2 

#         for buy in range(2):
#             ahead[buy] = 0


#         # Reversed the indexs as opposite in tabulation ( also nth case covered)
#         for i in range(n-1,-1,-1):
#             curr = [-1] * 2 

#             for buy in range(2):

#                 if buy == 1:
#                     take = - prices[i] + ahead[0]
#                     ntake = ahead[1]
#                     result = max(take,ntake)
#                 else:
#                     sell = prices[i] + ahead[1]
#                     nsell = ahead[0]
#                     result = max(sell,nsell)
                
#                 curr[buy] = result
            
#             ahead = curr
        
#         return ahead[1]

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int: 

#         n = len(prices)

#         prev = [-1] * 2 

#         for buy in range(2):
#             prev[buy] = 0


#         # Reversed the indexs as opposite in tabulation ( also nth case covered)
#         for i in range(n-1,-1,-1):
#             curr = [-1] * 2 

#             for buy in range(2):

#                 if buy == 1:
#                     take = - prices[i] + prev[0]
#                     ntake = prev[1]
#                     result = max(take,ntake)
#                 else:
#                     sell = prices[i] + prev[1]
#                     nsell = prev[0]
#                     result = max(sell,nsell)
                
#                 curr[buy] = result
            
#             prev = curr
        
#         return prev[1]

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int: 

#         n = len(prices)

#         dp = [[-1] * 2 for _ in range(n+1)]

#         for buy in range(2):
#             dp[n][buy] = 0

        

#         # Reversed the indexs as opposite in tabulation ( also nth case covered)
#         for i in range(n-1,-1,-1):

#             for buy in range(2):

#                 if buy == 1:
#                     take = - prices[i] + dp[i+1][0]
#                     ntake = dp[i+1][1]
#                     result = max(take,ntake)
#                 else:
#                     sell = prices[i] + dp[i+1][1]
#                     nsell = dp[i+1][0]
#                     result = max(sell,nsell)
                
#                 dp[i][buy] = result
        
#         return dp[0][1]

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int: 

#         n = len(prices)

#         dp = [[-1] * 2 for _ in range(n)]

#         def calc(i,buy):

#             if i == n:
#                 return 0 # if we still have a stock( the money is already given)



#             if dp[i][buy] != -1:
#                 return dp[i][buy]


#             if buy == 1:
#                 take = - prices[i] + calc(i+1,0)
#                 ntake = calc(i+1,1)
#                 result = max(take,ntake)
#             else:
#                 sell = prices[i] + calc(i+1,1)
#                 nsell = calc(i+1,0)
#                 result = max(sell,nsell)
            
#             dp[i][buy] = result

#             return dp[i][buy] 
        
#         return calc(0,1)

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int: 

#         n = len(prices)  # Number of days (length of prices array)

#         def calc(i, buy):

#             # Base case: If we've processed all days, there's no profit to be made
#             if i == n:
#                 return 0  # If we still have a stock, the money is already given

#             if buy == 1:  # We are in a state where we can buy
#                 # Option 1: Buy the stock at current price and move to next day in sell state
#                 take = -prices[i] + calc(i + 1, 0)
#                 # Option 2: Do not buy the stock and move to next day in buy state
#                 ntake = calc(i + 1, 1)
#                 # Return the maximum profit between buying and not buying
#                 return max(take, ntake)
#             else:  # We are in a state where we can sell
#                 # Option 1: Sell the stock at current price and move to next day in buy state
#                 sell = prices[i] + calc(i + 1, 1)
#                 # Option 2: Do not sell the stock and move to next day in sell state
#                 nsell = calc(i + 1, 0)
#                 # Return the maximum profit between selling and not selling
#                 return max(sell, nsell)
        
#         # Start from day 0 in buy state and calculate the maximum profit
#         return calc(0, 1)
