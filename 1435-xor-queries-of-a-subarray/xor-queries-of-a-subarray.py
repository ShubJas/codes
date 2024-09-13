class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        
        prefix_xor = []
        xor = 0
        result =  []
        for n in arr:
            xor ^= n
            prefix_xor.append(xor)
        
        for i, j in queries:
            if i != 0:
                result.append(prefix_xor[i-1]^prefix_xor[j])
            else:
                result.append(prefix_xor[j])
        
        return result

# Brute
# class Solution:
#     def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        

#         result = []
#         for i,j in queries:
#             xor = 0
#             for n in arr[i:j+1]:
#                 xor ^= n
#             result.append(xor)
        
#         return result