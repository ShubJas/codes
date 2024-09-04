class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        carry = 1
        digits = digits[::-1]
        i = 0
        n = len(digits)
        while carry and i<n:
            digit = digits[i] + carry 
            carry = digit // 10
            i+=1
        
        if carry:
            digits.append(1)
        
        return digits[::-1]





class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        

        digits = ''.join(str(n) for n in digits)
        digits = [int(digit) for digit in list(str(int(digits)+1))]

        return digits