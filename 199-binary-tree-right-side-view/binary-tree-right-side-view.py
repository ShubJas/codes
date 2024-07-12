# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import List, Optional
import collections

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # List to store the right side view of the tree
        result = []
        
        # If the root is None, return the empty result list
        if not root:
            return result
        
        # Initialize a deque (queue) with the root node
        q = collections.deque([root])
        
        # Perform level order traversal
        while q:
            # Variable to keep track of the rightmost node at each level
            right_node = None
            # Get the number of nodes at the current level
            qlen = len(q)
            # Iterate over all nodes at the current level
            for _ in range(qlen):
                curr = q.popleft()
                if curr:
                    # Update right_node to the current node
                    right_node = curr
                    # Add the left child to the queue
                    q.append(curr.left)
                    # Add the right child to the queue
                    q.append(curr.right)
            # After processing all nodes at the current level, add the value of right_node to the result list
            if right_node:
                result.append(right_node.val)
        
        # Return the list of right side view values
        return result
