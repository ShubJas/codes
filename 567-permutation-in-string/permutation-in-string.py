#  More optimal ( no hashmap comparison)

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)
        
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1
            
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            
            l += 1
        
        return matches == 26





# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         hashmap1 = defaultdict(int)
#         hashmap2 =  defaultdict(int)
#         for c in s1:
#             hashmap1[c]+=1
        
#         winlength=len(s1)

#         for c in s2[:winlength]:
#             hashmap2[c]+=1
        
#         if hashmap1 == hashmap2:
#             return True
        
#         for i in range(winlength,len(s2)):
#             hashmap2[s2[i]]+=1
#             if hashmap2[s2[i-winlength]] == 1:
#                 del hashmap2[s2[i-winlength]]
#             else:
#                 hashmap2[s2[i-winlength]]-=1
            
#             if hashmap1 == hashmap2:
#                 return True
#         return False