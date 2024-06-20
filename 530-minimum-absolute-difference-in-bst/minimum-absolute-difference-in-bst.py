# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        stack =[]
        curr = root
        prev = -10**5
        mindif = 10**5



        while stack or curr:

            while curr:
                stack.append(curr)
                curr = curr.left
            
            node = stack.pop()
            mindif = min(mindif, node.val - prev)
            prev = node.val
            curr = node.right
        

        return mindif

        


