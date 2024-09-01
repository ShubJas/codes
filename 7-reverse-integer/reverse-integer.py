class Solution:
    def reverse(self, x: int) -> int:

        rev = int(''.join([ch for ch in reversed(str(x) if x >= 0 else str(x)[1:])]))
        
        if rev > 2**31 - 1 :
            return 0

        return rev if x >=0 else -rev  