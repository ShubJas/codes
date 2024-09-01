class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:

        if m * n != len(original):
            return []
        
        result = []
        for row in range(m):

            result.append(original[row*n : (row+1)* n])
        
        return result

# class Solution:
#     def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        
#         if len(original) != m * n:
#             return []

#         result = [[-1] * n for _ in range(m)]

#         for i in range(len(original)):
#             col = i % n
#             row = i // n
#             result[row][col] = original[i]

#         return result
