class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        

        l = t = 0
        r = len(matrix[0])
        b = len(matrix)
        result = []
        while l<r and t<b:


            for j in range(l,r):
                result.append(matrix[t][j])
            t+=1

            for i in range(t,b):
                result.append(matrix[i][r-1])
            r-=1


            if l == r or t == b:
                break
                
            for j in range(r-1,l-1,-1):
                result.append(matrix[b-1][j])
            b-=1
            
            for i in range(b-1,t-1,-1):
                result.append(matrix[i][l])
            l+=1

        
        return result

