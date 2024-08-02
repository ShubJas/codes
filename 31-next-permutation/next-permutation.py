class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # left of galti is sorted(correct) right is wrong
        # Step 1: Find the left Galti digit
        piv = len(nums) - 2 # second last element
        while piv >= 0 and nums[piv] >= nums[piv + 1]:
            piv -= 1

        # Step 2: If there is galiti
        if piv >= 0:
            # Step 3: Find the rightmost successor to the pivot in the suffix.
            j = len(nums) - 1
            
            while nums[j] <= nums[piv]:
                j -= 1
            
            # Step 4: Swap the pivot with its rightmost successor.
            nums[piv], nums[j] = nums[j], nums[piv]

        # Step 5: Reverse the suffix to get the next smallest lexicographical permutation.
        nums[piv + 1:] = sorted(nums[piv + 1:])

#  1   3   2
#  piv
#  1   3    2
#  piv      j
#  exchange
#  2   3    1
#  piv| sort
#  2   1    3  