# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.total = 0
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.dfs(root,low,high)

        return self.total



    def dfs(self,root,low,high):

        if not root:
            return

        if root.val > high:
            return self.dfs(root.left,low,high)

        if root.val < low:
            return self.dfs(root.right,low,high)
        

        self.total+= root.val


        root.left = self.dfs(root.left,low,high)
        root.right = self.dfs(root.right,low,high)

        return root
        