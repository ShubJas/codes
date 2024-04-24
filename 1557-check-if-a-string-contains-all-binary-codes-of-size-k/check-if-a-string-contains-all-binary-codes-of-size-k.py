class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        hashset = set()
        for i in range(0,len(s)-k+1):
            hashset.add(s[i:i+k])
            if len(hashset) == math.pow(2,k):
                return True
        return False
        

        