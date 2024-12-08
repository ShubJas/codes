class Solution:
    def check(self, nums: List[int]) -> bool:

        vio = 0
        n = len(nums)
        for i in range(len(nums)):

            if nums[i] > nums[(i+1)%n]:
                vio+=1
            
        return vio<=1



        