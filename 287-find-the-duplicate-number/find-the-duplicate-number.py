class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        hashset = {}

        for val in nums:
            hashset[val] = hashset.get(val,0) + 1
        
        for val ,  count in hashset.items():
            if count >1:
                return val
        
        
        
        
        
        
        # ctr = Counter(nums)

        # for value,count in ctr.items():
        #     if count>1:
        #         return value 
        