# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # If the tree is empty, create a new node with the given value and return it
        if not root:
            return TreeNode(val)

        # If the value to be inserted is greater than the root's value,
        # insert it into the right subtree
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        # If the value to be inserted is less than the root's value,
        # insert it into the left subtree
        elif val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        
        # Return the root node after insertion
        return root
