class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        xor = 0
        for n in nums:
            xor ^= n

        for n in range(len(nums)+1):
            xor ^= n
        
        return xor


# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
        
#         seen = set(nums)

#         for n in range(len(nums)+1):
#             if n not in seen:
#                 return n