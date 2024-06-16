# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        result = []

        q = collections.deque([root])

        while q:
            temp = []
            for _ in range(len(q)):
                curr = q.popleft()
                if curr:
                    temp.append(curr.val)
                    q.append(curr.left)
                    q.append(curr.right)
            if temp:
                result.append(temp)
        
        for i in range(len(result)):
            if i & 1 == 1:
                result[i].reverse()
        
        return result


        



# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

#         result = []

#         q = collections.deque([root])
#         rev = 1
#         while q:
#             temp  =[]
#             for i in range(len(q)):
#                 curr = q.popleft()
#                 if curr:
#                     temp.append(curr.val)
#                     q.append(curr.left)
#                     q.append(curr.right)
#             if rev % 2 == 0:
#                 temp.reverse()
#             rev+=1
#             if temp:
#                 result.append(temp)
        
#         return result
        
                
        