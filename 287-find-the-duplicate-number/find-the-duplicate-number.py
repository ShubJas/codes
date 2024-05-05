class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ctr = Counter(nums)

        for value,count in ctr.items():
            if count>1:
                return value 
        