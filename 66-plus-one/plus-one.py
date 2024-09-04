class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        

        digits = ''.join(str(n) for n in digits)
        digits = [int(digit) for digit in list(str(int(digits)+1))]

        return digits