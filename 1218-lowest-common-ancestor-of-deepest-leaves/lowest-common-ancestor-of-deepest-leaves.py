# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections
from typing import Optional, List

class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        vals = []
        
        def levelorder_bfs(root):
            q = collections.deque([root])
            while q:
                qlen = len(q)
                temp = []
                for _ in range(qlen):
                    curr = q.popleft()  
                    if curr:
                        temp.append(curr)
                        q.append(curr.left)
                        q.append(curr.right)
                if temp:
                    vals.append(temp)
        
        def ances(root, p, q):
            if not root:
                return None

            if root == p or root == q:
                return root
            
            left = ances(root.left, p, q)
            right = ances(root.right, p, q)

            if left and right:
                return root
            
            return left if left else right

        levelorder_bfs(root)

        deepest_leaves = vals[-1]
        
        if len(deepest_leaves) == 1:
            return deepest_leaves[0]
        else:
            ancestor = deepest_leaves[0]
            for node in deepest_leaves[1:]:
                ancestor = ances(root, ancestor, node)
            return ancestor
