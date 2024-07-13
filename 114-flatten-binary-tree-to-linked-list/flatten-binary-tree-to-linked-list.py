# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        curr = root

        while curr:

            if curr.left:
                if curr.right:

                    temp = curr.right
                    curr.right = curr.left
                    temp2 = curr.left
                    while temp2.right:
                        temp2 = temp2.right
                    temp2.right = temp
                else:
                    curr.right = curr.left
            curr.left = None
            curr = curr.right        
        
        return root



        