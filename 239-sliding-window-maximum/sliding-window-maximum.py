from sortedcontainers import SortedList
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        dq = deque()
        result = []

        for i in range(k):
            while dq and nums[dq[-1]]<nums[i]:
                dq.pop()            
            dq.append(i)
        result.append(nums[dq[0]])

        for i in range(k,len(nums)):

            while dq and dq[0]<= i-k:
                dq.popleft()


            while dq and nums[dq[-1]]<nums[i]:
                dq.pop()            
            dq.append(i)
            result.append(nums[dq[0]])


        
        return result
        
        
        
        
        
        
        # result = []
        # sl= SortedList()
        # for n in nums[:k]:
        #     sl.add(n)
        # result.append(sl[-1])
        # for i in range(k,len(nums)):
        #     sl.remove(nums[i-k])
        #     sl.add(nums[i])
        #     result.append(sl[-1])
        
        # return result

            

        