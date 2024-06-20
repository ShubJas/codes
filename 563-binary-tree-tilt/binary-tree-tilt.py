# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.total = 0
    

    def tilt(self,root):
        if not root:
            return 0
        
        
        left_sum = self.tilt(root.left) 
        right_sum = self.tilt(root.right)

        self.total += abs(left_sum - right_sum)

        return root.val + left_sum + right_sum
    
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.tilt(root)
        return self.total
        