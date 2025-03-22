class Solution:
    def largestOddNumber(self, num: str) -> str:
        lo = -1
        for i in range(len(num)):
            if int(num[i]) % 2 != 0:
                lo = i
        
        if lo != -1:
            return num[:lo+1]
        else:
            return ''
