class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        

        def feasible(div):

            # total =0
            # for n in nums:
            #     total += (n-1)//div + 1
            # return total <= threshold

            return sum([(n-1)//div + 1 for n in nums]) <= threshold

        l = 1
        r = max(nums)

        while l<r:
            
            m = (l+r)//2

            if feasible(m):
                r = m
            else:
                l = m+1
        return l

        