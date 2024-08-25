'''
Even i: If i is even, then its binary representation is simply the binary representation of i // 2 shifted left by one bit (which is equivalent to multiplying by 2). Shifting left by one bit does not add any new 1's. Therefore, result[i] = result[i // 2].

Example:
4 (binary: 100) is 2 (binary: 10) shifted left by one bit. The count of 1's is the same: 1.
result[4] = result[2] = 1.
Odd i: If i is odd, then its binary representation is the same as i // 2 shifted left by one bit, plus a 1 in the least significant bit (rightmost position). Therefore, result[i] = result[i // 2] + 1.

Example:
5 (binary: 101) is 2 (binary: 10) shifted left by one bit, with an additional 1 added at the end. Therefore, result[5] = result[2] + 1 = 1 + 1 = 2.


'''
class Solution:
    def countBits(self, n: int) -> List[int]:

        if n==0:
            return [0]
        if n == 1:
            return [0,1]
        
        result = [0,1]
        
        for i in range(2,n+1):
            if i % 2 == 0:
                result.append(result[i//2])
            else:
                result.append(result[i//2] + 1)
        
        return result
        



# class Solution:
#     def countBits(self, n: int) -> List[int]:


#         result = []
#         for i in range(n+1):
#             result.append(list(bin(i)[2:]).count('1'))
        
#         return result