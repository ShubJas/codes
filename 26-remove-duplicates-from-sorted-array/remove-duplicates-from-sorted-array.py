class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        i = j = 0 

        while i<len(nums):

            while i< len(nums)-1 and nums[i] == nums[i+1]:
                i+=1
            
            nums[j]=nums[i]
            j+=1
            i+=1

        return j
        