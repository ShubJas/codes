class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        n = len(matrix)
        m = len(matrix[0])

        prev = [-1] * m 

        for j in range(m):
            prev[j] = matrix[0][j]


        for i in range(1,n):
            curr = [-1] * m 
            for j in range(m):

                up_left = up_right = float('inf')
                up = prev[j]
                if j> 0:
                    up_left = prev[j-1]
                
                if j < m-1:
                    up_right = prev[j+1]
                
                curr[j] = matrix[i][j] + min(up,up_left,up_right)
            prev = curr

        return min(prev)


# class Solution:
#     def minFallingPathSum(self, matrix: List[List[int]]) -> int:
#         """
#         This function calculates the minimum falling path sum in a given n x n matrix.
#         A falling path starts at any element in the first row and chooses one element from each row.
#         The next row's chosen element must be in the column directly below or diagonally left/right.

#         Args:
#         - matrix: A list of lists of integers representing the matrix.

#         Returns:
#         - The minimum falling path sum.
#         """
        
#         n = len(matrix)  # Number of rows
#         m = len(matrix[0])  # Number of columns

#         # Initialize the dp array with -1 for all elements
#         dp = [[-1] * m for _ in range(n)]

#         # Base case: Fill the first row of dp with the first row of matrix
#         for j in range(m):
#             dp[0][j] = matrix[0][j]

#         # Fill the dp array from the second row to the last row
#         for i in range(1, n):
#             for j in range(m):
#                 # Initialize the possible path sums to infinity
#                 up_left = up_right = float('inf')
#                 # Directly above
#                 up = dp[i - 1][j]
#                 # Diagonally left above
#                 if j > 0:
#                     up_left = dp[i - 1][j - 1]
#                 # Diagonally right above
#                 if j < m - 1:
#                     up_right = dp[i - 1][j + 1]
                
#                 # The current cell's minimum path sum
#                 dp[i][j] = matrix[i][j] + min(up, up_left, up_right)

#         # The answer is the minimum value in the last row of the dp array
#         return min(dp[n - 1])

    

# class Solution:
#     def minFallingPathSum(self, matrix: List[List[int]]) -> int:

#         n = len(matrix)
#         m = len(matrix[0])


#         dp = [[-1] * m for _ in range(n)]


#         def calc(x,y):

#             if x<0 or y<0 or x>= n or y>=n:
#                 return float('inf')


#             if x == 0:
#                 return matrix[x][y]
            
#             if dp[x][y] != -1:
#                 return dp[x][y]
            

#             up = calc(x-1,y)
#             up_left = calc(x-1,y-1)
#             up_right = calc(x-1,y+1)


#             dp[x][y] = matrix[x][y] + min(up,up_left,up_right)

#             return dp[x][y]

#         min_sum = float('inf')
#         for j in range(m):
#             min_sum = min(min_sum,calc(n-1,j))
        

#         return min_sum

# class Solution:
#     def minFallingPathSum(self, matrix: List[List[int]]) -> int:

#         n = len(matrix)
#         m = len(matrix[0])

#         def calc(x,y):

#             if x<0 or y<0 or x>= n or y>=n:
#                 return float('inf')


#             if x == 0:
#                 return matrix[x][y]
            

#             up = calc(x-1,y)
#             up_left = calc(x-1,y-1)
#             up_right = calc(x-1,y+1)

#             return matrix[x][y] + min(up,up_left,up_right)

#         min_sum = float('inf')
#         for j in range(m):
#             min_sum = min(min_sum,calc(n-1,j))
        

#         return min_sum
        