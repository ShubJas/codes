class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        
        # before we start,(-1) index, the parity is 0 ( edgecase for handeling 1st letter combinations)
        parity_index = {0:-1}

        # For bitmasking (parity)
        vovels = 'aeiou'

        # acts as currsum
        parity = 0

        longest = 0

        for i,ch in enumerate(s):


            if ch in vovels:
                index = vovels.index(ch)

                parity ^= 1 << index

            if parity in parity_index:
                longest = max(longest,i - parity_index[parity])
            else:
                parity_index[parity] = i
        
        return longest





        

            