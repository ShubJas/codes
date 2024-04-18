class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m
            
            # Check if the left half is normally sorted
            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:  # Target is in the normally sorted left half
                    r = m - 1
                else:
                    l = m + 1
            else:
                # The right half must be normally sorted
                if nums[m] < target <= nums[r]:  # Target is in the normally sorted right half
                    l = m + 1
                else:
                    r = m - 1

        return -1
