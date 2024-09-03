class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        result = []

        def backtrack(i):
            if i == n:
                result.append(nums[:])
                return


            for j in range(i,n):

                nums[i], nums[j] = nums[j], nums[i]
                backtrack(i+1)
                nums[i], nums[j] = nums[j], nums[i]

        backtrack(0)
        return result