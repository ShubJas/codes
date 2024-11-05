class Solution:
    def minChanges(self, s: str) -> int:
        
        # hm = {'1':0,'0':0}
        count = 0
        n = len(s)


        for i in range(0,n,2):


            if s[i] == s[i+1]:
                continue
            elif s[i] != s[i+1]:
                count+=1
        
        return count