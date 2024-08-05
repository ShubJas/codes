class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:

        count = defaultdict(int)

        for c in arr:
            count[c] += 1
        s = 0
        for c,cnt in count.items():
            if cnt == 1:
                s+=1
            if s == k:
                return c
        
        return ''

