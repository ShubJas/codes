# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Initialize the current node as the root
        curr = root

        # Loop until we find the LCA
        while curr:
            # If both p and q are greater than the current node's value, move to the right subtree
            if curr.val < p.val and curr.val < q.val:
                curr = curr.right
            # If both p and q are less than the current node's value, move to the left subtree
            elif curr.val > p.val and curr.val > q.val:
                curr = curr.left
            # If the current node's value is between p and q (inclusive), we have found the LCA
            else:
                return curr





# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None
# # Using DFS
# class Solution:
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
#         if p.val < q.val:
#             min_val, max_val = p.val, q.val
#         else:
#             min_val, max_val = q.val, p.val
        
#         def dfs(root):
#             if not root:
#                 return None
            
#             # If both p and q are less than root, then LCA lies in the left subtree
#             if root.val > max_val:
#                 return dfs(root.left)
#             # If both p and q are greater than root, then LCA lies in the right subtree
#             elif root.val < min_val:
#                 return dfs(root.right)
#             # If one node is on the left and the other is on the right, root is the LCA
#             else:
#                 return root
        
#         # Start DFS from the root
#         return dfs(root)
