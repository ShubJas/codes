class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        n = len(coins)


        prev = [0] * (amount + 1)


        prev[0] = 1
        

        for target in range(amount+1):
            if target % coins[0] == 0:
                prev[target] = 1
            else:
                prev[target] = 0
        

        for i in range(1,n):
            curr = [0] * (amount + 1)
            curr[0] = 1
            
            for target in range(1,amount+1):

                take =0
                if coins[i] <= target:
                    take = curr[target - coins[i]]
                
                ntake = prev[target]

                curr[target] = take + ntake
            prev = curr

    
        return prev[amount]


# class Solution:
#     def change(self, amount: int, coins: List[int]) -> int:

#         n = len(coins)


#         dp = [[0] * (amount + 1) for _ in range(n)]


#         for i in range(n):

#             dp[i][0] = 1
        

#         for target in range(amount+1):
#             if target % coins[0] == 0:
#                 dp[0][target] = 1
#             else:
#                 dp[0][target] = 0
        

#         for i in range(1,n):

#             for target in range(1,amount+1):

#                 take =0
#                 if coins[i] <= target:
#                     take = dp[i][target - coins[i]]
                
#                 ntake = dp[i-1][target]

#                 dp[i][target] = take + ntake

    
#         return dp[n-1][amount]


# class Solution:
#     def change(self, amount: int, coins: List[int]) -> int:

#         n = len(coins)


#         dp = [[-1] * (amount + 1) for _ in range(n)]
#         def calc(i,target):



#             if target == 0:
#                 return 1
            

#             if i == 0:
#                 if target % coins[0] == 0:
#                     return 1
#                 else:
#                     return 0

#             if dp[i][target] != -1:
#                 return dp[i][target]

#             take =0
#             if coins[i] <= target:
#                 take = calc(i,target - coins[i])
            
#             ntake = calc(i-1,target)

#             dp[i][target] = take + ntake
            

#             return dp[i][target]

        
#         return calc(n-1,amount)

# class Solution:
#     def change(self, amount: int, coins: List[int]) -> int:

#         n = len(coins)

#         def calc(i,target):



#             if target == 0:
#                 return 1
            

#             if i == 0:
#                 if target % coins[0] == 0:
#                     return 1
#                 else:
#                     return 0

#             take =0
#             if coins[i] <= target:
#                 take = calc(i,target - coins[i])
            
#             ntake = calc(i-1,target)

#             return take + ntake

        
#         return calc(n-1,amount)
        