class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        for i , num in enumerate(nums):
            if abs(i - num) > 1:
                return False
        
        return True

        '''In a perfectly sorted permutation nums of integers from 0 to n-1, the number at index i should be i itself (i.e., nums[i] = i).
If the element nums[i] is x, then nums[x] should ideally be x. However, the solution checks if abs(x - nums[x]) > 1.
This condition ensures that the value at any position is not more than one index away from its actual value. If this condition is satisfied, then all global inversions are also local inversions, and vice versa.'''


# class Solution:
#     def isIdealPermutation(self, nums: List[int]) -> bool:
#         # cant use global vars as there is recursive function calls
#         # so use mutable Dstructure
#         # 0 - global, 1 - local 
#         inv = [0, 0]

#         def merge_sort(A):
#             def mergesort(low, high, A):
#                 if low >= high:
#                     return

#                 m = (low + high) // 2

#                 mergesort(low, m, A)
#                 mergesort(m + 1, high, A)
#                 merge(low, m, high, A)

#             def merge(low, m, high, A):
#                 temp = []
#                 l = low
#                 r = m + 1

#                 while l <= m and r <= high:
#                     if A[l] <= A[r]:
#                         temp.append(A[l])
#                         l += 1
#                     else:
#                         inv[0] += (m - l + 1)  # Global inversions
#                         temp.append(A[r])
#                         r += 1

#                 while l <= m:
#                     temp.append(A[l])
#                     l += 1

#                 while r <= high:
#                     temp.append(A[r])
#                     r += 1

#                 for i in range(low, high + 1):
#                     A[i] = temp[i - low]

#             low = 0
#             high = len(A) - 1
#             mergesort(low, high, A)

#         # Count local inversions
#         for i in range(len(nums) - 1):
#             if nums[i] > nums[i + 1]:
#                 inv[1] += 1

#         merge_sort(nums[:])  # Pass a copy of nums to avoid modification

#         return inv[0] == inv[1]


# class Solution:
#     def isIdealPermutation(self, nums: List[int]) -> bool:


#         loc = glo = 0
#         n = len(nums)
#         j = n -1
#         while j > 0 :
#             for i in range(j-1,-1,-1):
#                 if nums[i] > nums[j]:

#                     if j == i+1:
#                         loc +=1   
#                     glo +=1
#             j -=1
        
#         return glo == loc

