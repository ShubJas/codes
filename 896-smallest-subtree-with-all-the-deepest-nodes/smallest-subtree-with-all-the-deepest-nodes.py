# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        
        # Helper function to perform DFS and find the depth and LCA of deepest leaves
        def dfs(node: Optional[TreeNode]) -> Tuple[int, Optional[TreeNode]]:
            if not node:
                return (0, None)  # Base case: Return depth 0 and no LCA for null node
            
            # Recursively find the depth and LCA of the left subtree
            left_depth, left_lca = dfs(node.left)
            # Recursively find the depth and LCA of the right subtree
            right_depth, right_lca = dfs(node.right)
            
            # Compare the depths of the left and right subtrees
            if left_depth > right_depth:
                # If left subtree is deeper, return its depth + 1 and its LCA
                return (left_depth + 1, left_lca)
            elif right_depth > left_depth:
                # If right subtree is deeper, return its depth + 1 and its LCA
                return (right_depth + 1, right_lca)
            else:
                # If both subtrees have the same depth, return depth + 1 and current node as LCA
                return (left_depth + 1, node)
        
        # Call the dfs function starting from the root and return the LCA
        return dfs(root)[1]