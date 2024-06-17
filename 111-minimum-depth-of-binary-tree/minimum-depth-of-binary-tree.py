# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# BFS
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        q = collections.deque([(root,1)])


        while q:

            curr , curr_depth = q.popleft()

            if not curr:
                continue

            if not curr.left and not curr.right:
                return curr_depth
            
            
            
            q.append((curr.left,curr_depth + 1))
            q.append((curr.right,curr_depth + 1))
        
        return 0

            




        




# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right

# # DFS
# class Solution:
#     def minDepth(self, root: Optional[TreeNode]) -> int:


#         if not root:
#             return 0
        

#         left_depth = self.minDepth(root.left)
#         right_depth = self.minDepth(root.right)

#         if not root.left and not root.right:
#             return 1
        
#         if not root.left:
#             return 1 + right_depth
        
#         if not root.right:
#             return 1 + left_depth
        

#         return 1 + min(left_depth,right_depth)
        