class Solution:
    def minChanges(self, s: str) -> int:
        
        count = 0
        n = len(s)


        for i in range(0,n,2):
            if s[i] != s[i+1]:
                count+=1
        
        return count