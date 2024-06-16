# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
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
            if q:
                result.append(temp)
        return result


        



# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def __init__(self):
#         self.result = []
#     def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         Q = deque([root])
#         if not root:
#             return None
#         while Q:
#             temp = []
#             sub_list_length = len(Q)
#             for _ in range(sub_list_length):
#                 curr = Q.popleft()
#                 if curr.left:
#                     Q.append(curr.left)
#                 if curr.right:
#                     Q.append(curr.right)
#                 temp.append(curr.val)
#             self.result.append(temp)
        
#         return self.result



        