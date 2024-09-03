class Solution:
    def getLucky(self, s: str, k: int) -> int:
        


        string = ''.join(str(ord(ch)-96) for ch in s)

        S = sum(int(digit) for digit in string)

        for _ in range(k-1):
            S = sum(int(digit) for digit in str(S))
        
        return S
