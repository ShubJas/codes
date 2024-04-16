# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, left=root)
        
        queue = [root]
        current_depth = 1
        # Perform BFS until reaching the level before the target depth
        while queue and current_depth < depth - 1:
            next_level = []
            for node in queue:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            queue = next_level
            current_depth += 1
        
        # At this point, queue contains all nodes at depth - 1
        for node in queue:
            # Insert new nodes
            node.left = TreeNode(val, left=node.left)
            node.right = TreeNode(val, right=node.right)
        
        return root
