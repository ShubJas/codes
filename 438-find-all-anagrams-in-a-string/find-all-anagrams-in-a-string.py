class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        hashmap1 = defaultdict(int)
        hashmap2 = defaultdict(int)
        result = []
        for c in p:
            hashmap1[c]+= 1
        winlength = len(p)
        for c in s[:winlength]:
            hashmap2[c]+=1
        if hashmap1==hashmap2:
            result.append(0)
        for i in range(winlength,len(s)):
            hashmap2[s[i]]+=1
            if hashmap2[s[i-winlength]]==1:
                del hashmap2[s[i-winlength]]
            else:
                hashmap2[s[i-winlength]]-=1

            
            
            
            if hashmap1 == hashmap2:
                result.append(i-winlength+1)
        return result