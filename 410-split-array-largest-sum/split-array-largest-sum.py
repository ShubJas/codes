class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def feasible(S):
            total = 0
            splits = 1
            for n in nums:
                total += n
                if total > S:
                    total = n
                    splits +=1
                    if splits > k:
                        return False
            return True


        l = max(nums)
        r = sum(nums)

        while(l < r):

            m = (l+r)//2

            if(feasible(m)):
                r = m
            else:
                l =m + 1
        return l
        