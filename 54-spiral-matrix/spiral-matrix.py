class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        

        left = top = 0
        right = len(matrix[0]) - 1
        bottom = len(matrix) - 1
        result = []

        while left <= right and top <= bottom:



            for j in range(left,right+1):
                result.append(matrix[top][j])
            top+=1

            for i in range(top,bottom+1):
                result.append(matrix[i][right])
            right-=1

            if bottom>=top:
                for j in range(right,left-1,-1):
                    result.append(matrix[bottom][j])
                bottom-=1
            
            if left <= right:
                for i in range(bottom,top-1,-1):
                    result.append(matrix[i][left])
                left+=1
        

        return result
