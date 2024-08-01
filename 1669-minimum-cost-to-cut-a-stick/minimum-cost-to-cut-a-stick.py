class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:

        len_cuts = len(cuts)
        
        cuts = [0] + cuts + [n]
        cuts.sort()

        nn = len(cuts)

        dp = [[0] * nn for _ in range(nn)]


        for i in range(nn-1,0,-1):

            for j in range(i,len_cuts+1):

                min_cost = float('inf')
                for k in range(i,j+1):

                    cost = dp[i][k-1] + dp[k+1][j] + cuts[j+1] - cuts[i-1]

                    min_cost = min(min_cost,cost)
                
                dp[i][j] = min_cost



        # def calc(i,j):

        #     if i > j:
        #         return 0

        #     if dp[i][j] != -1:
        #         return dp[i][j]

        #     min_cost = float('inf')
        #     for k in range(i,j+1):

        #         cost = calc(i,k-1) + calc(k+1,j) + cuts[j+1] - cuts[i-1]

        #         min_cost = min(min_cost,cost)
            
        #     dp[i][j] = min_cost

        #     return dp[i][j]
        
        return dp[1][len_cuts]

# i -> 1 to nn-1
# j -> len_cuts to i



# class Solution:
#     def minCost(self, n: int, cuts: List[int]) -> int:

#         len_cuts = len(cuts)
        
#         cuts = [0] + cuts + [n]
#         print(cuts)
#         cuts.sort()

#         nn = len(cuts)

#         dp = [[-1] * nn for _ in range(nn)]


#         def calc(i,j):

#             if i > j:
#                 return 0

#             if dp[i][j] != -1:
#                 return dp[i][j]

#             min_cost = float('inf')
#             for k in range(i,j+1):

#                 cost = calc(i,k-1) + calc(k+1,j) + cuts[j+1] - cuts[i-1]

#                 min_cost = min(min_cost,cost)
            
#             dp[i][j] = min_cost

#             return dp[i][j]
        
#         return calc(1,len_cuts)
        
