class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        hashmap = defaultdict(int)
        count = 0
        for c in s[:3]:
            hashmap[c]+=1
        
        if len(hashmap)==3:
            count+=1
        
        for i in range(3,len(s)):
            hashmap[s[i]]+=1
            if hashmap[s[i-3]]==1:
                del hashmap[s[i-3]]
            else:
                hashmap[s[i-3]]-=1
            if len(hashmap) == 3:
                count+=1
        return count
        