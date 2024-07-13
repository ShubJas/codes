# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional, Tuple

class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # Helper function to perform DFS and find the depth and LCA of deepest leaves
        def dfs(root):
            if not root:
                return (0, None)  # Base case: Return depth 0 and no LCA for null root
            
            # Recursively find the depth and LCA of the left subtree
            left_depth, left_lca = dfs(root.left)
            # Recursively find the depth and LCA of the right subtree
            right_depth, right_lca = dfs(root.right)
            
            # Compare the depths of the left and right subtrees
            if left_depth > right_depth:
                # If left subtree is deeper, return its depth + 1 and its LCA
                return (left_depth + 1, left_lca)
            elif right_depth > left_depth:
                # If right subtree is deeper, return its depth + 1 and its LCA
                return (right_depth + 1, right_lca)
            else:
                # If both subtrees have the same depth, return depth + 1 and current root as LCA
                return (left_depth + 1, root)
        
        # Call the dfs function starting from the root and return the LCA
        return dfs(root)[1]








# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right

# class Solution:
#     def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
#         # List to store nodes at each level
#         vals = []
        
#         # Helper function to perform level order traversal
#         def levelorder_bfs(root):
#             # Initialize deque for level order traversal
#             q = collections.deque([root])
#             while q:
#                 qlen = len(q)  # Number of nodes at current level
#                 temp = []  # Temporary list to store nodes at current level
#                 for _ in range(qlen):
#                     curr = q.popleft()  # Pop the leftmost node from queue
#                     if curr:
#                         temp.append(curr)  # Append current node to temp list
#                         q.append(curr.left)  # Add left child to queue
#                         q.append(curr.right)  # Add right child to queue
#                 if temp:
#                     vals.append(temp)  # Add current level nodes to vals
        
#         # Helper function to find LCA of two nodes
#         def ances(root, p, q):
#             if not root:
#                 return None  # If root is None, return None

#             if root == p or root == q:
#                 return root  # If root is either p or q, return root
            
#             # Recursively find LCA in left and right subtrees
#             left = ances(root.left, p, q)
#             right = ances(root.right, p, q)

#             if left and right:
#                 return root  # If both left and right are non-None, root is LCA
            
#             return left if left else right  # Otherwise, return non-None value

#         # Perform level order traversal to populate vals
#         levelorder_bfs(root)

#         # Get the deepest leaves
#         deepest_leaves = vals[-1]
        
#         # If there is only one deepest leaf, return it
#         if len(deepest_leaves) == 1:
#             return deepest_leaves[0]
#         else:
#             # Find the LCA for all deepest leaves
#             ancestor = deepest_leaves[0]
#             for node in deepest_leaves[1:]:
#                 ancestor = ances(root, ancestor, node)
#             return ancestor
