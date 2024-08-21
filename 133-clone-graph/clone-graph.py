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
            return None
            
        # Dictionary to map original nodes to their clones
        old_new = {}

        def dfs(node):

            # If the node has already been cloned, return the clone from the map
            if node in old_new:
                return old_new[node]

            # Clone the current node (only the value, neighbors will be added later)
            newNode = Node(node.val)
            
            # Map the original node to its clone
            old_new[node] = newNode
            
            # Iterate over all the neighbors of the current node
            for neig in node.neighbors:
                # Recursively clone the neighbors and add them to the clone's neighbors
                newNode.neighbors.append(dfs(neig))

            # Return the cloned node
            return newNode
        
        # If the input node is None, return None
        # Otherwise, start the DFS from the input node
        return dfs(node)