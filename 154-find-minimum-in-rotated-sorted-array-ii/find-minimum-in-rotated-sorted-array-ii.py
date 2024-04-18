class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            # If the middle element is greater than the rightmost element, the minimum is in the right half
            if nums[m] > nums[r]:
                l = m + 1
            # Else, the minimum is in the left half including m
            elif nums[m]<nums[l]:
                r = m
            else:
                r-=1
        # After the loop, l will be the index of the minimum element
        return nums[l]
