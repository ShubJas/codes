class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        hashmap1 = defaultdict(int)
        hashmap2 = defaultdict(int)
        result = []
        for c in p:
            hashmap1[c]= hashmap1.get(c,0) + 1
        
        for c in s[:len(p)]:
            hashmap2[c]+=1
        if hashmap1==hashmap2:
            result.append(0)
        for i in range(len(p),len(s)):
            hashmap2[s[i]]+=1
            if hashmap2[s[i-len(p)]]==1:
                del hashmap2[s[i-len(p)]]
            else:
                hashmap2[s[i-len(p)]]-=1

            
            
            
            if hashmap1 == hashmap2:
                result.append(i-len(p)+1)
        return result