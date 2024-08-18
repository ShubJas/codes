class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:


        n = len(points)
        m = len(points[0])
        


        for r in range(1,n):

            right = [0] * m

            right[-1] = points[r-1][-1]
            for c in range(m-2,-1,-1):
                right[c] = max(right[c+1]-1,points[r-1][c])
            
            left = points[r-1][0]
            points[r][0] = max(left,right[0]) + points[r][0]

            for c in range(1,m):
                left = max(left-1,points[r-1][c])
                points[r][c] = max(left,right[c]) + points[r][c]

        return max(points[-1])   







# class Solution:
#     def maxPoints(self, points: List[List[int]]) -> int:
        
#         n = len(points)
#         m = len(points[0])

#         ahead = [0] * m

#         for r in range(n-1,-1,-1):
#             curr = [0] * m        
#             for c in range(m-1,-1,-1):
#                 maxi = -float('inf')
#                 for j in range(m):
#                     point = points[r][j] + ahead[j]
#                     if r>0:
#                         point-=abs(j-c)
#                     maxi = max(maxi,point)
                
#                 curr[c] = maxi
#             ahead = curr
        
#         return max(ahead)


# #  r-> 0 to n-1
# #  c ->0 to m-1
# class Solution:
#     def maxPoints(self, points: List[List[int]]) -> int:
        
#         n = len(points)
#         m = len(points[0])

#         dp = [[0] * m for _ in range(n+1)]

#         for r in range(n-1,-1,-1):

#             for c in range(m-1,-1,-1):
#                 maxi = -float('inf')
#                 for j in range(m):
#                     point = points[r][j] + dp[r+1][j]
#                     if r>0:
#                         point-=abs(j-c)
#                     maxi = max(maxi,point)
                
#                 dp[r][c] = maxi
        
#         return max(dp[0])


# class Solution:
#     def maxPoints(self, points: List[List[int]]) -> int:
        
#         n = len(points)
#         m = len(points[0])

#         dp = [[-1] * m for _ in range(n+1)]


#         def calc(r,c):

#             if r == n:
#                 return 0
            
#             if dp[r][c] != -1:
#                 return dp[r][c]

#             maxi = -float('inf')
#             for j in range(m):
#                 point = points[r][j] + calc(r+1,j)
#                 if r>0:
#                     point-=abs(j-c)
#                 maxi = max(maxi,point)
            
#             dp[r][c] = maxi
#             return dp[r][c]
        
#         return calc(0,-1)