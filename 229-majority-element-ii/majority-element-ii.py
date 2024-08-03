#  Cancellation algo/ Boyer Moore’s Voting Algorithm
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        n  =len(nums)
        appear = n // 3
        # as / 3 , there are 2 max elements possible so 2 vars


        count1 = count2 = 0 
        ele1 = ele2 = -1


        for x in nums:
            # keeps count of the 1st ele so it shoudnt be 2nd ele
            if count1 == 0 and x != ele2:
                ele1 = x
                count1 += 1
            # keeps count of the 2st ele so it shoudnt be 1nd ele
            elif count2 == 0 and x != ele1:
                ele2 = x
                count2 += 1 

            elif x == ele1:
                count1 += 1
            elif x == ele2:
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        
        result = set()

        if nums.count(ele1) > appear:
            result.add(ele1)

        
        if nums.count(ele2) > appear:
            result.add(ele2)


        return list(result)

# class Solution:
#     def majorityElement(self, nums: List[int]) -> List[int]:

#         n  =len(nums)
#         appear = n //3

#         count = defaultdict(int)

#         for x in nums:

#             count[x] += 1
        
#         result = []
#         for x,cnt in count.items():
#             if cnt > appear:
#                 result.append(x)


#         return result
        
        