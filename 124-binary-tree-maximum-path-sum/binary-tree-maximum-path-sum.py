# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.maxsum = -float("inf")  # Initialize maxsum to negative infinity

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return 0  # Return 0 for null nodes

            # Recursively get the max path sum of left and right subtrees
            left_max = max(dfs(root.left), 0)  # Ignore paths with negative sums
            right_max = max(dfs(root.right), 0)  # Ignore paths with negative sums

            # Calculate the path sum passing through the current node
            current_sum = root.val + left_max + right_max

            # Update the global maximum path sum
            self.maxsum = max(self.maxsum, current_sum)

            # Return the maximum path sum of the current node
            return root.val + max(left_max, right_max)

        dfs(root)  # Start the DFS traversal from the root
        return self.maxsum  # Return the global maximum path sum
