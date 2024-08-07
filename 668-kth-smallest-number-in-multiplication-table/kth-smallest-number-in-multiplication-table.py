class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        

        def feasible(num):
            count = 0
            for row in range(1,m+1):
                count += min(num // row, n)
                # if num//row > n:
                #     count+=n
                # else:
                #     count+= num//row
            
            return count>=k


        l = 1
        r = m*n

        while l<r:
            mid = (l+r)//2
            if feasible(mid):
                r = mid
            else:
                l = mid+1
        
        return l

# import heapq

# class Solution:
#     def findKthNumber(self, m: int, n: int, k: int) -> int:
#         # Generate all elements in the multiplication table
#         arr = []

#         for r in range(1, m + 1):
#             for c in range(1, n + 1):
#                 arr.append(r * c)

#         # Transform the list into a heap
#         heapq.heapify(arr)

#         # Pop elements k-1 times to get the k-th smallest element
#         while k > 1:
#             heapq.heappop(arr)
#             k -= 1

#         # Return the k-th smallest element
#         return heapq.heappop(arr)
