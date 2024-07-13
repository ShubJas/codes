class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        
        nodes = set(leftChild + rightChild)
        nodes.discard(-1) # discard - only removes if exist
        root = -1
        for i in range(n):
            if i not in nodes:
                root = i
                break
        
        visited = set()
        def dfs(root):

            if root == -1:
                return True
            
            if root in visited:
                return False

            visited.add(root)

            return dfs(leftChild[root]) and dfs(rightChild[root])


        return dfs(root) and len(visited) == n

        

        
