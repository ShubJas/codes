# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def __init__(self):
    #     self.maxi = 0
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def height(node):
            if not node:
                return -1 # Return -1 as the height of an empty subtree
            nonlocal maxi
            # Recursively get the height of the left and right subtrees
            left_height = height(node.left)
            right_height = height(node.right)
            
            # The diameter at the current node is the sum of the heights of the
            # left and right subtrees plus 2 (for the edges connecting to the current node)
            maxi = max(maxi, 2 + left_height + right_height)
            
            # Return the height of the subtree rooted at the current node
            return 1 + max(left_height, right_height)
        maxi=0
        height(root)  # Calculate the height of the tree and update the maximum diameter
        return maxi
        