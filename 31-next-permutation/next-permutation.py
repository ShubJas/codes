class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        piv = len(nums) -2
        while piv>=0 and nums[piv+1]<=nums[piv]:
            piv-=1

        
        if piv>=0:
            j= len(nums)-1
            
            while nums[j]<=nums[piv]:
                j-=1
            
            nums[piv] , nums[j] = nums[j] , nums[piv]
        

        nums[piv+1:] = sorted(nums[piv+1:])
        












#         i = len(nums) - 2
#         while i >= 0 and nums[i] >= nums[i + 1]:
#             i -= 1
        
#         if i >= 0:
#             j = len(nums) - 1
#             while nums[j] <= nums[i]:
#                 j -= 1
#             nums[i], nums[j] = nums[j], nums[i]
        
#         nums[i + 1:] = reversed(nums[i + 1:])

# # This code correctly modifies nums in-place to the next permutation.
