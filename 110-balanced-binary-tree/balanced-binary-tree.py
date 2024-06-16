# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        return self.depth(root) >=0


    
    def depth(self,root):

        if not root:
            return 0
        
        left = self.depth(root.left)
        right = self.depth(root.right)

        if left < 0 or right < 0 or abs(left-right) > 1:
            return -1
        
        return 1 + max(left,right)



# Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def isBalanced(self, root: Optional[TreeNode]) -> bool:

#         if not root:
#             return True
        

#         return self.depth(root)[0]


    

#     def depth(self,node):
#         if not node:
#             return [True,0]
        
#         left = self.depth(node.left)
#         right =  self.depth(node.right)

#         balanced = left[0] and right[0] and abs(left[1]-right[1])<2 

#         return [balanced,1 + max(left[1],right[1])]
        


        
        