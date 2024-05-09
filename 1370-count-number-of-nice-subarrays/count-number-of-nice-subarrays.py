class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1
        

        prefixfreq = {0:1}
        result = currsum = 0

        for i in range(len(nums)):
            currsum += nums[i]
            diff = currsum - k

            result += prefixfreq.get(diff,0)

            prefixfreq[currsum] = 1 + prefixfreq.get(currsum,0)
        
        return result

                                                                         