class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        pos = 0
        neg = 1
        result = [0] * len(nums)
        for n in nums:
            if n > 0:
                result[pos] = n
                pos+=2
            else:
                result[neg] = n
                neg+=2
        
        return result

        



# class Solution:
#     def rearrangeArray(self, nums: List[int]) -> List[int]:
        
#         pos = []
#         neg = []

#         for n in nums:
#             if n > 0:
#                 pos.append(n)
#             else:
#                 neg.append(n)

#         nums = []
#         for x,y in zip(pos,neg):
#             nums.append(x)
#             nums.append(y)
        
#         return nums