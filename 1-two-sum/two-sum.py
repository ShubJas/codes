class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap = {}
        for i,n in enumerate(nums):
            ai=target-n
            if ai in hashmap:
                return [hashmap[ai],i]
            hashmap[n]=i
        return
            
        
        # we have to return the indeices in the original array so we cant sort
        # s=0
        # l=len(nums)-1
        # nums.sort()
        # while(s<l):
        #     if((nums[s]+nums[l])>target):
        #         l=l-1
        #     elif((nums[s]+nums[l])<target):
        #         s=s+1
        #     else:
        #         return [s,l]

        