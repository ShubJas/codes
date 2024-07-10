# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # If the tree is empty, return None
        if not root:
            return root
        
        # If the key to be deleted is smaller than the root's key,
        # then it lies in the left subtree
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        # If the key to be deleted is greater than the root's key,
        # then it lies in the right subtree
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        # If the key is the same as the root's key, then this is the node to be deleted
        else:
            # Node with only one child or no child
            if not root.right:
                return root.left
            elif not root.left:
                return root.right
            
            # Node with two children: Get the inorder successor (smallest
            # in the right subtree)
            curr = root.right
            while curr.left:
                curr = curr.left
            
            # Copy the inorder successor's value to this node
            root.val = curr.val
            
            # Delete the inorder successor
            root.right = self.deleteNode(root.right, root.val)
        
        # Return the root node after deletion
        return root
