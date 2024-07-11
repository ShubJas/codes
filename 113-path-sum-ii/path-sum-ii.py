# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []  # List to store all paths that sum up to targetSum

        def inorder_dfs(root, cur_sum, path, result):
            if not root:
                return  # If the current node is None, return immediately

            path.append(root.val)  # Add the current node's value to the path
            cur_sum += root.val  # Update the current sum
            
            # Check if it's a leaf node and the current sum equals targetSum
            if not root.left and not root.right and cur_sum == targetSum:
                result.append(path[:])  # Append a copy of the current path to result
            
            # Recursively check the left and right subtrees
            inorder_dfs(root.left, cur_sum, path, result)
            inorder_dfs(root.right, cur_sum, path, result)
            
            path.pop()  # Backtrack by removing the last element from the path
        
        inorder_dfs(root, 0, [], result)  # Initialize the DFS with the root, initial sum, and an empty path
        return result  # Return the list of paths that sum up to targetSum
