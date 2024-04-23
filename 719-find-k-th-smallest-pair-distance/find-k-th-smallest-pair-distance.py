class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        


        def issmaller(dist):
            count = i = j = 0
            while i<n:

                while j<n and nums[j]-nums[i] <= dist:
                    j+=1
                count += j - i - 1
                i+=1
            return count >= k

            

        nums.sort()
        l = 0
        r = nums[-1] - nums[0]
        n = len(nums)
        while l<r:
            m = (l+r)//2

            if issmaller(m):
                r =m
            else:
                l = m+1
        return l


        # def issmaller(dist):
        #     count = 0
        #     for i in range(len(nums)-1):
        #         for j in range(i+1,len(nums)):
        #             if abs(nums[j]-nums[i]) <= dist:
        #                 count +=1
        #     return count >=k


        # l = 0
        # r = max(nums) - min(nums)
        
        # while l<r:
        #     m = (l+r)//2

        #     if issmaller(m):
        #         r =m
        #     else:
        #         l = m+1
        # return l