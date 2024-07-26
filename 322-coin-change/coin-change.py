# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         n = len(coins)

#         prev = [-1] * (amount + 1) 


#         for amnt in range(amount+1):
#             if amnt % coins[0] == 0: 
#                 prev[amnt] = amnt // coins[0]
#             else:
#                 prev[amnt] = float('inf')
        
#         for i in range(1,n):
#             for amnt in range(amount+1):

#                 take = float('inf')
#                 if coins[i] <= amnt:
#                     take = 1 + prev[amnt - coins[i]]

#                 ntake = prev[amnt]

#                 prev[amnt] = min(take, ntake)

#         ans = prev[amount]
#         return ans if ans != float('inf') else -1


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)

        prev = [-1] * (amount + 1) 


        for amnt in range(amount+1):
            if amnt % coins[0] == 0: 
                prev[amnt] = amnt // coins[0]
            else:
                prev[amnt] = float('inf')
        
        for i in range(1,n):
            curr = [-1] * (amount + 1) 
            for amnt in range(amount+1):

                take = float('inf')
                if coins[i] <= amnt:
                    take = 1 + curr[amnt - coins[i]]

                ntake = prev[amnt]

                curr[amnt] = min(take, ntake)
            prev = curr

        ans = prev[amount]
        return ans if ans != float('inf') else -1


# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         n = len(coins)

#         dp = [[-1] * (amount + 1) for _ in range(n)]


#         for amnt in range(amount+1):
#             if amnt % coins[0] == 0: 
#                 dp[0][amnt] = amnt // coins[0]
#             else:
#                 dp[0][amnt] = float('inf')
        
#         for i in range(1,n):
#             for amnt in range(amount+1):

#                 take = float('inf')
#                 if coins[i] <= amnt:
#                     take = 1 + dp[i][amnt - coins[i]]

#                 ntake = dp[i - 1][amnt]

#                 dp[i][amnt] = min(take, ntake)

#         ans = dp[n - 1][amount]
#         return ans if ans != float('inf') else -1


# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         n = len(coins)

#         dp = [[-1] * (amount + 1) for _ in range(n)]

#         def calc(i, amount):
#             if amount == 0:
#                 return 0
            
#             if i == 0:
#                 if amount % coins[0] == 0:
#                     return  amount // coins[0]
#                 else:
#                     return float('inf')
            
            
#             if dp[i][amount] != -1:
#                 return dp[i][amount]


#             take = float('inf')
#             if coins[i] <= amount:
#                 take = 1 + calc(i, amount - coins[i])

#             ntake = calc(i - 1, amount)

#             dp[i][amount] = min(take, ntake)
#             return dp[i][amount]

#         ans = calc(n - 1, amount)
#         return ans if ans != float('inf') else -1

# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         n = len(coins)

#         def calc(i, amount):
#             if amount == 0:  # this is not required as  if coins[i] <= amount: #                 take = 1 + calc(i, amount - coins[i]) handels it

#                 return 0
            
            # if i == 0:
            #     if amount % coins[0] == 0:
            #         return  amount // coins[0]
            #     else:
            #         return float('inf')
            

#             take = float('inf')
#             if coins[i] <= amount:
#                 take = 1 + calc(i, amount - coins[i])

#             ntake = calc(i - 1, amount)

#             return min(take, ntake)

#         ans = calc(n - 1, amount)
#         return ans if ans != float('inf') else -1