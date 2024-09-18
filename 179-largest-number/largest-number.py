class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        if nums.count(0) == len(nums):
            return '0'
        
        # for i,n in enumerate(nums):
        #     nums[i] = str(n)

        nums = map(str,nums)

        def compare(n1,n2):

            if n1 + n2 > n2 + n1: # means n1 is bigger(in str)
                return -1
            else:
                return 1

        nums = sorted(nums,key = cmp_to_key(compare))

        return ''.join(nums)

