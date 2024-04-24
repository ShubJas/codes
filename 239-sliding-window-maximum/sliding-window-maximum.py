from sortedcontainers import SortedList
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        sl= SortedList()
        for n in nums[:k]:
            sl.add(n)
        result.append(sl[-1])
        for i in range(k,len(nums)):
            sl.remove(nums[i-k])
            sl.add(nums[i])
            result.append(sl[-1])
        
        return result

            

        