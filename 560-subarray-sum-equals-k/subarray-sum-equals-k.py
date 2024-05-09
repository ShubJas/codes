class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        cursum = result = 0
        prefixfreq = defaultdict(int)
        prefixfreq[0] =1 

        for i in range(len(nums)):

            cursum += nums[i]
            diff = cursum - k

            result += prefixfreq[diff]

            prefixfreq[cursum]  += 1 
        return result


        