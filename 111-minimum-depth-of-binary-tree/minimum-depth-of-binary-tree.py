# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: 
            return 0
        self.minDepth=float('inf')

        self.dfs(root,0)

        return self.minDepth
    def dfs(self,node,curr_depth):
        if not node :
            return

        if not node.left and not node.right:
            self.minDepth=min(self.minDepth,curr_depth +1)
        self.dfs(node.left,curr_depth+1)
        self.dfs(node.right,curr_depth+1)    