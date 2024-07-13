# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # Helper function to validate the BST
        def validate(node, low, high):
            # An empty tree is a valid BST
            if not node:
                return True

            # Check if the current node's value is within the valid range
            if node.val <= low or node.val >= high:
                return False
            
            # Recursively validate the left and right subtrees
            # For the left subtree, update the upper bound
            # For the right subtree, update the lower bound
            return validate(node.left, low, node.val) and validate(node.right, node.val, high)

        # Initialize the recursion with the entire range of valid values
        return validate(root, float('-inf'), float('inf'))
