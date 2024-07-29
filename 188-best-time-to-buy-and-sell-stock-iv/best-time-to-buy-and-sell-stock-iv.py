class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
    
        
                
        n = len(prices)
        
        ahead = [[0 for _ in range(k+1)] for _ in range(2)] 

        for i in range(n-1,-1,-1):
            curr = [[0 for _ in range(k+1)] for _ in range(2)] 
            for buy in range(2):
                
                for count in range(k-1,-1,-1):
                    if buy == 1:
                        take = -prices[i] + ahead[0][count]
                        ntake = ahead[1][count]
                        result = max(take,ntake)
                    
                    else:
                        sell = prices[i] + ahead[1][count+1]
                        nsell = ahead[0][count]
                        result = max(sell,nsell)
                    
                    curr[buy][count] = result
            ahead = curr
        
        return ahead[1][0]


# class Solution:
#     def maxProfit(self, k: int, prices: List[int]) -> int:
    
        
#         n = len(prices)

#         def calc(i,buy,count):


#             if count == k or i == n:
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
        