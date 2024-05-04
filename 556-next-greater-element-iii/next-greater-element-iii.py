class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums = [int(i) for i in str(n)]
        piv = len(nums)-2

        while piv >=0 and nums[piv] >=nums[piv+1]:
            piv-=1
        
        if piv == -1:
            return -1

        if piv>=0:
            
            j = len(nums) -1

            while nums[piv] >= nums[j]:
                j-=1
            

            nums[piv] , nums[j] = nums[j] , nums[piv]

            nums[piv+1:] = nums[piv+1:][::-1]

            result = int("".join(map(str,nums)))

            return result if result < 2**31 else -1
        

        