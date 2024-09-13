#  Intuition - start from left follow rules considering only left, then do the same for right
class Solution:
    def candy(self, ratings: List[int]) -> int:
        


        left = [1]
        n = len(ratings)

        for i in range(n-1):

            if ratings[i+1] > ratings[i]:
                left.append(left[-1] + 1)
            else:
                left.append(1)
        S = 0
        right = 1
        for i in range(n-2,-1,-1):
            if ratings[i] > ratings[i+1]:
                right = right + 1
            else:
                right = 1

            
            S += max(left[i],right) 

        return S + left[-1]

# #  O(N) TC , 0(2N) SC
# class Solution:
#     def candy(self, ratings: List[int]) -> int:
        


#         arr = [1]
#         n = len(ratings)

#         for i in range(n-1):
#             left = 1
#             if ratings[i+1] > ratings[i]:
#                 left.append(left[-1] + 1)
#             else:
#                 left.append(1)
            
#             if ratings[n-i-2] > ratings[n-i-1]:
#                 right.append(right[-1] + 1)
#             else:
#                 right.append(1)
        


        
#         right = right[::-1]


#         # print([max(l,r) for l,r in zip(left,right)])
#         return sum([max(l,r) for l,r in zip(left,right)])
