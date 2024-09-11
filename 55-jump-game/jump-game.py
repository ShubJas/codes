class Solution:
    def canJump(self, nums: List[int]) -> bool:
        


        n = len(nums)
        maxi = 0
        for i in range(n):

            if i > maxi:
                return False

            maxi = max(maxi, i + nums[i])

            if maxi >= n - 1:
                return True
        
        return True

#  Wrong sol
# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
        

#         i = 0
#         n = len(nums)
#         if n == 1 or n == 0 :
#             return True

#         while i < n - 1 :
#             print(i)
#             steps = nums[i]
#             if steps == 0:
#                 return False
#             move =  1
#             while i + move < min(i + steps + 1, n) and steps > nums[i + move]:
#                 move+=1
#             if move == steps + 1 :
#                 move -= 1
#             i = i + move
        
#         return True
