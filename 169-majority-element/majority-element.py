#  Cancellation algo/ Boyer Moore’s Voting Algorithm
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        n  = len(nums)
        # as n/2 only one majority ele psbl 
        #  so one var

        appear = n // 2

        count = 0
        ele = 0
        
        for x in nums:
            if count == 0:
                ele = x
                count +=1
            elif x == ele:
                count +=1
            else:
                count -=1
        

        if nums.count(ele) > appear:
            return ele


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

        