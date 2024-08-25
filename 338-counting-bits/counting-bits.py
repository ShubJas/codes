class Solution:
    def countBits(self, n: int) -> List[int]:

        # binary = list(bin(n)[2:]).count('1')

        result = []
        for i in range(n+1):
            result.append(list(bin(i)[2:]).count('1'))
        
        return result




        