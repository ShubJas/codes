class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        
        n = len(triangle)
                
        prev = [-1 for i in range(n)]
        

        prev[0] = triangle[0][0]

        for i in range(1,n):
            curr = [-1 for i in range(n)]
            for j in range(i+1):
                up = up_left = float('inf')
                if i>j:
                    up = prev[j]
                if j> 0 :
                    up_left = prev[j-1]

                curr[j] = triangle[i][j] + min(up,up_left)
            prev = curr
        return min(prev)
        

# class Solution:
#     def minimumTotal(self, triangle: List[List[int]]) -> int:

        
#         n = len(triangle)
                
#         dp = [[-1 for j in range(0,i+1)] for i in range(n)]
        

#         dp[0][0] = triangle[0][0]

#         for i in range(1,n):
#             for j in range(i+1):
#                 up = up_left = float('inf')
#                 if i>j:
#                     up = dp[i-1][j]
#                 if j> 0 :
#                     up_left = dp[i-1][j-1]

#                 dp[i][j] = triangle[i][j] + min(up,up_left)
                
#         return min(dp[n-1])

# class Solution:
#     def minimumTotal(self, triangle: List[List[int]]) -> int:

        
#         n = len(triangle)
#         # for i in range(n):
#         #     for j in range(0,i+1):
                
#         dp = [[-1 for j in range(0,i+1)] for i in range(n)]
        
        
#         def calc(x,y):

#             if x == n-1:
#                 return triangle[x][y]
            
#             if dp[x][y] != -1:
#                 return dp[x][y]
#             # if x < 0 or y < 0 or y > x:
#             #     return float('inf')

            
#             down = calc(x+1,y)

#             down_right = calc(x+1,y+1)

#             dp[x][y] = triangle[x][y] + min(down,down_right)

#             return dp[x][y]
#         return calc(0,0)


# class Solution:
#     def minimumTotal(self, triangle: List[List[int]]) -> int:

        
#         n = len(triangle)
#         # for i in range(n):
#         #     for j in range(0,i+1):
                
            
        
#         def calc(x,y):

#             if x == n-1:
#                 return triangle[x][y]
            

#             # if x < 0 or y < 0 or y > x:
#             #     return float('inf')

            
#             down = calc(x+1,y)

#             down_right = calc(x+1,y+1)

#             return triangle[x][y] + min(down,down_right)
        

        
#         return calc(0,0)



# class Solution:
#     def minimumTotal(self, triangle: List[List[int]]) -> int:

        
#         n = len(triangle)
#         # for i in range(n):
#         #     for j in range(0,i+1):
                

        
#         def calc(x,y):

#             if x == 0 and  y ==0:
#                 return triangle[0][0]
            

#             if x < 0 or y < 0 or y > x:
#                 return float('inf')

            
#             up = calc(x-1,y)

#             up_left = calc(x-1,y-1)

#             return triangle[x][y] + min(up,up_left)
        
#         min_path = float('inf')

#         for i in range(n):
#             min_path = min(min_path,calc(n-1,i))
        
#         return min_path