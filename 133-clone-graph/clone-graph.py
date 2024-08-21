"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return node

        old_new = {}
        def dfs(node):


            if node in old_new:
                return old_new[node]
            
            old_new[node] = Node(node.val)

            for neighbor in node.neighbors:
                old_new[node].neighbors.append(dfs(neighbor))
            
            return old_new[node]
        
        return dfs(node)