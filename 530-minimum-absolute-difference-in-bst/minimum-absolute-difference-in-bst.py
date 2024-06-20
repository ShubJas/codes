# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        

        arr = []
        min_diff = 10**5

        def dfs_inorder(root):

            if not root:
                return 
            
            dfs_inorder(root.left)
            arr.append(root.val)
            dfs_inorder(root.right)
        
        dfs_inorder(root)

        for i in range(len(arr)-1):
            min_diff =min(min_diff,arr[i+1]-arr[i])
        
        return min_diff


        # stack =[]
        # curr = root
        # prev = -10**5
        # mindif = 10**5



        # while stack or curr:

        #     while curr:
        #         stack.append(curr)
        #         curr = curr.left
            
        #     node = stack.pop()
        #     mindif = min(mindif, node.val - prev)
        #     prev = node.val
        #     curr = node.right
        

        # return mindif

        


