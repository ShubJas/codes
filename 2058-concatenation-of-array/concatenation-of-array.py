class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        nums.extend(nums)

        # for x in nums:
        #     ans.append(x)

        return nums