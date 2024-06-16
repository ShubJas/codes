# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxdia = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.depth(root)
        return self.maxdia

    
    def depth(self,root):

        left_depth = self.depth(root.left) if root.left else 0
        right_depth = self.depth(root.right) if root.right else 0

        self.maxdia = max(self.maxdia,left_depth+ right_depth)

        return 1 + max(left_depth,right_depth)



    
        