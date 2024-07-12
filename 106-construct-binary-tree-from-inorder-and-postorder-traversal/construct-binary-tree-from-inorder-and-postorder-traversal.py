# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#  write in NB n Visulize
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # Base case: if either list is empty, return None (no tree/subtree)
        if not inorder or not postorder:
            return
        
        # The last element in postorder is always the root of the current subtree
        root = TreeNode(postorder[-1])
        
        # Find the index of the root in the inorder list
        mid = inorder.index(postorder[-1])
        
        # Recursively build the left subtree
        # Left subtree: inorder[:mid], postorder[:mid]
        root.left = self.buildTree(inorder[:mid], postorder[:mid])
        
        # Recursively build the right subtree
        # Right subtree: inorder[mid+1:], postorder[mid:-1]
        root.right = self.buildTree(inorder[mid+1:], postorder[mid:-1])
        
        # Return the constructed tree/subtree
        return root
