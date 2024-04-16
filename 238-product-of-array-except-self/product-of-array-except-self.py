class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        postfix = 1
        result = [1] * len(nums)
        for i in range(len(nums)):
            result[i] = prefix
            prefix *=  nums[i]
        
        for i in range(len(nums)-1, -1,-1):
            result[i] *= postfix 
            postfix *= nums[i]

        return result
            
        
        
        
        
        
        
        
        # pre = 1
        # post= 1
        # out = [1] * len(nums)
        # for i in range(len(nums)):
        #     out[i] = pre
        #     pre *=nums[i]

        # for i in range(len(nums)-1,-1,-1):
        #     out[i] *= post
        #     post*=nums[i]
        # return out


        
