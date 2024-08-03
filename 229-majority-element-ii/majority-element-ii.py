class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        n  =len(nums)
        appear = n //3

        count = defaultdict(int)

        for x in nums:

            count[x] += 1
        
        result = []
        for x,cnt in count.items():
            if cnt > appear:
                result.append(x)


        return result
        