class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        total = ans =0
        seen = defaultdict(int)
        for i in range(k):
            total +=nums[i]
            seen[nums[i]]+=1
        if(len(seen)== k):
            ans = total
        for i in range(k,len(nums)):
            total = total - nums[i-k] + nums[i] 
            seen[nums[i-k]]-=1
            if seen[nums[i-k]]==0:
                del seen[nums[i-k]]
            seen[nums[i]]+=1
            if(len(seen)==k):
                ans = max(ans,total)
        return ans