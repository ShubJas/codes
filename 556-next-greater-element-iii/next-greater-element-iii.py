class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums = list(map(int, str(n)))
        i = len(nums) - 2

        # Find the first decreasing element from the end
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i == -1:
            return -1

        # Find the element just larger than nums[i] to swap with
        j = len(nums) - 1
        while nums[j] <= nums[i]:
            j -= 1

        # Swap
        nums[i], nums[j] = nums[j], nums[i]

        # Reverse the sequence after the pivot
        nums[i + 1:] = reversed(nums[i + 1:])

        # Convert back to integer
        result = int(''.join(map(str, nums)))

        # If specific bounds are given, apply them
        return result if result < 2**31 else -1
