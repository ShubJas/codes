class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n  # Adjust k to be within the bounds of nums' length

        # Helper function to reverse a portion of the array
        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start, end = start + 1, end - 1
        
        # Reverse the entire array
        reverse(0, n - 1)
        # Reverse the first k elements
        reverse(0, k - 1)
        # Reverse the rest of the array
        reverse(k, n - 1)

        
        
        
        
        
        
        
        
        
        
        # n = len(nums)
        # k = k % n  

        # def rot():
        #     last = nums[-1]
        #     for i in range(len(nums) - 1, 0, -1):
        #         nums[i] = nums[i - 1]
        #     nums[0] = last
        
        # for _ in range(k):
        #     rot()  
