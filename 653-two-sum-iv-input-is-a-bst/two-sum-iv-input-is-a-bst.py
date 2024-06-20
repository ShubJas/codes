# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.num  =set()
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool: 
    
        # if not root:
        #     return False
        # ai = k - root.val
        # if ai in self.num:
        #     return True
        
        # else:
        #     self.num.add(root.val)
        
        # return self.findTarget(root.left,k) or self.findTarget(root.right,k)
        
        if not root:
            return False
        

        q = collections.deque([root])

        while q:

            curr = q.popleft()

            if not curr:
                continue
            
            ai  = k - curr.val
            if ai in self.num:
                return True
            else:
                self.num.add(curr.val)

            q.append(curr.left)
            q.append(curr.right)
        
        return False