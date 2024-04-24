class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxval = sum(nums[:k])

        total = sum(nums[:k])
        for i in range(k,len(nums)):
            total = total + nums[i] - nums[i-k]
            maxval = max(maxval, total)
        

        return maxval/k

            
        