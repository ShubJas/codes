# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Inner function to perform DFS and check path sums
        def inorder_dfs(root, curr_sum):
            if not root:
                return False  # If the current node is None, there is no path, return False
            
            curr_sum += root.val  # Add the current node's value to the current sum

            # If it's a leaf node, check if the current sum equals the targetSum
            if not root.left and not root.right:
                return curr_sum == targetSum
            
            # Recursively check the left and right subtrees
            return inorder_dfs(root.left, curr_sum) or inorder_dfs(root.right, curr_sum)
        
        # Start the DFS from the root with an initial sum of 0
        return inorder_dfs(root, 0)
