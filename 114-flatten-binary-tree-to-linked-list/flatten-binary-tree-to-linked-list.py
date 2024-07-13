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




        def dfs(root):
            

            if not root:
                return
            
            left = dfs(root.left)
            right = dfs(root.right)

            if root.left:
                left.next = root.right
                root.right = root.left
                root.left = None
            
            return root
        

        dfs(root)





#  Iterative approach
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
        
        curr = root  # Start with the root node

        while curr:  # Iterate over the tree
            if curr.left:  # If there is a left subtree
                if curr.right:  # If there is also a right subtree
                    temp = curr.right  # Store the right subtree temporarily
                    curr.right = curr.left  # Move the left subtree to the right
                    temp2 = curr.left  # Start from the left subtree
                    while temp2.right:  # Find the rightmost node of the left subtree
                        temp2 = temp2.right
                    temp2.right = temp  # Connect the original right subtree to the rightmost node of the left subtree
                else:
                    curr.right = curr.left  # If there is no right subtree, move the left subtree to the right
            curr.left = None  # Set the left child to None
            curr = curr.right  # Move to the next node (the right child)
        
        return root  # Return the modified root
