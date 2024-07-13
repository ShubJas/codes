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

        def dfs(node: Optional[TreeNode]) -> Optional[TreeNode]:
            # Base case: if the node is None, return None
            if not node:
                return None
            
            # Recursively flatten the left and right subtrees
            left_tail = dfs(node.left)
            right_tail = dfs(node.right)

            # If there is a left subtree, we need to insert it
            # between the current node and the right subtree
            if node.left:
                # Connect the tail of the left subtree with the start of the right subtree
                if left_tail:
                    left_tail.right = node.right
                # Move the entire left subtree to the right
                node.right = node.left
                node.left = None  # Set the left child to None
            
            # We need to return the "tail" of the flattened subtree that starts at the current node.
            # The tail is the rightmost node of this subtree.
            # If there is a right tail, it is the tail of this subtree.
            # If there is no right tail but there is a left tail, the left tail is the tail of this subtree.
            # If there are no left or right tails, the current node is the tail.
            return right_tail or left_tail or node

        # Call the dfs helper function starting from the root
        dfs(root)




# #  Iterative approach
# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right

# class Solution:
#     def flatten(self, root: Optional[TreeNode]) -> None:
#         """
#         Do not return anything, modify root in-place instead.
#         """
        
#         curr = root  # Start with the root node

#         while curr:  # Iterate over the tree
#             if curr.left:  # If there is a left subtree
#                 if curr.right:  # If there is also a right subtree
#                     temp = curr.right  # Store the right subtree temporarily
#                     curr.right = curr.left  # Move the left subtree to the right
#                     temp2 = curr.left  # Start from the left subtree
#                     while temp2.right:  # Find the rightmost node of the left subtree
#                         temp2 = temp2.right
#                     temp2.right = temp  # Connect the original right subtree to the rightmost node of the left subtree
#                 else:
#                     curr.right = curr.left  # If there is no right subtree, move the left subtree to the right
#             curr.left = None  # Set the left child to None
#             curr = curr.right  # Move to the next node (the right child)
        
#         return root  # Return the modified root
