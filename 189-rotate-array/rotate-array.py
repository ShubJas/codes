class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        
        n = len(nums)
        k = k%n

        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])





        # def rev(l,r):
        #     while l<r:
        #         nums[l] , nums[r] = nums[r] , nums[l]
        #         l+=1
        #         r-=1
        
        # n = len(nums)
        # k = k%n
        # rev(0,n-1)
        # rev(0,k-1)
        # rev(k,n-1)
            

        
        
        
        
        
        
        
        
        
        
        # n = len(nums)
        # k = k % n  

        # def rot():
        #     last = nums[-1]
        #     for i in range(len(nums) - 1, 0, -1):
        #         nums[i] = nums[i - 1]
        #     nums[0] = last
        
        # for _ in range(k):
        #     rot()  
