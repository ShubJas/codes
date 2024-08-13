class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        nums.reverse()

        n = len(nums)
        k = k % n 

        nums[k:] = reversed(nums[k:])
        nums[:k] = reversed(nums[:k])
        return nums

        # n = len(nums)

        # rot = k % n 


        # def rotate(nums):
        #     last = nums[n-1]
        #     for i in range(n-1,0,-1):
        #         nums[i] = nums[i-1]
        #     nums[0] = last


        # for i in range(rot):
        #     rotate(nums)
        

        # return nums
        