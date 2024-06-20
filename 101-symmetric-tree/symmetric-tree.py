# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# BFS
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:


        q = collections.deque([(root,root)])

        while q:
            a , b = q.popleft()

            if not a and not b:
                continue
            
            if not a or not b:
                return False
            
            if a.val != b.val:
                return False
            
            q.append((a.left,b.right))
            q.append((a.right,b.left))
        
        return True
        


        








#  DFS
# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def isSymmetric(self, root: Optional[TreeNode]) -> bool:

#         return self.same(root.left,root.right)

#     def same(self,p,q):

#         if not p and not q: 
#             return True
#         if (not p or not q) or (p.val != q.val):
#             return False
        
#         return self.same(p.left,q.right) and self.same(p.right,q.left)
        