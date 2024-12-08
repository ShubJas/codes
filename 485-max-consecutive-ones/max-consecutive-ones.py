class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        

        count = maxi = 0

        for x in nums:
            
            if x == 0:
                count = 0
            else:
                count+=1
            if maxi < count:
                maxi = count

        return maxi