class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashmap1 = defaultdict(int)
        hashmap2 =  defaultdict(int)
        for c in s1:
            hashmap1[c]+=1
        
        winlength=len(s1)

        for c in s2[:winlength]:
            hashmap2[c]+=1
        
        if hashmap1 == hashmap2:
            return True
        
        for i in range(winlength,len(s2)):
            hashmap2[s2[i]]+=1
            if hashmap2[s2[i-winlength]] == 1:
                del hashmap2[s2[i-winlength]]
            else:
                hashmap2[s2[i-winlength]]-=1
            
            if hashmap1 == hashmap2:
                return True
        return False