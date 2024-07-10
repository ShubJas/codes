# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.ans = 0  # Initialize ans to store the k-th smallest value
        self.count = 0  # Initialize count to manage the decrementing of k

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = k  # Set count to k, representing the number of nodes to visit before finding the k-th smallest
        self.inorder_dfs(root)  # Start the in-order traversal
        return self.ans  # Return the k-th smallest value after traversal

    def inorder_dfs(self, root: Optional[TreeNode]):
        if not root:
            return  # If the current node is None, return immediately
        
        # Recursively traverse the left subtree
        self.inorder_dfs(root.left)
        
        # Decrement count and check if it has reached 0
        self.count -= 1
        if self.count == 0:
            self.ans = root.val  # Set ans to the current node's value if count is 0
            return  # Return immediately to stop further unnecessary traversal
        
        # Recursively traverse the right subtree
        self.inorder_dfs(root.right)
