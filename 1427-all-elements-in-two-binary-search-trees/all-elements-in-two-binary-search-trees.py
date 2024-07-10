# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        arr1 = []
        arr2 = []


        self.inorder_dfs(root1,arr1)
        self.inorder_dfs(root2,arr2)

        res = []

        while len(arr1)>0 and len(arr2)>0:
            if arr1[0] >=arr2[0]:
                res.append(arr2.pop(0))
            else:
                res.append(arr1.pop(0))
            
        if len(arr1) >0:
            res+= arr1
        else:
            res+= arr2
        
        return res

    def inorder_dfs(self,root,arr):
        if not root:
            return 
        
        self.inorder_dfs(root.left,arr)
        arr.append(root.val)
        self.inorder_dfs(root.right,arr)
        