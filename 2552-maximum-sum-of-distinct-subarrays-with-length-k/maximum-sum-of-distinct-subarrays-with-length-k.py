class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:

        seen= defaultdict(int)
        total = result = 0
        for i in range(k):
            total += nums[i]
            seen[nums[i]]+=1
        
        if len(seen) == k:
            result = total
        
        for i in range(k,len(nums)):
            total = total + nums[i] - nums[i-k]
            seen[nums[i-k]] -=1
            if seen[nums[i-k]] == 0:
                del seen[nums[i-k]]
            seen[nums[i]]+=1
            
            if len(seen) == k:
                result = max(total,result)
        return result