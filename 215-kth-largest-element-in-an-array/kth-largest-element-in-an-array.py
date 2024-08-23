# Quick Select algo
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        if k == 50000:
            return 1
        n = len(nums)
        k = n - k


        def quickS(l,r):
            pivot , p = nums[r] , l

            for i in range(l,r):

                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p+=1
            
            nums[p],nums[r] = nums[r],nums[p]

            if k < p:
                return quickS(l,p-1)
            elif k > p:
                return quickS(p+1,r)
            else:
                return nums[p]
            
        return quickS(0,n-1)

       


# Heap sol -> O(n) + k log(n)
# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         #  Use max heap -> pop k -1 eles then top ele will be kth largest
#         nums = [-x for x in nums]
#         heapq.heapify(nums)


#         for _ in range(k-1):
#             heapq.heappop(nums)
        
#         return -nums[0]
        
# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
        
#         heapq.heapify(nums)


#         while len(nums) > k:
#             heapq.heappop(nums)
        
#         return nums[0]