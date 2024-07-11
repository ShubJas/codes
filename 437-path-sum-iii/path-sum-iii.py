# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.total_paths = 0
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        curr_sum = 0
        def dfs(root,curr_sum):

            if not root:
                return 
            

            curr_sum +=root.val
            if curr_sum ==  targetSum:
                self.total_paths +=1
            
            dfs(root.left,curr_sum)
            dfs(root.right,curr_sum)
        
        def traverse(root):
            if not root:
                return

            dfs(root,0)
            traverse(root.left)
            traverse(root.right)
        

        traverse(root)
        return self.total_paths


        