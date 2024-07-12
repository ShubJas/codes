# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#  write in NB n Visulize
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Base case: if either list is empty, return None (no tree/subtree)
        if not preorder or not inorder:
            return None
        
        # The first element in preorder is always the root
        root = TreeNode(preorder[0])
        
        # Find the index of the root in inorder list
        mid = inorder.index(preorder[0])
        
        # Recursively build the left subtree
        # Left subtree: preorder[1:mid+1], inorder[:mid]
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        
        # Recursively build the right subtree
        # Right subtree: preorder[mid+1:], inorder[mid+1:]
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        
        return root
