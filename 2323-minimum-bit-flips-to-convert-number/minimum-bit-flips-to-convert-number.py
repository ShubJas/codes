class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        count = 0
        while start or goal:
            if start & 1 != goal & 1:
                count+=1
            start >>= 1
            goal >>= 1
        
        return count


# class Solution:
#     def minBitFlips(self, start: int, goal: int) -> int:

#         start = bin(start)[2:][::-1]
#         goal = bin(goal)[2:][::-1]

#         l = max(len(start),len(goal))

#         while len(start) < l:
#             start += '0'

#         while len(goal) < l:
#             goal += '0'

#         i = count =  0
#         while i < l:
#             if start[i] != goal[i]:
#                 count+=1
#             i+=1

#         return count
        