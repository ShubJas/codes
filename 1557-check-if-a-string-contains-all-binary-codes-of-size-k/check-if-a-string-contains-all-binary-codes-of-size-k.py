class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        hashset = set()
        count =0
        for i in range(0,len(s)):
            if s[i:i+k] not in hashset and i+k <= len(s):
                print(s[i:i+k])
                hashset.add(s[i:i+k])
                count+=1
            if count == math.pow(2,k):
                return True
        return False
        

        