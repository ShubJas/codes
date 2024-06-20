# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        return self.same(root.left,root.right)

    def same(self,p,q):

        if not p and not q: 
            return True
        if (not p or not q) or (p.val != q.val):
            return False
        
        return self.same(p.left,q.right) and self.same(p.right,q.left)
        