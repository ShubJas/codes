class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        
        # Create a set of all children nodes (left and right)
        nodes = set(leftChild + rightChild)
        # Remove -1 from the set, as it represents a null child
        nodes.discard(-1) # discard - only removes if exist
        
        root = -1
        # Find the root node (the node that is not anyone's child)
        for i in range(n):
            if i not in nodes:
                root = i
                break
        
        visited = set()
        
        # Helper function to perform DFS and check for cycles and connectivity
        def dfs(root):
            if root == -1:
                return True  # If the node is null, it's valid
            
            if root in visited:
                return False  # If the node is already visited, there's a cycle

            visited.add(root)  # Mark the node as visited

            # Recursively validate the left and right children
            return dfs(leftChild[root]) and dfs(rightChild[root])

        # Validate the tree by performing DFS from the root
        # Check if all nodes are visited exactly once
        return dfs(root) and len(visited) == n
