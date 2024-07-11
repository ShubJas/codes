# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:



        result = []
        def inorder_dfs(root,path,result):
            

            if not root:
                return 
            
            path.append(str(root.val))
            if not root.left and not root.right:
                result.append(int(''.join(path)))
            
            inorder_dfs(root.left,path,result)
            inorder_dfs(root.right,path,result)
            path.pop()
        

        inorder_dfs(root,[],result)
        return sum(result)
        