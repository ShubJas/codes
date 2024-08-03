class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        n  = len(nums)
        appear = n // 2

        count = defaultdict(int)

        for x in nums:

            count[x] += 1
        
        result = []
        for x,cnt in count.items():
            if cnt > appear:
                return x


# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:

#         n  = len(nums)
#         appear = n // 2

#         count = defaultdict(int)

#         for x in nums:

#             count[x] += 1
        
#         result = []
#         for x,cnt in count.items():
#             if cnt > appear:
#                 return x

        