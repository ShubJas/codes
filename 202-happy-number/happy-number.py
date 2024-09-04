class Solution:
    def isHappy(self, n: int) -> bool:
        

        seen = set()

        while n not in seen:
            seen.add(n)
            n = sum(int(digit) ** 2 for digit in str(n))
            if n == 1:
                return True
        
        return False


