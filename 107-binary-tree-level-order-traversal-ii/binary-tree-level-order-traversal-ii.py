# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:

        result = []
        q = collections.deque([root])

        while q:

            temp = []
            for _ in range(len(q)):
                curr = q.popleft()
                if curr:
                    temp.append(curr.val)
                    q.append(curr.left)
                    q.append(curr.right)
            
            if temp:
                result.append(temp)
        
        return result[::-1]
    

        