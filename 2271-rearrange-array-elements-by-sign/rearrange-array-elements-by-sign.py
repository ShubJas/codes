class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        pos = []
        neg = []

        for n in nums:
            if n > 0:
                pos.append(n)
            else:
                neg.append(n)

        nums = []
        for x,y in zip(pos,neg):
            nums.append(x)
            nums.append(y)
        
        return nums