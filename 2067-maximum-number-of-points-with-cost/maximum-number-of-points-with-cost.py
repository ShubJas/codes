class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # Get the number of rows (r) and columns (c) in the points grid
        r, c = len(points), len(points[0])

        # Iterate through each row starting from the second row
        for i in range(1, r):
            # Create a temporary array 'right' to store the maximum points
            # achievable when moving right-to-left in the previous row
            right = [0] * c
            
            # Initialize the rightmost value of 'right' with the last column of the previous row
            right[-1] = points[i-1][-1]

            # Fill the 'right' array by calculating maximum points from right-to-left
            for j in range(c-2, -1, -1):
                # Calculate the maximum points by considering the right neighbor and moving left
                right[j] = max(right[j+1] - 1, points[i-1][j])

            # Initialize 'left' with the first column of the previous row
            left = points[i-1][0]

            # Update the first column of the current row
            # This considers the maximum between moving directly down or from the right
            points[i][0] = max(left, right[0]) + points[i][0]

            # Update the rest of the columns in the current row from left to right
            for j in range(1, c):
                # Update 'left' by considering the left neighbor and moving right
                left = max(left - 1, points[i-1][j])

                # Update the current cell by adding the maximum points
                # achievable from either left or right, plus the current cell's points
                points[i][j] = max(left, right[j]) + points[i][j]

        # The answer is the maximum value in the last row, which represents
        # the maximum points that can be collected from top to bottom
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