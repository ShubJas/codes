# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        result = []
        def inorder_dfs(root,cur_sum,path,result):

            if not root:
                return 
            cur_sum += root.val
            path.append(root.val)
            if not root.left and not root.right and cur_sum == targetSum:
                result.append(path[:])
                
            
            inorder_dfs(root.left,cur_sum,path,result)
            inorder_dfs(root.right,cur_sum,path,result)
            path.pop()
        
        inorder_dfs(root,0,[],result)

        return result
            



            

            
        