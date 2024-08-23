class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:

            n  &= n-1
            count+=1
        
        return count




'''
Suppose n = 12, which in binary is 1100.
n - 1 = 11, which in binary is 1011.
n & (n - 1) = 1100 & 1011 = 1000 (in binary), which is 8 in decimal.
The lowest set bit has been removed, and now n is 1000.

'''

# class Solution:
#     def hammingWeight(self, n: int) -> int:
        
#         return list(bin(n)[2:]).count('1')