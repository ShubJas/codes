class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        cursum = result = 0
        prefixfreq = {0:1}

        for i in range(len(nums)):

            cursum += nums[i]
            diff = cursum - k

            result += prefixfreq.get(diff,0)

            prefixfreq[cursum] = 1 + prefixfreq.get(cursum,0)
        return result


        