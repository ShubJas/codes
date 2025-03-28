# Intuition - start with bursting last Baloon
class Solution:
    def maxCoins(self, nums: List[int]) -> int:


        nlen = len(nums)


        nums = [1] + nums + [1]

        n = len(nums)

        dp = [[0] * n for _ in range(n)]


        for i in range(nlen,0,-1):

            for j in range(i,nlen+1):

                max_coins = 0
                for k in range(i,j+1):


                    coins = nums[i-1] * nums[k] * nums[j+1] + dp[i][k-1] + dp[k+1][j]
                    max_coins = max(max_coins,coins)

                dp[i][j] = max_coins


        return dp[1][nlen]


# i -> 1 to nlen
# j -> nlen to i



# class Solution:
#     def maxCoins(self, nums: List[int]) -> int:


#         nlen = len(nums)


#         nums = [1] + nums + [1]

#         n = len(nums)

#         dp = [[-1] * n for _ in range(n)]

#         def calc(i,j):

#             if i > j:
#                 return 0
            

#             if dp[i][j] != -1:
#                 return dp[i][j]

#             max_coins = 0
#             for k in range(i,j+1):


#                 coins = nums[i-1] * nums[k] * nums[j+1] + calc(i,k-1) + calc(k+1,j)
#                 max_coins = max(max_coins,coins)

#             dp[i][j] = max_coins

#             return  dp[i][j]


#         return calc(1,nlen)


# class Solution:
#     def maxCoins(self, nums: List[int]) -> int:


#         nlen = len(nums)


#         nums = [1] + nums + [1]

#         n = len(nums)


#         def calc(i,j):

#             if i > j:
#                 return 0

#             max_coins = 0
#             for k in range(i,j+1):


#                 coins = nums[i-1] * nums[k] * nums[j+1] + calc(i,k-1) + calc(k+1,j)
#                 max_coins = max(max_coins,coins)


#             return max_coins 


        



#         return calc(1,nlen)






            




        