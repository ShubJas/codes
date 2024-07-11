# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:


        def inorder_dfs(root,curr_sum):

            if not root:
                return False
            
            curr_sum += root.val

            if not root.left and not root.right:
                return curr_sum == targetSum
            
            return inorder_dfs(root.left,curr_sum)  or inorder_dfs(root.right, curr_sum)
        

        return inorder_dfs(root,0)


        