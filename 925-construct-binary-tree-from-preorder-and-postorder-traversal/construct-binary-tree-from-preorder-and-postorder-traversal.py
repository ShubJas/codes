# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # If either list is empty, return None
        if not preorder or not postorder:
            return None
        
        # The first element in preorder is always the root
        root = TreeNode(preorder[0])
        
        # If there is only one element, return the root immediately (base case for a single node)
        if len(preorder) == 1:
            return root
        
        # Find the root of the left subtree in postorder
        left_root_val = preorder[1]
        left_subtree_size = postorder.index(left_root_val) + 1
        
        # Construct the left and right subtrees recursively
        root.left = self.constructFromPrePost(preorder[1:left_subtree_size + 1], postorder[:left_subtree_size])
        root.right = self.constructFromPrePost(preorder[left_subtree_size + 1:], postorder[left_subtree_size:-1])
        
        # Return the constructed root node
        return root
