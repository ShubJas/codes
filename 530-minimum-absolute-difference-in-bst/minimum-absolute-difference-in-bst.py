# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        list=[]
        def dfs_in_order(root):
            if not root:
                return 
            dfs_in_order(root.left)
            list.append(root.val)
            dfs_in_order(root.right)
        dfs_in_order(root)
        min_ans=float("inf")
        for n in range(1,len(list)):
            min_ans=min(min_ans,(list[n]-list[n-1]))
        return min_ans


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

        


