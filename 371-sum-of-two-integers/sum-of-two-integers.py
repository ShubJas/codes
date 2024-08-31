class Solution:
    def getSum(self, a: int, b: int) -> int:
        xor = a ^ b 
        xor += (a & b) << 1

        return xor

