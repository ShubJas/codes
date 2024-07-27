class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        n = len(coins)


        dp = [[-1] * (amount + 1) for _ in range(n)]
        def calc(i,target):



            if target == 0:
                return 1
            

            if i == 0:
                if target % coins[0] == 0:
                    return 1
                else:
                    return 0

            if dp[i][target] != -1:
                return dp[i][target]

            take =0
            if coins[i] <= target:
                take = calc(i,target - coins[i])
            
            ntake = calc(i-1,target)

            dp[i][target] = take + ntake
            

            return dp[i][target]

        
        return calc(n-1,amount)



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
        