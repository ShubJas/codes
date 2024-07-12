# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        # Base case: if preorder list is empty, return None
        if not preorder:
            return None

        # The first element in preorder is the root of the BST
        root = TreeNode(preorder[0])
        
        # If there is only one element, return it as the root
        if len(preorder) == 1:
            return root

        # Find the boundary between left and right subtrees using BST prop
        i = 1
        while i < len(preorder) and preorder[i] < preorder[0]:
            i += 1

        # Recursively construct the left and right subtrees
        root.left = self.bstFromPreorder(preorder[1:i])
        root.right = self.bstFromPreorder(preorder[i:])
        
        return root
