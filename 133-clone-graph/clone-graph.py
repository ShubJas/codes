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
        old_new = {}
        def dfs(node):
            if node in old_new:
                return old_new[node]
            newNode = Node(node.val)
            old_new[node]= newNode
            for neig in node.neighbors:
                newNode.neighbors.append(dfs(neig))
            return newNode
        
        return dfs(node) if node else None
