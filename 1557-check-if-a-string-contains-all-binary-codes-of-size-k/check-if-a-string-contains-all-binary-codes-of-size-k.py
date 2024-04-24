class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        hashset = set()
        totalpsbl = 2**k
        for i in range(0,len(s)-k+1):
            hashset.add(s[i:i+k])
            if len(hashset) == totalpsbl:
                return True
        return False
        

        