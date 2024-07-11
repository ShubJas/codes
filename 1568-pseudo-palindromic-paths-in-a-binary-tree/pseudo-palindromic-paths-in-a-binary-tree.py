# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:

        freq = defaultdict(int)
        self.result = 0

        def dfs(root,odd):

            if not root:
                return
            freq[root.val] +=1
            curr_odd = 1 if freq[root.val] % 2 == 1 else -1
            odd += curr_odd
            if not root.left and not root.right:
                if odd <= 1:
                    self.result+=1
            
            dfs(root.left,odd)
            dfs(root.right,odd)
            freq[root.val] -=1
            odd -= curr_odd
        
        dfs(root,0)

        return self.result
                
            

            
        