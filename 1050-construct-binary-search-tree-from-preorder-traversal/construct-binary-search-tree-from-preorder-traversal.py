# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        # Index to keep track of the current position in the preorder list
        self.index = 0
        
        def buildBST(preorder, lower, upper):
            # If all elements are processed or the current element is out of bounds, return None
            if self.index == len(preorder) or not (lower < preorder[self.index] < upper):
                return None
            
            # Get the current element and move the index forward
            val = preorder[self.index]
            self.index += 1
            
            # Create a new TreeNode with the current value
            root = TreeNode(val)
            
            # Recursively build the left subtree with updated upper bound
            root.left = buildBST(preorder, lower, val)
            
            # Recursively build the right subtree with updated lower bound
            root.right = buildBST(preorder, val, upper)
            
            return root
        
        # Start the recursive construction with initial boundaries
        return buildBST(preorder, float('-inf'), float('inf'))
