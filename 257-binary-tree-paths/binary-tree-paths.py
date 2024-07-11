# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        result = []


        def dfs(root,path,result):


            if not root:
                return
            
            path.append(str(root.val))

            if not root.left and not root.right:
                result.append('->'.join(path))
            else:
                dfs(root.left,path,result)
                dfs(root.right,path,result)
            path.pop()
        
        dfs(root,[],result)

        return result






# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right

# class Solution:
#     def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
#         result = []  # List to store all root-to-leaf paths

#         def dfs(root, path, result):
#             if not root:
#                 return  # If the current node is None, return immediately
            
#             path += str(root.val)  # Add the current node's value to the path
            
#             if not root.left and not root.right:
#                 # If the current node is a leaf, append the path to the result list
#                 result.append(path)
#             else:
#                 # If the current node is not a leaf, continue the depth-first search
#                 dfs(root.left, path + '->', result)  # Traverse the left subtree
#                 dfs(root.right, path + '->', result)  # Traverse the right subtree
        
#         dfs(root, '', result)  # Initialize the DFS with an empty path
#         return result  # Return the list of root-to-leaf paths
