class Solution:
    def maxProfit(self, prices: List[int]) -> int:


        n = len(prices)

        ahead2 = [0] * 2 
        ahead1 = [0] * 2 



        for i in range(n-1,-1,-1):
            curr = [0] * 2 
            
            for buy in range(2):

                if buy == 1:

                    take = -prices[i] + ahead1[0]
                    ntake = ahead1[1]
                    result = max(take,ntake)
                
                else:
                    sell = prices[i] + ahead2[1] # cant buy next day
                    nsell = ahead1[0]
                    result = max(sell,nsell)
                curr[buy] = result    

            ahead2 = ahead1
            ahead1 = curr 

        return ahead1[1]

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:


#         n = len(prices)

#         dp = [[0] * 2 for _ in range(n+2)]


#         for i in range(n-1,-1,-1):

#             for buy in range(2):

#                 if buy == 1:

#                     take = -prices[i] + dp[i+1][0]
#                     ntake = dp[i+1][1]
#                     result = max(take,ntake)
                
#                 else:
#                     sell = prices[i] + dp[i+2][1] # cant buy next day
#                     nsell = dp[i+1][0]
#                     result = max(sell,nsell)
#                 dp[i][buy] = result     

#         return dp[0][1]

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:


#         n = len(prices)

#         dp = [[-1] * 2 for _ in range(n+1)]


#         def calc(i,buy):


#             if i >= n:
#                 return 0


#             if dp[i][buy] != -1:
#                 return dp[i][buy]


#             if buy == 1:

#                 take = -prices[i] + calc(i+1,0)
#                 ntake = calc(i+1,1)
#                 result = max(take,ntake)
            
#             else:
#                 sell = prices[i] + calc(i+2,1) # cant buy next day
#                 nsell = calc(i+1,0)
#                 result = max(sell,nsell)
#             dp[i][buy] = result 

#             return dp[i][buy] 

#         return calc(0,1)


# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:


#         n = len(prices)

#         def calc(i,buy):


#             if i >= n:
#                 return 0


#             if buy == 1:

#                 take = -prices[i] + calc(i+1,0)
#                 ntake = calc(i+1,1)
#                 return max(take,ntake)
            
#             else:
#                 sell = prices[i] + calc(i+2,1) # cant buy next day
#                 nsell = calc(i+1,0)
#                 return max(sell,nsell)
        

#         return calc(0,1)

        