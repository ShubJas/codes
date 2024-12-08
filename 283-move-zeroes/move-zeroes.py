class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if nums.count(0) == 0:
            return nums
            
        j = -1
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                j = i
                break
        

        for i in range(j+1,n):

            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j+=1


        

        