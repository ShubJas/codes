class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:

        n = len(nums)


        def feasible(dist):
            count =0
            i = j =0
            while i < n:

                while j < n and nums[j] - nums[i] <= dist:
                    j+=1
                count += j - i -1
                i +=1
            
            return count >= k




            



        nums.sort()

        l = 0
        r = nums[-1] - nums[0]

        while l<r:

            mid = (l+r)//2

            if feasible(mid):
                r = mid
            else:
                l = mid+1

        return l


        # distances = []
        # for i in range(n-1):
        #     for j in range(i+1,n):
        #         distances.append(abs(nums[i]-nums[j]))
        

        # heapq.heapify(distances)

        # while k> 1:
        #     heapq.heappop(distances)
        #     k-=1
        
            
        # return heapq.heappop(distances)


        
        