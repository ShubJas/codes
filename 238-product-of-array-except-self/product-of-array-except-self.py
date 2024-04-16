class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        post= 1
        out = [1] * len(nums)
        for i in range(len(nums)):
            out[i] = pre
            pre *=nums[i]

        for i in range(len(nums)-1,-1,-1):
            out[i] *= post
            post*=nums[i]
        return out


        
