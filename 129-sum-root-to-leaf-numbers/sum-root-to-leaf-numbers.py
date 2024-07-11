# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root, num):
            if not root:
                return 0  # If the current node is None, return 0
            
            num = num * 10 + root.val  # Update the current number
            
            if not root.left and not root.right:
                return num  # If it's a leaf node, return the current number
            
            # Recursively calculate the sum for left and right subtrees and return their sum
            return dfs(root.left, num) + dfs(root.right, num)
        
        return dfs(root, 0)  # Initialize the DFS with the root and an initial number 0




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        result = []  # List to store all root-to-leaf numbers

        def inorder_dfs(root, path, result):
            if not root:
                return  # If the current node is None, return immediately
            
            path.append(str(root.val))  # Add the current node's value to the path as a string

            if not root.left and not root.right:
                # If it's a leaf node, append the number formed by the path to result
                result.append(int(''.join(path)))
            
            # Recursively check the left and right subtrees
            inorder_dfs(root.left, path, result)
            inorder_dfs(root.right, path, result)
            
            path.pop()  # Backtrack by removing the last element from the path
        
        inorder_dfs(root, [], result)  # Initialize the DFS with the root and an empty path
        return sum(result)  # Return the sum of all numbers formed by root-to-leaf paths
